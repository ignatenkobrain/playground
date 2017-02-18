# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate term

Name:           rust-%{crate}
Version:        0.4.5
Release:        1%{?dist}
Summary:        Terminal formatting library

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/term
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
Patch0:         term-0.4.5-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
A terminal formatting library.

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
* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.5-1
- Initial package

