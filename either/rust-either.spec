# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate either

Name:           rust-%{crate}
Version:        1.0.3
Release:        1%{?dist}
Summary:        Enum `Either`, with variants `Left` and `Right` and trait implementations

# https://github.com/bluss/either/issues/11
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/either
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
The enum `Either`, with variants `Left` and `Right` and trait implementations
including Iterator, Read, Write.

Either has methods that are similar to Option and Result.

Includes convenience macros `try_left!()` and `try_right!()` to
use for short-circuiting logic.

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
%doc README.rst
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-1
- Initial package