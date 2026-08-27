Name: atlas-rt
Version: 0.1.3
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
* Thu Aug 27 2026 davidkovach-fuentes <davidkovach-fuentes2027@u.northwestern.edu> 0.1.3-1
- test workflow (davidkovach-fuentes2027@u.northwestern.edu)
- prepare for PR (davidkovach-fuentes2027@u.northwestern.edu)
- test for webhook rebuild (davidkovach-fuentes2027@u.northwestern.edu)

