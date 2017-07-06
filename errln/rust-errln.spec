# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate errln

Name:           rust-%{crate}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Utility macros to write to stderr

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/errln
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Utility macros to write to stderr.

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
%license LICENCE-MIT LICENCE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Thu Jul 06 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-1
- Initial package
