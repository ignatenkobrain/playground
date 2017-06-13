# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate num

Name:           rust-%{crate}
Version:        0.1.37
Release:        2%{?dist}
Summary:        Collection of numeric types and traits for Rust

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/num
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * No paths
Patch0:         num-0.1.37-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(num-bigint) >= 0.1.36 with crate(num-bigint) < 0.2.0)
BuildRequires:  (crate(num-complex) >= 0.1.36 with crate(num-complex) < 0.2.0)
BuildRequires:  (crate(num-integer) >= 0.1.33 with crate(num-integer) < 0.2.0)
BuildRequires:  (crate(num-iter) >= 0.1.33 with crate(num-iter) < 0.2.0)
BuildRequires:  (crate(num-rational) >= 0.1.36 with crate(num-rational) < 0.2.0)
BuildRequires:  (crate(num-traits) >= 0.1.37 with crate(num-traits) < 0.2.0)
%if %{with check}
# [dev-dependencies]
BuildRequires:  (crate(rand) >= 0.3.8 with crate(rand) < 0.4.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
A collection of numeric types and traits for Rust, including bigint,
complex, rational, range iterators, generic integers, and more!

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
* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.37-2
- Port to use rust-packaging

* Thu Mar 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.37-1
- Initial package
