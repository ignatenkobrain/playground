# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate rustc-demangle

Name:           rust-%{crate}
Version:        0.1.4
Release:        2%{?dist}
Summary:        Rust compiler symbol demangling

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/rustc-demangle
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Rust compiler symbol demangling.

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
* Tue Jun 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-2
- Port to use rust-packaging

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Sun Feb 12 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-3
- Sync with rust2rpm generator

* Fri Feb 10 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-2
- Sync with rust2rpm generator

* Fri Feb 10 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-1
- Initial package
