# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate num-bigint

Name:           rust-%{crate}
Version:        0.1.39
Release:        1%{?dist}
Summary:        Big integer implementation for Rust

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/num-bigint
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * No paths
Patch0:         num-bigint-0.1.39-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(num-integer) >= 0.1.32 with crate(num-integer) < 0.2.0)
BuildRequires:  (crate(num-traits) >= 0.1.32 with crate(num-traits) < 0.2.0)
BuildRequires:  (crate(rand) >= 0.3.14 with crate(rand) < 0.4.0)
BuildRequires:  (crate(rustc-serialize) >= 0.3.19 with crate(rustc-serialize) < 0.4.0)
BuildRequires:  (crate(serde) >= 0.7.0 with crate(serde) < 0.9.0)
%if %{with check}
# [dev-dependencies]
BuildRequires:  (crate(rand) >= 0.3.14 with crate(rand) < 0.4.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Big integer implementation for Rust.

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
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.39-1
- Update to 0.1.39

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.37-2
- Port to use rust-packaging

* Wed Mar 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.37-1
- Update to 0.1.37

* Thu Mar 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.36-1
- Initial package
