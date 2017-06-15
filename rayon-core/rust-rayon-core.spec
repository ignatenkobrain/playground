# Generated by rust2rpm
# Tests require #![cfg_attr(test, feature(conservative_impl_trait))]
%bcond_with check
%global debug_package %{nil}

%global crate rayon-core

Name:           rust-%{crate}
Version:        1.2.0
Release:        1%{?dist}
Summary:        Core APIs for Rayon

# https://github.com/nikomatsakis/rayon/issues/374
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/rayon-core
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(coco) >= 0.1.1 with crate(coco) < 0.2.0)
BuildRequires:  (crate(futures) >= 0.1.7 with crate(futures) < 0.2.0)
BuildRequires:  (crate(lazy_static) >= 0.2.2 with crate(lazy_static) < 0.3.0)
BuildRequires:  (crate(libc) >= 0.2.16 with crate(libc) < 0.3.0)
BuildRequires:  (crate(num_cpus) >= 1.2.0 with crate(num_cpus) < 2.0.0)
BuildRequires:  (crate(rand) >= 0.3.0 with crate(rand) < 0.4.0)

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Core APIs for Rayon.

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
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.0-1
- Initial package
