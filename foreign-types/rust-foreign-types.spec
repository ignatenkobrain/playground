# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate foreign-types

Name:           rust-%{crate}
Version:        0.2.0
Release:        2%{?dist}
Summary:        Framework for Rust wrappers over C APIs

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/foreign-types
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
A framework for Rust wrappers over C APIs.

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
* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-2
- Port to use rust-packaging

* Mon Apr 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-1
- Initial package