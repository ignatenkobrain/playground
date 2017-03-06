# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate serde_json

Name:           rust-%{crate}
Version:        0.9.9
Release:        1%{?dist}
Summary:        JSON serialization file format

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/serde_json
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo
# [dependencies]
BuildRequires:  (crate(dtoa) >= 0.4.0 with crate(dtoa) < 0.5.0)
BuildRequires:  (crate(itoa) >= 0.3.0 with crate(itoa) < 0.4.0)
BuildRequires:  (crate(linked-hash-map) >= 0.4.1 with crate(linked-hash-map) < 0.5.0)
BuildRequires:  (crate(num-traits) >= 0.1.32 with crate(num-traits) < 0.2.0)
BuildRequires:  (crate(serde) >= 0.9.11 with crate(serde) < 0.10.0)
%if %{with check}
# [dev-dependencies]
BuildRequires:  (crate(serde_derive) >= 0.9.0 with crate(serde_derive) < 0.10.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
A JSON serialization file format.

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
* Mon Mar 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.9-1
- Update to 0.9.9

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.8-1
- Initial package
