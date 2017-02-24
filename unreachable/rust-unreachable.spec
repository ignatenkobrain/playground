# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate unreachable

Name:           rust-%{crate}
Version:        0.1.1
Release:        2%{?dist}
Summary:        Unreachable code optimization hint in stable rust

License:        MIT
URL:            https://crates.io/crates/unreachable
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  (crate(void) >= 1.0.0 with crate(void) < 2.0.0)

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
An unreachable code optimization hint in stable rust.

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
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-2
- Use rich dependencies

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.1-1
- Initial package