# Generated by rust2rpm
# extprim -> extprim_literals(dev) -> extprim_literals_macros -> extprim
%bcond_with check
%global debug_package %{nil}

%global crate extprim

Name:           rust-%{crate}
Version:        1.3.0
Release:        1%{?dist}
Summary:        Extra primitive types (u128, i128)

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/extprim
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(num-traits) >= 0.1.0 with crate(num-traits) < 0.2.0)
BuildRequires:  (crate(rand) >= 0.3.0 with crate(rand) < 0.4.0)
# [build-dependencies]
BuildRequires:  (crate(rustc_version) >= 0.2.0 with crate(rustc_version) < 0.3.0)
%if %{with check}
# [dev-dependencies]
BuildRequires:  (crate(extprim_literals) >= 2.0.0 with crate(extprim_literals) < 3.0.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Extra primitive types (u128, i128).

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
%license LICENSE-MIT.txt LICENSE-APACHE.txt
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Mon Jul 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.2-1
- Initial package
