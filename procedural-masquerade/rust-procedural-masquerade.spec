# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate procedural-masquerade

Name:           rust-%{crate}
Version:        0.1.2
Release:        1%{?dist}
Summary:        macro_rules for making proc_macro_derive pretending to be proc_macro

# https://github.com/servo/rust-cssparser/issues/158
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/procedural-masquerade
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
macro_rules for making proc_macro_derive pretending to be proc_macro.

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
* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.2-1
- Initial package
