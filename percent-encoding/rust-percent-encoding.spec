# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate percent-encoding

Name:           rust-%{crate}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Percent encoding and decoding

# https://github.com/servo/rust-url/issues/376
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/percent-encoding
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * no dependencies are needed, https://github.com/servo/rust-url/pull/377
Patch0:         percent-encoding-1.0.0-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Percent encoding and decoding.

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
* Wed Jul 05 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Initial package