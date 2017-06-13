# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate serde_codegen_internals

Name:           rust-%{crate}
Version:        0.14.2
Release:        2%{?dist}
Summary:        AST representation used by Serde codegen

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/serde_codegen_internals
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  ((crate(syn) >= 0.11.0 with crate(syn) < 0.12.0) with crate(syn/parsing))

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
AST representation used by Serde codegen. Unstable.

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
* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.2-2
- Port to use rust-packaging

* Thu Mar 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.2-1
- Update to 0.14.2

* Wed Mar 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.1-1
- Update to 0.14.1

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.0-1
- Update to 0.14.0

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.0-2
- Use rich dependencies

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.0-1
- Initial package
