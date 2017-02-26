# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate toml

Name:           rust-%{crate}
Version:        0.3.0
Release:        1%{?dist}
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/toml
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  (crate(serde) >= 0.9.6 with crate(serde) < 0.10.0)
%if %{with check}
BuildRequires:  (crate(serde_derive) >= 0.9.0 with crate(serde_derive) < 0.10.0)
BuildRequires:  (crate(serde_json) >= 0.9.0 with crate(serde_json) < 0.10.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
A native Rust encoder and decoder of TOML-formatted files and streams. Provides
implementations of the standard Serialize/Deserialize traits for TOML data to
facilitate deserializing and serializing Rust structures.

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
* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-1
- Initial package
