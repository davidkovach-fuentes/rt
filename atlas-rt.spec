Name: atlas-rt
Version: 0.1.4
Release: 1%{?dist}
License: MIT
Summary: An overlay type system for shell pipelines
Url: https://github.com/davidkovach-fuentes/rt
# Sources can be obtained by
# git clone https://github.com/davidkovach-fuentes/rt
# cd rt
# tito build --tgz
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

Requires: moby-engine

%description
Rt catches data incompatibilities in shell pipelines before they run.
Give it a shell program and it tells you when one command produces data the next command can't consume
-- with a concrete counterexample showing exactly what breaks.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup

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
* Thu Aug 27 2026 github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com>
- no (davidkovach-fuentes2027@u.northwestern.edu)
- stop throwing (davidkovach-fuentes2027@u.northwestern.edu)
- tito --version (davidkovach-fuentes2027@u.northwestern.edu)
- no (davidkovach-fuentes2027@u.northwestern.edu)
- tito --version (davidkovach-fuentes2027@u.northwestern.edu)
- like just work (davidkovach-fuentes2027@u.northwestern.edu)
- one more time or i give up (davidkovach-fuentes2027@u.northwestern.edu)
- just work (davidkovach-fuentes2027@u.northwestern.edu)
- stop tweaking my stuff (davidkovach-fuentes2027@u.northwestern.edu)
- no (davidkovach-fuentes2027@u.northwestern.edu)
- no (davidkovach-fuentes2027@u.northwestern.edu)
- no (davidkovach-fuentes2027@u.northwestern.edu)
- just like work do something (davidkovach-fuentes2027@u.northwestern.edu)
- rm sudo (davidkovach-fuentes2027@u.northwestern.edu)
- change workflow container to Fedora (davidkovach-
  fuentes2027@u.northwestern.edu)
- add pip install tito (davidkovach-fuentes2027@u.northwestern.edu)
- tweak Install Dependencies (davidkovach-fuentes2027@u.northwestern.edu)
- change to release-based (davidkovach-fuentes2027@u.northwestern.edu)
- workflow to update package (davidkovach-fuentes2027@u.northwestern.edu)
- Automatic commit of package [atlas-rt] release [0.1.3-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- test workflow (davidkovach-fuentes2027@u.northwestern.edu)
- prepare for PR (davidkovach-fuentes2027@u.northwestern.edu)
- test for webhook rebuild (davidkovach-fuentes2027@u.northwestern.edu)
- Automatic commit of package [atlas-rt] release [v0.1.1-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- revert to webhooks and place spec in root (davidkovach-
  fuentes2027@u.northwestern.edu)
- Automatic commit of package [atlas-rt] release [0.1.1-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- Automatic commit of package [atlas-rt] release [0.1.0-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- stop duplicate Copr job (davidkovach-fuentes2027@u.northwestern.edu)
- update spec, srpm (davidkovach-fuentes2027@u.northwestern.edu)
- update spec, srpm (davidkovach-fuentes2027@u.northwestern.edu)
- change to MIT License (davidkovach-fuentes2027@u.northwestern.edu)
- restructure & separate workflows (davidkovach-fuentes2027@u.northwestern.edu)
- Fix Copr Makefile for dash and speed up Actions checkout (davidkovach-
  fuentes2027@u.northwestern.edu)
- tweak copr makefile (davidkovach-fuentes2027@u.northwestern.edu)
- Stop cleanup from deleting  build-packages.sh was rm -rf'ing pkg/linux, which
  removed build-srpm.sh (davidkovach-fuentes2027@u.northwestern.edu)
- Fix Copr release workflow: build SRPM from repo root (davidkovach-
  fuentes2027@u.northwestern.edu)
- fix merge conflict (davidkovach-fuentes2027@u.northwestern.edu)
- update release workflow (davidkovach-fuentes2027@u.northwestern.edu)
- test workflow for release-based Copr (davidkovach-
  fuentes2027@u.northwestern.edu)
- test workflow for release-based Copr (davidkovach-
  fuentes2027@u.northwestern.edu)
- Automatic commit of package [atlas-rt] release [v0.1.1-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- Automatic commit of package [atlas-rt] release [0.1.2-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- Automatic commit of package [atlas-rt] release [0.1.1-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- Automatic commit of package [atlas-rt] release [0.1.2-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- Automatic commit of package [atlas-rt] release [0.1.1-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- Automatic commit of package [atlas-rt] release [0.1.5-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- update README (davidkovach-fuentes2027@u.northwestern.edu)
- Fix Copr Fedora build with make_srpm and full-repo archive (davidkovach-
  fuentes2027@u.northwestern.edu)
- Automatic commit of package [atlas-rt] release [0.1.4-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- Automatic commit of package [atlas-rt] release [v0.1.3-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- adjust SPEC chroot (davidkovach-fuentes2027@u.northwestern.edu)
- Automatic commit of package [atlas-rt] release [v0.1.2-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- create releases, move SPEC (davidkovach-fuentes2027@u.northwestern.edu)
- Automatic commit of package [atlas-rt] release [v0.1.1-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- restructure and rename packaging scripts & folders (davidkovach-
  fuentes2027@u.northwestern.edu)
- restructure and rename packaging scripts & folders (davidkovach-
  fuentes2027@u.northwestern.edu)
- rename SPEC to 'atlas-rt' (davidkovach-fuentes2027@u.northwestern.edu)
- Automatic commit of package [atlas-rt] release [0.1.4-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- Automatic commit of package [atlas-rt] release [0.1.3-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- Document packaging/dist; keep RPM/tarball artifacts gitignored (davidkovach-
  fuentes2027@u.northwestern.edu)
- tito build; initialize Copr repository (davidkovach-
  fuentes2027@u.northwestern.edu)
- Automatic commit of package [rt] release [0.1.2-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- Automatic commit of package [rt] release [0.1.2-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- Automatic commit of package [rt] release [0.1.1-1]. (davidkovach-
  fuentes2027@u.northwestern.edu)
- upload spec file, tito init (davidkovach-fuentes2027@u.northwestern.edu)
- update install inst: use 'dnf install -y' instead of 'rmp -i' (davidkovach-
  fuentes2027@u.northwestern.edu)
- remove duplicate install inst; open PR (davidkovach-
  fuentes2027@u.northwestern.edu)
- remove duplicate install inst; open PR (davidkovach-
  fuentes2027@u.northwestern.edu)
- README correction; prepare to open PR (davidkovach-
  fuentes2027@u.northwestern.edu)
- fix NAME-VERSION for RPM package (davidkovach-fuentes2027@u.northwestern.edu)
- prepare for PR; remove iteration from pkg name (davidkovach-
  fuentes2027@u.northwestern.edu)
- add comments and credit; update with corrected formula (davidkovach-
  fuentes2027@u.northwestern.edu)
- map secrets to env for workflow (davidkovach-fuentes2027@u.northwestern.edu)
- update workflow to validate tap (davidkovach-fuentes2027@u.northwestern.edu)
- initial fpm packaging (davidkovach-fuentes2027@u.northwestern.edu)
- initial packaging workflow (davidkovach-fuentes2027@u.northwestern.edu)
- Fix container entrypoint dispatch (vagos@lamprou.xyz)
- Rename docker action (vagos@lamprou.xyz)
- feat(packaging): initial brew packaging (#1) (166773733+davidkovach-
  fuentes@users.noreply.github.com)
- clean up PR for merging (davidkovach-fuentes2027@u.northwestern.edu)
- replace fields for transfer (davidkovach-fuentes2027@u.northwestern.edu)
- replace fields for transfer (davidkovach-fuentes2027@u.northwestern.edu)
- minor tweaks to Formula (davidkovach-fuentes2027@u.northwestern.edu)
- delete the old workflow (davidkovach-fuentes2027@u.northwestern.edu)
- more graceful error message (davidkovach-fuentes2027@u.northwestern.edu)
- update workflow release (davidkovach-fuentes2027@u.northwestern.edu)
- fix format and workflow (davidkovach-fuentes2027@u.northwestern.edu)
- linux workflow (davidkovach-fuentes2027@u.northwestern.edu)
- run workflow release (davidkovach-fuentes2027@u.northwestern.edu)
- ci: build homebrew tarball in workflow (davidkovach-
  fuentes2027@u.northwestern.edu)
- initial support for brew/ubuntu/fedora (davidkovach-
  fuentes2027@u.northwestern.edu)
- stream type: fix reference to nonexistent function (github@kapetanak.is)
- regex: fix wrong docstring (github@kapetanak.is)
- use PyPI libdash (github@kapetanak.is)
- docs: imrpove annotations section in the readme (github@kapetanak.is)
- fix: typo in readme (github@kapetanak.is)
- main: exit with 0 on success, 1 on type errors, 2 on system errors
  (github@kapetanak.is)
- wrap error-prone functions with try/except blocks to prevent crashes
  (github@kapetanak.is)
- type db: delete unused functions in extended signatures (github@kapetanak.is)
- test: add 20 integration tests for annotation checker pipeline
  (github@kapetanak.is)
- fix: gate NoEmptyOutput output_override and skip_remaining_checks on
  is_violated (github@kapetanak.is)
- type db: add TODO for @@ lazy directory content implementation
  (github@kapetanak.is)
- fix: add ContainsViolationError for *_contains annotations; use distinct
  formatting (github@kapetanak.is)
- type db: add _substitute_shell_vars as centralized @var lookup; update echo
  to use it (github@kapetanak.is)
- type db: wire StreamTypeTemplate hole resolution in
  resolve_annotation_pattern; fix has_child_of_type to check self
  (github@kapetanak.is)
- test: add tests for {{hole}} syntax in annotations and
  resolve_annotation_pattern function (github@kapetanak.is)
- checker: use resolve_annotation_pattern for all annotation regex resolution
  (github@kapetanak.is)
- resolver: add resolve_annotation_pattern, build_command_env; move _enrich_env
  to resolver; use _parse_transform_expression for ASSUME_OUTPUT
  (github@kapetanak.is)
- test: add tests for colon and arrow inside quoted annotation values
  (github@kapetanak.is)
- resolver: iterate annotations in reverse so last ASSUME_OUTPUT wins
  (github@kapetanak.is)
- parser: remove redundant left==right check in arrow disambiguation
  (github@kapetanak.is)
- checker: remove dead _resolve_input, _check_output_contains, and unused
  imports (github@kapetanak.is)
- checker: add assert handlers for new annotation scheme (input, output,
  input_contains, output_contains) (github@kapetanak.is)
- type db: replace ASSUME with ASSUME_OUTPUT in resolver, add ASSUME_INPUT skip
  in checker, remove dead _match_input_type (github@kapetanak.is)
- type db: inject @var annotations into env with var: prefix for resolver
  consumption (github@kapetanak.is)
- docs: update all references to annotations in the docs, as well as add
  examples in the readme (github@kapetanak.is)
- test(regular_type): add tests for the new user annotation parsing logic
  (github@kapetanak.is)
- refactor(regular_type): refactor the user annotation syntax to make it less
  confusing and more usable (github@kapetanak.is)
- add barebones AGENTS.md (github@kapetanak.is)
- cleanup: remove all leftovers of src/stream and the artifact evaluation
  (github@kapetanak.is)
- cleanup: delete artifact evaluation files and scripts (github@kapetanak.is)
- cleanup: flatten nested test directory (github@kapetanak.is)
- cleanup: delete tests for now-deleted src/stream (github@kapetanak.is)
- add __init__ module to rt (github@kapetanak.is)
- cleanup: delete src/stream (old codebase) (github@kapetanak.is)
- scripts: make installation and docker-run scripts posix (github@kapetanak.is)
- scripts: turn python script (stub generator) into shell script for
  convenience (github@kapetanak.is)
- scripts: remove unused scripts (github@kapetanak.is)
- type db: fix cut's resolver, which was missing a function definition
  (github@kapetanak.is)
- rti: use rt imports and apis instead of stream (github@kapetanak.is)
- shell parser: rename function that parses invocations (github@kapetanak.is)
- type db: add type alias getter and setter (regex syntactic sugar)
  (github@kapetanak.is)
- fix: change default output of unknown command to `.*` (it accidentally was
  `{{input}}`) (github@kapetanak.is)
- docs: add docstrings to explain some not-so-obvious code blocks
  (github@kapetanak.is)
- docs: massively improve the readme file (github@kapetanak.is)
- docs: add document with contribution instructions and guide
  (github@kapetanak.is)
- meta: update `uv run rt` to use rt instead of stream (github@kapetanak.is)
- rename repo reference (github@kapetanak.is)
- scripts: add installation script for curl-to-sh installation
  (github@kapetanak.is)
- scripts: add script to run rt through docker by automatically mounting path
  arguments to it (github@kapetanak.is)
- docs: add a document describing how command signatures can be created
  (github@kapetanak.is)
- docs: add a document describing the architecture of the system
  (github@kapetanak.is)
- Update publish-docker action to only work when triggered manually
  (github@kapetanak.is)
- human readable types added (rsrikanth@ucsd.edu)
- test(transducer): add inline todos in test module highlighting what is
  missing from it (github@kapetanak.is)
- refactor(transducer): remove unused filter_transducer, cut_field_transducer,
  translate_to_line_delimited_FST (github@kapetanak.is)
- test(transducer): add forward tests for cut_char and 4 regex-based transducer
  builders (github@kapetanak.is)
- test(transducer): add hypothesis tests for inverse round-trip and soundness
  properties (github@kapetanak.is)
- test(transducer): widen hypothesis alphabets and strengthen
  compression/deletion property checks (github@kapetanak.is)
- refactor(tests): declass and merge inverse transducer tests into
  test_transducer.py (github@kapetanak.is)
- docs(tests): add docstrings to forward transducer property tests
  (github@kapetanak.is)
- no_input_reason field added (rsrikanth@ucsd.edu)
- Revise command examples and output in README
  (156384326+Ridzz23@users.noreply.github.com)
- refactor(stream -> rt): add main module for running the system
  (github@kapetanak.is)
- refactor(stream -> rt): add module for formatting error output
  (github@kapetanak.is)
- refactor(stream -> rt): add module for converting automata to regular
  expressions (github@kapetanak.is)
- refactor(stream -> rt): add type checking implementation in checker.py
  (github@kapetanak.is)
- refactor(stream -> rt): add heuristics.py, with an abstract class for
  defining heuristics easily and independently of yaml files
  (github@kapetanak.is)
- refactor(stream -> rt): add all extended command types (python classes)
  translated to subclass RuleResolver (github@kapetanak.is)
- refactor(stream -> rt): add all basic command types (yaml files) translated
  to the new format (github@kapetanak.is)
- refactor(stream -> rt): add get_type/register_type functions for getting and
  setting types (register_type is wip) (github@kapetanak.is)
- refactor(stream -> rt): add description of the language used to define types
  in yaml (github@kapetanak.is)
- refactor(stream -> rt): add some tests for the resolver (github@kapetanak.is)
- refactor(stream -> rt): add regular type resolver interface and
  implementation Defines the interface for reading type annotations (yaml files
  or python functions) and returning command types The implementation,
  RuleResolver works with the yaml format (github@kapetanak.is)
- refactor(stream -> rt): fix infinite recursion bug in stream type constructor
  (github@kapetanak.is)
- refactor(stream -> rt): add annotations module, defining annotations
  describing command behavior as well as environment contents
  (github@kapetanak.is)
- refactor(stream -> rt): add command type module (github@kapetanak.is)
- refactor(stream -> rt): add stream tranformations module that are used to
  describe how a command type transforms its input (github@kapetanak.is)
- refactor(stream -> rt): add extended regular operations on stream types
  (stream's regular_operator module) (github@kapetanak.is)
- refactor(stream -> rt): add utils module, for helper functions that do not
  fit in any other module (github@kapetanak.is)
- refactor(stream -> rt): add stream_type module, a refactored version of the
  regular_type module * Two classes: StreamType and StreamTypeTemplate, for
  when regexes have holes in them (github@kapetanak.is)
- refactor(stream -> rt): add refactored shell parsing module * Defines a
  Pipeline data type * Its API is one function: parse_pipelines()
  (github@kapetanak.is)
- refactor(stream -> rt): add transducer tests (github@kapetanak.is)
- refactor(stream -> rt): add transducer module, which is stream's FST with
  slightly different names (github@kapetanak.is)
- refactor(stream -> rt): add constants module for global constants
  (github@kapetanak.is)
- refactor(stream -> rt): add tests for the regex module (github@kapetanak.is)
- refactor(stream -> rt): add __init__ to regex module which exports the public
  api if the module (github@kapetanak.is)
- refactor(stream -> rt): add regex parser * Uses Dialect enum instead of str
  mode (github@kapetanak.is)
- refactor(stream -> rt): add regex ast module (github@kapetanak.is)
- refactor(stream -> rt): add java_api module to new rt package
  (github@kapetanak.is)
- Add publish-docker-image workflow (gh action) (github@kapetanak.is)
- -i shows polymorphic and instantiated types (github@kapetanak.is)
- Fix broken build on newer uv versions? (LukasALazarek@gmail.com)
- updated description of rti (156384326+Ridzz23@users.noreply.github.com)
- Added new examples showing rti with and without -i
  (156384326+Ridzz23@users.noreply.github.com)
- Renamed rtr to rti and limited type instantiation to -i (rsrikanth@ucsd.edu)
- restore functionality checking script (zekai.li.0028@gmail.com)
- refactor(regex_parser): move three regular type transformation functions to
  regular_type module (github@kapetanak.is)
- move eval scripts into the scripts directory in src/stream
  (github@kapetanak.is)
- fix(stream): restore accidentally removed escaped-delimiter handling in
  sed.py (github@kapetanak.is)
- refactor(stream): extract char-set utilities into char_set_utils.py
  (github@kapetanak.is)
- refactor(stream): remove dead field_select, refine_log, and automaton_to_ast
  (github@kapetanak.is)
- refactor(stream): consolidate regex utilities into regex_parser.py
  (github@kapetanak.is)
- refactor(stream): remove dead Z3 and regex utility code (github@kapetanak.is)
- refactor(stream): resolve regex utility naming collision and deduplicate
  (github@kapetanak.is)
- refactor(stream): remove dead backward_func, CommandTypeResult, and
  InferenceResult (github@kapetanak.is)
- refactor(stream): extract helpers from regular_type into focused modules
  (github@kapetanak.is)
- Remove whole-stream representation of RegularType and update codebase
  accordingly (github@kapetanak.is)
- Refactor existing tests to use conftest fixtures and clean up
  (github@kapetanak.is)
- Add conftest.py and new test files (github@kapetanak.is)
- Move existing tests from src/stream/unit_tests/ to tests/stream/
  (github@kapetanak.is)
- Add hypothesis dependency and Java type stubs (github@kapetanak.is)
- Add stream.java_api to centralize JVM initialization (github@kapetanak.is)
- fix regex parser (zekai.li.0028@gmail.com)
- fix sort (zekai.li.0028@gmail.com)
- command type config (zekai.li.0028@gmail.com)
- update input type (zekai.li.0028@gmail.com)
- merge (zekai.li.0028@gmail.com)
- regex (zekai.li.0028@gmail.com)
- Fix sort negative constraint (LukasALazarek@gmail.com)
- shrink (zekai.li.0028@gmail.com)
- refactor sed and awk (zekai.li.0028@gmail.com)
- fix regular operators (zekai.li.0028@gmail.com)
- rtr bugfix: default type is .* and not empty (github@kapetanak.is)
- Add rtr, a tool that resolves command invocation types, as a second package *
  First iteration of the tool, still plenty to do (github@kapetanak.is)
- Make devcontainer context-free Previous devcontainer relied on an external
  workspace file and failed to build if it didn't exist (github@kapetanak.is)
- Improve CLI further (github@kapetanak.is)
- perf (zekai.li.0028@gmail.com)
- Update README with installation instructions (github@kapetanak.is)
- Update dockerfile to expose a dev target and a sys target
  (github@kapetanak.is)
- Move pyproject.toml to the root of the project and add uv support
  (github@kapetanak.is)
- Add a main module exposing a CLI interface (github@kapetanak.is)
- Fix invalid escapes (github@kapetanak.is)
- clean up (zekai.li.0028@gmail.com)
- remove warning (zekai.li.0028@gmail.com)
- update command support (zekai.li.0028@gmail.com)
- fix grep (zekai.li.0028@gmail.com)
- update instructions (zekai.li.0028@gmail.com)
- add entry point (zekai.li.0028@gmail.com)
- cleanup (zekai.li.0028@gmail.com)
- cleanup (zekai.li.0028@gmail.com)
- update benchmark (zekai.li.0028@gmail.com)
- Adopt snapshot update (zekai.li.0028@gmail.com)
- update scripts (zekai.li.0028@gmail.com)
- update scripts (zekai.li.0028@gmail.com)
- update instruction (zekai.li.0028@gmail.com)
- update (zekai.li.0028@gmail.com)
- update (zekai.li.0028@gmail.com)
- update (zekai.li.0028@gmail.com)
- tables (zekai.li.0028@gmail.com)
- refactor (zekai.li.0028@gmail.com)
- update baseline (zekai.li.0028@gmail.com)
- add typedb (zekai.li.0028@gmail.com)
- update readme (zekai.li.0028@gmail.com)
- update (zekai.li.0028@gmail.com)
- fix (zekai.li.0028@gmail.com)
- fix bugs in heuristics (zekai.li.0028@gmail.com)
- update scripts (zekai.li.0028@gmail.com)
- update scripts (zekai.li.0028@gmail.com)
- update (zekai.li.0028@gmail.com)
- update (zekai.li.0028@gmail.com)
- update (zekai.li.0028@gmail.com)
- update (zekai.li.0028@gmail.com)
- update README (zekai.li.0028@gmail.com)
- update README (zekai.li.0028@gmail.com)
- update README (zekai.li.0028@gmail.com)
- fix fmt type (zekai.li.0028@gmail.com)
- fix: parser does not use correct extra pash annots (zekai.li.0028@gmail.com)
- remove logs (zekai.li.0028@gmail.com)
- update dockerfile (zekai.li.0028@gmail.com)
- Added unlisted dependency to README
  (107506602+Zarquon0@users.noreply.github.com)
- remove lagency Dockerfile (zekai.li.0028@gmail.com)
- remove useless code (zekai.li.0028@gmail.com)
- refactor: use new timing util (zekai.li.0028@gmail.com)
- add timing data (zekai.li.0028@gmail.com)
- add baseline label (zekai.li.0028@gmail.com)
- add awk subset support (zekai.li.0028@gmail.com)
- fix awk parser (zekai.li.0028@gmail.com)
- new awk parser (zekai.li.0028@gmail.com)
- add baseline ground truth (zekai.li.0028@gmail.com)
- correct koala benchmark usage (zekai.li.0028@gmail.com)
- create Rt++ benchmark (zekai.li.0028@gmail.com)
- add koala benchmark (zekai.li.0028@gmail.com)
- add koala benchmark (zekai.li.0028@gmail.com)
- update transducer product computation (zekai.li.0028@gmail.com)
- Pass over github analysis (LukasALazarek@gmail.com)
- update transducer product computation (zekai.li.0028@gmail.com)
- update transducer product computation (zekai.li.0028@gmail.com)
- update transducer product computation (zekai.li.0028@gmail.com)
- Fixed type checking for type_checker.py (except for all the "logging record
  possibly None" errors) (george.kapetanakis.gk@gmail.com)
- refactor: remove dependency z3 (zekai.li.0028@gmail.com)
- update dataflow analysis result (zekai.li.0028@gmail.com)
- update dataflow analysis result (zekai.li.0028@gmail.com)
- update dataflow analysis result (zekai.li.0028@gmail.com)
- update dataflow analysis result (zekai.li.0028@gmail.com)
- update dataflow analysis result (zekai.li.0028@gmail.com)
- refactor (zekai.li.0028@gmail.com)
- add interesting pipelines (zekai.li.0028@gmail.com)
- add interesting pipelines (zekai.li.0028@gmail.com)
- refactor (zekai.li.0028@gmail.com)
- upload interesting pipelines (zekai.li.0028@gmail.com)
- upload interesting pipelines (zekai.li.0028@gmail.com)
- update interesting pipelines (zekai.li.0028@gmail.com)
- update implementation.md (zekai.li.0028@gmail.com)
- add interesting pipelines (zekai.li.0028@gmail.com)
- update transducer product computation (zekai.li.0028@gmail.com)
- update transducers (zekai.li.0028@gmail.com)
- update implementation.md (zekai.li.0028@gmail.com)
- update implementation.md (zekai.li.0028@gmail.com)
- update implementation.md (zekai.li.0028@gmail.com)
- update implementation.md (zekai.li.0028@gmail.com)
- update implementation.md (zekai.li.0028@gmail.com)
- update implementation.md (zekai.li.0028@gmail.com)
- update implementation.md (zekai.li.0028@gmail.com)
- update implementation.md (zekai.li.0028@gmail.com)
- add implementation summary of cut (zekai.li.0028@gmail.com)
- update command pattern analysis (zekai.li.0028@gmail.com)
- add logger for command (zekai.li.0028@gmail.com)
- Add top level script for quickly running system, note in readme
  (LukasALazarek@gmail.com)
- add logs (zekai.li.0028@gmail.com)
- refactor: checking result (zekai.li.0028@gmail.com)
- refactor (zekai.li.0028@gmail.com)
- refactor (zekai.li.0028@gmail.com)
- refactor (zekai.li.0028@gmail.com)
- fix (zekai.li.0028@gmail.com)
- fix (zekai.li.0028@gmail.com)
- fix (zekai.li.0028@gmail.com)
- fix (zekai.li.0028@gmail.com)
- fix (zekai.li.0028@gmail.com)
- fix (zekai.li.0028@gmail.com)
- log refactor (zekai.li.0028@gmail.com)
- update logs (zekai.li.0028@gmail.com)
- add logs (zekai.li.0028@gmail.com)
- refactor (zekai.li.0028@gmail.com)
- update evaluation notes (zekai.li.0028@gmail.com)
- remove redundant benchmark (zekai.li.0028@gmail.com)
- remove Shseer benchmark (zekai.li.0028@gmail.com)
- fix timing bug (zekai.li.0028@gmail.com)
- Plot tweaks (LukasALazarek@gmail.com)
- update benchmark (zekai.li.0028@gmail.com)
- sync annotations (zekai.li.0028@gmail.com)
- update performance.py (zekai.li.0028@gmail.com)
- update the benchmark (zekai.li.0028@gmail.com)
- Update full_eval for performance update (LukasALazarek@gmail.com)
- Performance and debug script fixes (LukasALazarek@gmail.com)
- Fix bug in overview summary generation (LukasALazarek@gmail.com)
- update the baseline (zekai.li.0028@gmail.com)
- update the plots (zekai.li.0028@gmail.com)
- Plot and summary updates (LukasALazarek@gmail.com)
- update the results (final) (zekai.li.0028@gmail.com)
- update the results (final) (zekai.li.0028@gmail.com)
- change bad label to bad heuristics (zekai.li.0028@gmail.com)
- update benchmark (zekai.li.0028@gmail.com)
- update benchmark (zekai.li.0028@gmail.com)
- update benchmark (zekai.li.0028@gmail.com)
- update benchmark (zekai.li.0028@gmail.com)
- update github commits and fix annotations (zekai.li.0028@gmail.com)
- update github commits and fix annotations (zekai.li.0028@gmail.com)
- update github commits collection (zekai.li.0028@gmail.com)
- update github commits collection (zekai.li.0028@gmail.com)
- add github commits collection (zekai.li.0028@gmail.com)
- Pushed 12 new annotated benchmarks (george.kapetanakis.gk@gmail.com)
- add tainted tag (zekai.li.0028@gmail.com)
- 7 more annotated commits (george.kapetanakis.gk@gmail.com)
- More annotations (george.kapetanakis.gk@gmail.com)
- Make debug script more usable (LukasALazarek@gmail.com)
- Added 1 annotation (george.kapetanakis.gk@gmail.com)
- Multiple annotation changes (george.kapetanakis.gk@gmail.com)
- Added several annotations (and fixed some old ones)
  (george.kapetanakis.gk@gmail.com)
- Fixed two annotations (george.kapetanakis.gk@gmail.com)
- Modified 2 annotations (george.kapetanakis.gk@gmail.com)
- Update acme.sh_acme_5a44e63.sh
  (115373824+gkapetanakis@users.noreply.github.com)
- Modified some annotations (george.kapetanakis.gk@gmail.com)
- Annotated more GitHub (pre-)commits (george.kapetanakis.gk@gmail.com)
- update evaluation (zekai.li.0028@gmail.com)
- More fixes and updates to full-eval script after merge
  (LukasALazarek@gmail.com)
- Fix some lingering updates to move from old config, add some eval flags
  (LukasALazarek@gmail.com)
- Make system naming and coloring more consistent across plots
  (LukasALazarek@gmail.com)
- refactor and fix bugs (zekai.li.0028@gmail.com)
- plots: separate the correct and buggy sets in accuracy chart
  (LukasALazarek@gmail.com)
- More visual tweaks (LukasALazarek@gmail.com)
- Tweak plot visuals (LukasALazarek@gmail.com)
- Fix plotting names (LukasALazarek@gmail.com)
- Full eval script with plots (LukasALazarek@gmail.com)
- add config file (zekai.li.0028@gmail.com)
- First step to automated eval: centralize benchmark info in config
  (LukasALazarek@gmail.com)
- refactor: json to yaml (zekai.li.0028@gmail.com)
- update evaluation notes (zekai.li.0028@gmail.com)
- add github/stackoverflow collection (zekai.li.0028@gmail.com)
- Dockerfile: add todo to install evaluation deps (LukasALazarek@gmail.com)
- eval-summary: add bug detection csv generation (LukasALazarek@gmail.com)
- update translate-match (zekai.li.0028@gmail.com)
- minor (zekai.li.0028@gmail.com)
- deleted a wrongly uploaded script (george.kapetanakis.gk@gmail.com)
- added another script which i forgot about (george.kapetanakis.gk@gmail.com)
- added script used in SO benchmark collection
  (george.kapetanakis.gk@gmail.com)
- minor (zekai.li.0028@gmail.com)
- add ps and patial support for awk (zekai.li.0028@gmail.com)
- Integrate baseline results into evaluation results overview
  (LukasALazarek@gmail.com)
- fix evaluation script (zekai.li.0028@gmail.com)
- fix bugs (zekai.li.0028@gmail.com)
- annotation complement/correction (zekai.li.0028@gmail.com)
- annotation complement/correction (zekai.li.0028@gmail.com)
- annotation complement (zekai.li.0028@gmail.com)
- annotation correction (zekai.li.0028@gmail.com)
- fix sed bug (zekai.li.0028@gmail.com)
- fix delimiter bug (zekai.li.0028@gmail.com)
- add var and file annotation support for grep and cut
  (zekai.li.0028@gmail.com)
- Pushed some more annotations (output_new/pre_commit/advanced_Scripts_*)
  (george.kapetanakis.gk@gmail.com)
- add var and file annotation support (zekai.li.0028@gmail.com)
- fix group capturing (not finished) (zekai.li.0028@gmail.com)
- feat: add support for group capturing (not finished)
  (zekai.li.0028@gmail.com)
- feat: add FST for sed 's/^regex/str/' (zekai.li.0028@gmail.com)
- feat: add FST for sed 's/regex/str/' (zekai.li.0028@gmail.com)
- fix rev (zekai.li.0028@gmail.com)
- add support for sort -k (zekai.li.0028@gmail.com)
- Going over SO and GH (nvm) bug annotations (LukasALazarek@gmail.com)
- fix bugs in transducer (zekai.li.0028@gmail.com)
- added some (probably correct) annotations to git commits
  (george.kapetanakis.gk@gmail.com)
- commented some mistakenly uncommented code (george.kapetanakis.gk@gmail.com)
- fix a bug in transducer (zekai.li.0028@gmail.com)
- add support for sed (zekai.li.0028@gmail.com)
- Bugfix and added option in benchmark-fetching script
  (george.kapetanakis.gk@gmail.com)
- implement first replacement transducer (zekai.li.0028@gmail.com)
- implement global replacement transducer (zekai.li.0028@gmail.com)
- nevermind (removed 2 benchmarks) (george.kapetanakis.gk@gmail.com)
- Added some more benchmarks (george.kapetanakis.gk@gmail.com)
- Added a script that can be used to quickly find benchmarks with a given tag,
  along with a list of the tags used so far (george.kapetanakis.gk@gmail.com)
- Added annotated (and tagged; see next commit) benchmarks from stackoverflow.
  Benchmarks in the 'unclear/' folder are ambiguous or I could not annotate.
  (george.kapetanakis.gk@gmail.com)
- added 5 annotated stack overflow benchmarks (george.kapetanakis.gk@gmail.com)
- update github commits benchmark; fix a bug in FST; add rev
  (zekai.li.0028@gmail.com)
- fix a bug for tr -s (zekai.li.0028@gmail.com)
- update README (zekai.li.0028@gmail.com)
- update tr and cut FSTs; add new github commit collection
  (zekai.li.0028@gmail.com)
- Add the SO questions from Anirudh (LukasALazarek@gmail.com)
- Add by-benchmark-set results summary csv generation (LukasALazarek@gmail.com)
- refactor: regular type with automaton (zekai.li.0028@gmail.com)
- add hole support in regex parser (zekai.li.0028@gmail.com)
- update Dockerfile (zekai.li.0028@gmail.com)
- add support for empty transition (zekai.li.0028@gmail.com)
- minor (zekai.li.0028@gmail.com)
- minor (zekai.li.0028@gmail.com)
- add FST for one to many mapping (zekai.li.0028@gmail.com)
- add FST; replace z3 with dk.brics.automaton subset checking
  (zekai.li.0028@gmail.com)
- update README and Dockerfile (zekai.li.0028@gmail.com)
- update full benchmarks (zekai.li.0028@gmail.com)
- update commit filter and regex parser (zekai.li.0028@gmail.com)
- update evaluation statistics (zekai.li.0028@gmail.com)
- update README (zekai.li.0028@gmail.com)
- fix regex parsing in grep and sed (zekai.li.0028@gmail.com)
- add add parallel processing to evaluation script (zekai.li.0028@gmail.com)
- refactor: new regex parser (zekai.li.0028@gmail.com)
- add regex parser to subsumption checking (zekai.li.0028@gmail.com)
- add more escape char support in regex parser (zekai.li.0028@gmail.com)
- add regex parser (zekai.li.0028@gmail.com)
- add tag mapping (zekai.li.0028@gmail.com)
- update evaluation notes (zekai.li.0028@gmail.com)
- add stage checking timeout option (zekai.li.0028@gmail.com)
- excute z3 in subprocess (zekai.li.0028@gmail.com)
- some support for \n (zekai.li.0028@gmail.com)
- update evaluation results (zekai.li.0028@gmail.com)
- add command line argparser in evaluation script (zekai.li.0028@gmail.com)
- include github bugs in benchmarks (zekai.li.0028@gmail.com)
- add github bugs (zekai.li.0028@gmail.com)
- add full benchmark spreadsheets (zekai.li.0028@gmail.com)
- add results without annotations (zekai.li.0028@gmail.com)
- double check the benchmarks and the results (zekai.li.0028@gmail.com)
- fix pash annotation parser's bug (zekai.li.0028@gmail.com)
- fix pash annotation parser's bug (zekai.li.0028@gmail.com)
- fix statistical error of crahsed pipelines (zekai.li.0028@gmail.com)
- show pipeline contents when pash annotation error occurs
  (zekai.li.0028@gmail.com)
- add support for grep -n, yes, paste, md5sum; make the pash annotation error
  detector stricter (zekai.li.0028@gmail.com)
- update evaluation results (zekai.li.0028@gmail.com)
- update evaluation_notes (zekai.li.0028@gmail.com)
- update evaluation notes (zekai.li.0028@gmail.com)
- skip the pash annotations error when handling uninteresting commands
  (zekai.li.0028@gmail.com)
- Annotate remaining un-annoted evaluation pipelines (LukasALazarek@gmail.com)
- Add finer grained timing info to log (LukasALazarek@gmail.com)
- fix tr (zekai.li.0028@gmail.com)
- add input/output annotations (zekai.li.0028@gmail.com)
- fix preprocessing (zekai.li.0028@gmail.com)
- add pash exception, fix cut, sed, optimize preprocessing of regular type
  (zekai.li.0028@gmail.com)
- fix tr (zekai.li.0028@gmail.com)
- fix tr (zekai.li.0028@gmail.com)
- fix evaluation script (zekai.li.0028@gmail.com)
- rename enable_rule_empty_output -> enable_rule_no_empty_output
  (zekai.li.0028@gmail.com)
- fix heuristics for grep cut tr sed (zekai.li.0028@gmail.com)
- add heuristics (zekai.li.0028@gmail.com)
- fix crash caused by grep (zekai.li.0028@gmail.com)
- fix crash caused by matching commands (zekai.li.0028@gmail.com)
- fix: handle ^$ in regex; feat: add rule to ensure no ignored input
  (zekai.li.0028@gmail.com)
- fix escape characters related issue (zekai.li.0028@gmail.com)
- rafactor: {}&{} to ()&() (zekai.li.0028@gmail.com)
- update evaluation notes (zekai.li.0028@gmail.com)
- add llm generated buggy pipelines to full evaluation
  (zekai.li.0028@gmail.com)
- label the llm injected pipelines (zekai.li.0028@gmail.com)
- add timeout for subsumption checking (zekai.li.0028@gmail.com)
- refactor temp file process (zekai.li.0028@gmail.com)
- fix parser bug, label half of llm generated pipes (zekai.li.0028@gmail.com)
- fix cut, grep -e (zekai.li.0028@gmail.com)
- fix cut input type bug (zekai.li.0028@gmail.com)
- rename methods in CheckingResult (zekai.li.0028@gmail.com)
- add rule for empty output (zekai.li.0028@gmail.com)
- add user annotation (zekai.li.0028@gmail.com)
- add buggy pipelines injected by llm (zekai.li.0028@gmail.com)
- add buggy pipelines injected by llm (zekai.li.0028@gmail.com)
- fix evaluation_summary.py and clean pash_benchmarks (zekai.li.0028@gmail.com)
- add report (zekai.li.0028@gmail.com)
- fixed bugs in type checker (zekai.li.0028@gmail.com)
- improve efficiency of subsumption checking and rename status to illtyped
  (zekai.li.0028@gmail.com)
- Fix some csv shenanigans in table generation (LukasALazarek@gmail.com)
- fix bugs in parser (zekai.li.0028@gmail.com)
- tweat llm-injection (not finished) (zekai.li.0028@gmail.com)
- Add curated set of mutants (LukasALazarek@gmail.com)
- Add mutant curation and tabulation scripts, and notes about mutants
  (LukasALazarek@gmail.com)
- add unix50 mutation labels (zekai.li.0028@gmail.com)
- fix bugs in parser and refactor parser (zekai.li.0028@gmail.com)
- add ignore item (zekai.li.0028@gmail.com)
- Add mutant generation script (LukasALazarek@gmail.com)
- Add script to generate results table from json (LukasALazarek@gmail.com)
- traverse qargs (anirudh.narsipur@gmail.com)
- traverse more nodes for pipelines (anirudh.narsipur@gmail.com)
- add results for Shseer evaluations (zekai.li.0028@gmail.com)
- fix time cost measurement in evaluation script (zekai.li.0028@gmail.com)
- make notes for unix 50 and intercode (zekai.li.0028@gmail.com)
- adjust order of fields in evaluation_results.json (zekai.li.0028@gmail.com)
- refactor: type_checker, evaluation script (zekai.li.0028@gmail.com)
- refactor extract_pipe_nodes_from_file (zekai.li.0028@gmail.com)
- refactor evaluation script; evaluation script is stil broken
  (zekai.li.0028@gmail.com)
- fix unit tests (zekai.li.0028@gmail.com)
- add csv for categories of commits (zekai.li.0028@gmail.com)
- add notes for github commits (zekai.li.0028@gmail.com)
- feat: clean Shseer benchmark; add CheckingResult class; break evaluation
  script and unit tests now (zekai.li.0028@gmail.com)
- Add some pipeline mutators (LukasALazarek@gmail.com)
- add some notes in github filtered commits (zekai.li.0028@gmail.com)
- feat: add support for script parsing (zekai.li.0028@gmail.com)
- Evaluation updates: add place for notes, hook into results, add summary table
  (LukasALazarek@gmail.com)
- feat: support checking pipeline in the assignment (zekai.li.0028@gmail.com)
- accelerate subtyping checking (zekai.li.0028@gmail.com)
- feat: time out termination in evaluation script (zekai.li.0028@gmail.com)
- update unit tests for subtyping (zekai.li.0028@gmail.com)
- fix error in reading shseer benchmarks (zekai.li.0028@gmail.com)
- add shseer benchmarks (zekai.li.0028@gmail.com)
- update evaluation script (zekai.li.0028@gmail.com)
- update annotation format (zekai.li.0028@gmail.com)
- add user annotation support (zekai.li.0028@gmail.com)
- update summary of github_repos_commits (zekai.li.0028@gmail.com)
- add support to cut -d -f (zekai.li.0028@gmail.com)
- add llm injection (zekai.li.0028@gmail.com)
- add correct pipelines as full benchmark suites (zekai.li.0028@gmail.com)
- update the evaluation script (zekai.li.0028@gmail.com)
- update the script (zekai.li.0028@gmail.com)
- feat: make repos dir if doesnot exist (zekai.li.0028@gmail.com)
- feat: add llm filter to benchmark autofetcher (zekai.li.0028@gmail.com)
- feat: benchmark autofetcher (zekai.li.0028@gmail.com)
- modify an evaluation example fix a small error (zekai.li.0028@gmail.com)
- incomplete support for sed (zekai.li.0028@gmail.com)
- add incomplete support for xargs_stat (zekai.li.0028@gmail.com)
- refactor type inference (zekai.li.0028@gmail.com)
- update dockerfile (zekai.li.0028@gmail.com)
- feat: incomplete echo ls xargs stat rm support (zekai.li.0028@gmail.com)
- update evaluation script (zekai.li.0028@gmail.com)
- update evaluation script (zekai.li.0028@gmail.com)
- feat: xargs (zekai.li.0028@gmail.com)
- feat: partial support for tr (zekai.li.0028@gmail.com)
- feat: add negation intersection translations, add supports for grep -v and
  grep -w (zekai.li.0028@gmail.com)
- fix rule resolving (infiniteloop654@gmail.com)
- refactor rule resolving (infiniteloop654@gmail.com)
- remove requirements.txt and update pyproject.toml (infiniteloop654@gmail.com)
- add evaluation script (infiniteloop654@gmail.com)
- replace print with logging (infiniteloop654@gmail.com)
- update signature of grep and sort (infiniteloop654@gmail.com)
- update unit tests (infiniteloop654@gmail.com)
- modify the format of signatures (infiniteloop654@gmail.com)
- update some comments (infiniteloop654@gmail.com)
- feat: add parametric polymorphism (infiniteloop654@gmail.com)
- feat: Completed prototype implementation (infiniteloop654@gmail.com)
- adapt to parse_shell_to_asts (infiniteloop654@gmail.com)
- add gitignore (infiniteloop654@gmail.com)
- prototype init (infiniteloop654@gmail.com)

* Thu Aug 27 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> 0.1.3-1
- test workflow (davidkovach-fuentes2027@u.northwestern.edu)
- prepare for PR (davidkovach-fuentes2027@u.northwestern.edu)
- test for webhook rebuild (davidkovach-fuentes2027@u.northwestern.edu)

