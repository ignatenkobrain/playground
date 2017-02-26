# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global openssl_min 1.0.1

%global crate openssl-sys

Name:           rust-%{crate}
Version:        0.9.7
Release:        2%{?dist}
Summary:        FFI bindings to OpenSSL

License:        MIT
URL:            https://crates.io/crates/openssl-sys
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * No windows
Patch0:         openssl-sys-0.9.7-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo
# [dependencies]
BuildRequires:  (crate(libc) >= 0.2.0 with crate(libc) < 0.3.0)
# [build-dependencies]
BuildRequires:  (crate(gcc) >= 0.3.42 with crate(gcc) < 0.4.0)
BuildRequires:  (crate(pkg-config) >= 0.3.9 with crate(pkg-config) < 0.4.0)
BuildRequires:  pkgconfig(openssl) >= %{openssl_min}

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(openssl) >= %{openssl_min}

%description    devel
FFI bindings to OpenSSL.

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
%license LICENSE-MIT
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.7-2
- Rebuild

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.7-1
- Initial package
