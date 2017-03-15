# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate encoding_rs

Name:           rust-%{crate}
Version:        0.5.0
Release:        1%{?dist}
Summary:        Gecko-oriented implementation of the Encoding Standard

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/encoding_rs
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * No simd
Patch0:         encoding_rs-0.5.0-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo
# [dependencies]
BuildRequires:  (crate(cfg-if) >= 0.1.0 with crate(cfg-if) < 0.2.0)
BuildRequires:  (crate(rayon) >= 0.6.0 with crate(rayon) < 0.7.0)

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
A Gecko-oriented implementation of the Encoding Standard.

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
%license COPYRIGHT LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Wed Mar 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Initial package
