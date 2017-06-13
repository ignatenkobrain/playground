# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate libc

Name:           rust-%{crate}
Version:        0.2.21
Release:        2%{?dist}
Summary:        Library for types and bindings to native C functions

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/libc
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# https://github.com/rust-lang/cargo/issues/3642
Patch0:         libc-0.2.21-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
A library for types and bindings to native C functions often found in libc or
other common platform libraries.

This package contains library source intended for building other packages
which use %{crate} from crates.io.

%prep
%autosetup -n %{crate}-%{version} -p1
rm -vrf {.gitignore,.travis.yml,appveyor.yml,ci}
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
* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.21-2
- Port to use rust-packaging

* Sun Mar 05 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.21-1
- Update to 0.2.21

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.20-3
- Strip unneeded files

* Sun Feb 12 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.20-2
- Add license files
- Fix license tag

* Sun Feb 12 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.20-1
- Initial package
