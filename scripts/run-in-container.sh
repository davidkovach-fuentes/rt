#! /usr/bin/env sh

set -eu

image_remote="${RT_IMAGE_REMOTE:-ghcr.io/davidkovach-fuentes/rt:latest}"
image="${RT_IMAGE:-$image_remote}"
runtime="${RT_RUNTIME:-docker}"

if ! command -v "$runtime" >/dev/null 2>&1; then
    echo "rt: '$runtime' not found" >&2
    echo "    install Docker: https://docs.docker.com/get-docker/" >&2
    exit 1
fi

if ! "$runtime" info >/dev/null 2>&1; then
    echo "rt: cannot connect to the $runtime daemon" >&2
    echo "    ensure Docker is running and try again" >&2
    exit 1
fi

if ! "$runtime" image inspect "$image" >/dev/null 2>&1; then
    echo "rt: pulling '$image_remote'..." >&2
    if ! "$runtime" pull "$image_remote" >&2; then
        echo "rt: failed to pull '$image_remote'" >&2
        echo "    check that the image is public, or build locally:" >&2
        echo "      docker build --target sys -t rt ." >&2
        echo "      export RT_IMAGE=rt" >&2
        exit 1
    fi
    image="$image_remote"
fi

# Remember how many arguments were in argv at this point
init_argv="$#"

# Loop 1: build the docker args
argv=$init_argv
for arg; do
    argv=$((argv - 1))
    
    if [ -f "$arg" ]; then
        arg="$(realpath "$arg")"
        set -- "$@" -v  "${arg}:${arg}:ro"
        echo "$@"
    fi

    if [ "$argv" -eq 0 ]; then
        break
    fi
done

set -- "$@" "$image"

# Loop 2: build the rt args
if [ "$init_argv" -gt 0 ]; then
    argv=$init_argv
    for arg; do
        argv=$((argv - 1))

        if [ -f "$arg" ]; then
            arg="$(realpath "$arg")"
        fi

        set -- "$@" "$arg"

        if [ "$argv" -eq 0 ]; then
            break
        fi
    done
fi

# Pop all initial args
shift "$init_argv"

exec "$runtime" run --rm --interactive "$@"
