# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate tempdir

Name:           rust-%{crate}
Version:        0.3.5
Release:        1%{?dist}
Summary:        Library for managing a temporary directory

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/tempdir
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  crate(rand) >= 0.3.0
BuildConflicts: crate(rand) >= 0.4.0

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
%{summary}.

%prep
%autosetup -n %{crate}-%{version}
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
* Sun Feb 12 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.5-1
- Initial package
