# Generated by rust2rpm
# synom -> syn -> synom
%bcond_with check
%global debug_package %{nil}

%global crate synom

Name:           rust-%{crate}
Version:        0.11.3
Release:        3%{?dist}
Summary:        Stripped-down Nom parser used by Syn

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/synom
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * No paths
# * Bump unicode-xid to 0.1, https://github.com/dtolnay/syn/commit/98d27033fd3d39dc41cd82988d36bbb0152b2c43
Patch0:         synom-0.11.3-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(unicode-xid) >= 0.1.0 with crate(unicode-xid) < 0.2.0)
%if %{with check}
# [dev-dependencies]
BuildRequires:  ((crate(syn) >= 0.11.0 with crate(syn) < 0.12.0) with crate(syn/parsing) with crate(syn/full))
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Stripped-down Nom parser used by Syn.

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
* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.3-3
- Bump unicode-xid to 0.1

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.3-2
- Port to use rust-packaging

* Sun Mar 05 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.3-1
- Update to 0.11.3

* Tue Feb 28 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.2-1
- Update to 0.11.2

* Sat Feb 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.0-1
- Initial package
