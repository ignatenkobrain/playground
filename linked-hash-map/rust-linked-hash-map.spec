# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate linked-hash-map

Name:           rust-%{crate}
Version:        0.4.2
Release:        3%{?dist}
Summary:        HashMap wrapper that holds key-value pairs in insertion order

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/linked-hash-map
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * clippy is nightly
Patch0:         linked-hash-map-0.4.2-fix-metadata.diff
# Bump serde to 1.0, https://github.com/contain-rs/linked-hash-map/pull/84
Patch0001:      0001-upgrade-serde-support-for-serde1.0.patch
Patch0002:      0002-port-tests-to-serde-1.0.patch

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(heapsize) >= 0.3.9 with crate(heapsize) < 0.4.0)
BuildRequires:  (crate(serde) >= 1.0.0 with crate(serde) < 2.0.0)
BuildRequires:  (crate(serde_test) >= 1.0.0 with crate(serde_test) < 2.0.0)

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
A HashMap wrapper that holds key-value pairs in insertion order.

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
* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-3
- Bump serde to 1.0

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-2
- Port to use rust-packaging

* Thu Mar 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Sat Feb 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-1
- Initial package
