# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate strings

Name:           rust-%{crate}
Version:        0.0.1
Release:        2%{?dist}
Summary:        String utilities, including an unbalanced Rope

# https://github.com/nrc/strings.rs/commit/352766209ef1f07dcc49268c86510ce315b6f760
# https://github.com/nrc/strings.rs/issues/16
License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/strings
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(log) >= 0.3.0 with crate(log) < 0.4.0)

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
String utilities, including an unbalanced Rope.

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
* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.1-2
- Port to use rust-packaging

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.1-1
- Initial package
