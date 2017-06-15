# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate yaml-rust

Name:           rust-%{crate}
Version:        0.3.5
Release:        2%{?dist}
Summary:        YAML 1.2 parser for rust

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/yaml-rust
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * clippy is nightly
# * latest linked-hash-map, https://github.com/chyh1990/yaml-rust/pull/55
Patch0:         yaml-rust-0.3.5-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(linked-hash-map) >= 0.0.9 with crate(linked-hash-map) < 0.5.0)

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
The missing YAML 1.2 parser for rust.

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
* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.5-2
- Port to use rust-packaging

* Sat Feb 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.5-1
- Initial package
