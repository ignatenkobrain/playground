# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate syntex_syntax

Name:           rust-%{crate}
Version:        0.58.0
Release:        1%{?dist}
Summary:        Export of libsyntax for code generation

# https://github.com/serde-rs/syntex/issues/115
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/syntex_syntax
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# https://github.com/serde-rs/syntex/pull/116
Patch0:         syntex_syntax-0.58.0-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  crate(bitflags) >= 0.8.0
BuildRequires:  crate(log) >= 0.3.6
BuildRequires:  crate(rustc-serialize) >= 0.3.16
BuildRequires:  crate(syntex_errors) >= 0.58.0
BuildRequires:  crate(syntex_pos) >= 0.58.0
BuildRequires:  crate(unicode-xid) >= 0.0.4
BuildConflicts: crate(bitflags) >= 0.9.0
BuildConflicts: crate(log) >= 0.4.0
BuildConflicts: crate(rustc-serialize) >= 0.4.0
BuildConflicts: crate(syntex_errors) >= 0.59.0
BuildConflicts: crate(syntex_pos) >= 0.59.0
BuildConflicts: crate(unicode-xid) >= 0.0.5

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Export of libsyntax for code generation.

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
* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.58.0-1
- Initial package
