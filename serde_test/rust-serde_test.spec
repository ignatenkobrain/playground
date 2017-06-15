# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate serde_test

Name:           rust-%{crate}
Version:        1.0.8
Release:        1%{?dist}
Summary:        Token De/Serializer for testing De/Serialize implementations

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/serde_test
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(serde) >= 1.0.0 with crate(serde) < 2.0.0)
%if %{with check}
# [dev-dependencies]
BuildRequires:  ((crate(serde) >= 1.0.0 with crate(serde) < 2.0.0) with crate(serde/rc))
BuildRequires:  (crate(serde_derive) >= 1.0.0 with crate(serde_derive) < 2.0.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Token De/Serializer for testing De/Serialize implementations.

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

%changelog
* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.12-2
- Port to use rust-packaging

* Thu Mar 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.12-1
- Update to 0.9.12

* Mon Mar 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.11-1
- Update to 0.9.11

* Wed Mar 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.10-1
- Update to 0.9.10

* Sat Feb 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.9-1
- Initial package
