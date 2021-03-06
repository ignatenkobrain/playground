# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate base64

Name:           rust-%{crate}
Version:        0.6.0
Release:        1%{?dist}
Summary:        Encodes ands decode base64 as bytes or utf8

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/base64
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * Relax rand version, https://github.com/alicemaz/rust-base64/pull/40
Patch0:         base64-0.6.0-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(byteorder) >= 1.0.0 with crate(byteorder) < 2.0.0)
BuildRequires:  (crate(safemem) >= 0.2.0 with crate(safemem) < 0.3.0)
%if %{with check}
# [dev-dependencies]
BuildRequires:  (crate(rand) >= 0.3.15 with crate(rand) < 0.4.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Encodes and decodes base64 as bytes or utf8.

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
* Fri Jun 16 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-1
- Initial package
