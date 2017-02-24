# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate spin

Name:           rust-%{crate}
Version:        0.4.5
Release:        1%{?dist}
Summary:        Synchronization primitives based on spinning

License:        MIT
URL:            https://crates.io/crates/spin
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
Synchronization primitives based on spinning.
They may contain data,
They are usable without `std`
and static initializers are available.

This package contains library source intended for building other packages
which use %{crate} from crates.io.

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
# https://github.com/mvdnes/spin-rs/issues/37
%cargo_build --no-default-features

%install
%cargo_install

%if %{with check}
%check
%cargo_test --no-default-features
%endif

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.5-1
- Initial package