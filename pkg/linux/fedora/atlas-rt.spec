Name: atlas-rt
Version: 0.1.4
Release: 1%{?dist}
License: GPLv3
Summary: An overlay type system for shell pipelines
Url: https://github.com/davidkovach-fuentes/rt

# Full-repo tarball (must include repo-root scripts/). Copr make_srpm / .copr/Makefile
# creates this from git; do not use Copr method=tito (it only packs this subdirectory).
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

Requires: moby-engine

%description
Rt catches data incompatibilities in shell pipelines before they run.
Give it a shell program and it tells you when one command produces data the next command can't consume
-- with a concrete counterexample showing exactly what breaks.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
# git archive --prefix=rt-%{version}/  (see .copr/Makefile)
%autosetup -n rt-%{version}

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 scripts/run-in-container.sh %{buildroot}%{_bindir}/rt
ln -s rt %{buildroot}%{_bindir}/rti

#-- FILES ---------------------------------------------------------------------#
%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%{_bindir}/rt
%{_bindir}/rti

#-- CHANGELOG -----------------------------------------------------------------#
%changelog
* Sun Aug 23 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> 0.1.4-1
- 

* Sun Aug 23 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> 0.1.3-1
- use full-repo source tree so scripts/ is available during %%install

* Sun Aug 23 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> v0.1.3-1
- adjust SPEC chroot (davidkovach-fuentes2027@u.northwestern.edu)

* Sun Aug 23 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> v0.1.2-1
- create releases, move SPEC (davidkovach-fuentes2027@u.northwestern.edu)

* Fri Aug 21 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> 0.1.4-1
-

* Fri Aug 21 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> 0.1.3-1
- new package built with tito

* Fri Aug 21 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> 0.1.2-1
-

* Fri Aug 21 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> 0.1.2-1
-

* Fri Aug 21 2026 Unknown name 0.1.1-1
- new package built with tito
- renamed rt to atlas-rt
