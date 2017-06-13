# Generated by rust2rpm
# Checks are pretty much useless, because they rely on tty
%bcond_with check
%global debug_package %{nil}

%global crate atty

Name:           rust-%{crate}
Version:        0.2.2
Release:        2%{?dist}
Summary:        Simple interface for querying atty

License:        MIT
URL:            https://crates.io/crates/atty
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * No windows
Patch0:         atty-0.2.2-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(libc) >= 0.2.0 with crate(libc) < 0.3.0)

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
A simple interface for querying atty.

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
%license LICENSE
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-2
- Port to use rust-packaging

* Wed Mar 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-1
- Initial package
