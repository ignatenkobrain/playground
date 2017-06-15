# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate futures

Name:           rust-%{crate}
Version:        0.1.14
Release:        1%{?dist}
Summary:        Implementation of futures and streams featuring zero allocations

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/futures
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * No [workspace]
Patch0:         futures-0.1.14-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
An implementation of futures and streams featuring zero allocations,
composability, and iterator-like interfaces.

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
* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.14-1
- Initial package