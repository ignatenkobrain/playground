# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate scopeguard

Name:           rust-%{crate}
Version:        0.3.2
Release:        1%{?dist}
Summary:        RAII scope guard that will run a given closure when it goes out of scope

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/scopeguard
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
A RAII scope guard that will run a given closure when it goes out of scope,
even if the code between panics (assuming unwinding panic).

Defines the macros `defer!` and `defer_on_unwind!`; the latter only runs
if the scope is extited through unwinding on panic.

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
%doc README.rst
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-1
- Initial package
