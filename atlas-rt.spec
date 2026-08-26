Name: atlas-rt
Version: v0.1.1
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
* Wed Aug 26 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> v0.1.1-1
- revert to webhooks and place spec in root (davidkovach-
  fuentes2027@u.northwestern.edu)

* Wed Aug 26 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> 0.1.1-1
- 

* Wed Aug 26 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> 0.1.0-1
- Switch to root-level tito packaging for Copr webhooks
