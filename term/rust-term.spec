# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate term

Name:           rust-%{crate}
Version:        0.4.6
Release:        2%{?dist}
Summary:        Terminal formatting library

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/term
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * No windows
Patch0:         term-0.4.6-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
A terminal formatting library.

This package contains library source intended for building other packages
which use %{crate} from crates.io.

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/
%exclude %{cargo_registry}/%{crate}-%{version}/{appveyor.yml,scripts}

%changelog
* Sat Sep 23 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.6-2
- Exclude unneeded files

* Sun Jun 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.6-1
- Update to 0.4.6

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.5-2
- Port to use rust-packaging

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.5-1
- Initial package

