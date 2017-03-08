# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate log

Name:           rust-%{crate}
Version:        0.3.7
Release:        1%{?dist}
Summary:        Lightweight logging facade for Rust

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/log
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
A lightweight logging facade for Rust.

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
* Wed Mar 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.7-1
- Update to 0.3.7

* Sun Feb 12 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.6-1
- Initial package
