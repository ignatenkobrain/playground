# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate serde_codegen_internals

Name:           rust-%{crate}
Version:        0.13.0
Release:        1%{?dist}
Summary:        AST representation used by Serde codegen

# https://github.com/serde-rs/serde/issues/772
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/serde_codegen_internals
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  crate(syn) >= 0.11.0
BuildConflicts: crate(syn) >= 0.12.0

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
AST representation used by Serde codegen. Unstable.

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
* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.0-1
- Initial package
