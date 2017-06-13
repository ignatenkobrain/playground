# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate cfg-if

Name:           rust-%{crate}
Version:        0.1.0
Release:        2%{?dist}
Summary:        Macro to ergonomically define an item depending on a large number of #[cfg] parameters

# https://github.com/alexcrichton/cfg-if/issues/2
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/cfg-if
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
A macro to ergonomically define an item depending on a large number of #[cfg]
parameters. Structured like an if-else chain, the first matching branch is the
item that gets emitted.

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
* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-2
- Port to use rust-packaging

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-1
- Initial package

