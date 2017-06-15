# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate pkg-config

Name:           rust-%{crate}
Version:        0.3.9
Release:        2%{?dist}
Summary:        Library to run the pkg-config system tool

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/pkg-config
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
%if %{with check}
# [dev-dependencies]
BuildRequires:  (crate(lazy_static) >= 0.2.0 with crate(lazy_static) < 0.3.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       %{_bindir}/pkg-config

%description    devel
A library to run the pkg-config system tool at build time in order to be used
in Cargo build scripts.

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
* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.9-2
- Port to use rust-packaging

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.9-1
- Initial package
