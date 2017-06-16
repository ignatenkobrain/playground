# Generated by rust2rpm
# Tests are not distributed, https://github.com/carllerche/mio/issues/620
# Doctests require networking
%bcond_with check
%global debug_package %{nil}

%global crate mio

Name:           rust-%{crate}
Version:        0.6.9
Release:        1%{?dist}
Summary:        Lightweight non-blocking IO

License:        MIT
URL:            https://crates.io/crates/mio
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * No windows
# * Bump lazycell and env_logger, https://github.com/carllerche/mio/pull/619
Patch0:         mio-0.6.9-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(iovec) >= 0.1.0 with crate(iovec) < 0.2.0)
BuildRequires:  (crate(lazycell) >= 0.5.0 with crate(lazycell) < 0.6.0)
BuildRequires:  (crate(libc) >= 0.2.19 with crate(libc) < 0.3.0)
BuildRequires:  (crate(log) >= 0.3.1 with crate(log) < 0.4.0)
BuildRequires:  (crate(net2) >= 0.2.29 with crate(net2) < 0.3.0)
BuildRequires:  (crate(slab) >= 0.3.0 with crate(slab) < 0.4.0)
%if %{with check}
# [dev-dependencies]
BuildRequires:  (crate(bytes) >= 0.3.0 with crate(bytes) < 0.4.0)
BuildRequires:  (crate(env_logger) >= 0.4.0 with crate(env_logger) < 0.5.0)
BuildRequires:  (crate(tempdir) >= 0.3.4 with crate(tempdir) < 0.4.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Lightweight non-blocking IO.

This package contains library source intended for building other packages
which use %{crate} from crates.io.

%prep
%autosetup -n %{crate}-%{version} -p1
rm -vrf ci
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
%license LICENSE
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Fri Jun 16 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.9-1
- Initial package