# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate unicode-xid

Name:           rust-%{crate}
Version:        0.0.4
Release:        1%{?dist}
Summary:        Determine whether characters have properties according to Unicode Standard Annex #31

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/unicode-xid
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Determine whether characters have the XID_Start or XID_Continue
properties according to Unicode Standard Annex #31.

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
%license LICENSE-MIT LICENSE-APACHE COPYRIGHT
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.0.4-1
- Initial package