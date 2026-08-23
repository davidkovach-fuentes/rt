Name: atlas-rt
Version: 0.1.2
Release: 1%{?dist}
License: GPLv3
Summary: An overlay type system for shell pipelines
Url: https://github.com/davidkovach-fuentes/rt

# Created by .copr/Makefile via `git archive` of the full repo (includes scripts/).
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

Requires: moby-engine

%description
Rt catches data incompatibilities in shell pipelines before they run.
Give it a shell program and it tells you when one command produces data the next command can't consume
-- with a concrete counterexample showing exactly what breaks.

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
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
* Sun Aug 23 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> 0.1.2-1
- 

* Sun Aug 23 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> 0.1.1-1
- 

* Sun Aug 23 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu>
- 

* Sun Aug 23 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> 0.1.1-1
- 

* Sun Aug 23 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> 0.1.5-1
- Fix Copr Fedora build with make_srpm and full-repo archive (davidkovach-
  fuentes2027@u.northwestern.edu)

* Sun Aug 23 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> 0.1.4-2
- fix Version/Release; full-repo Source0 for Copr make_srpm

* Sun Aug 23 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> 0.1.4-1
- Copr packaging for Docker wrapper (scripts/run-in-container.sh)
