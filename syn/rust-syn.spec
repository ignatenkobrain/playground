# Generated by rust2rpm
# syn -> syntex_pos(dev) -> serde_derive -> serde_derive_internals -> syn
%bcond_with check
%global debug_package %{nil}

%global crate syn

Name:           rust-%{crate}
Version:        0.11.11
Release:        1%{?dist}
Summary:        Nom parser for Rust source code

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/syn
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * No paths
# * Bump unicode-xid to 0.1, https://github.com/dtolnay/syn/commit/570695ea9345d9db9e089a9e21f2b157dffa6fb3
Patch0:         syn-0.11.11-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(quote) >= 0.3.7 with crate(quote) < 0.4.0)
BuildRequires:  (crate(synom) >= 0.11.0 with crate(synom) < 0.12.0)
BuildRequires:  (crate(unicode-xid) >= 0.1.0 with crate(unicode-xid) < 0.2.0)
%if %{with check}
# [dev-dependencies]
BuildRequires:  (crate(syntex_pos) >= 0.58.0 with crate(syntex_pos) < 0.59.0)
BuildRequires:  (crate(syntex_syntax) >= 0.58.0 with crate(syntex_syntax) < 0.59.0)
BuildRequires:  (crate(tempdir) >= 0.3.5 with crate(tempdir) < 0.4.0)
BuildRequires:  (crate(walkdir) >= 1.0.1 with crate(walkdir) < 2.0.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Nom parser for Rust source code.

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
* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.11-1
- Update to 0.11.11

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.9-2
- Port to use rust-packaging

* Tue Mar 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.9-1
- Update to 0.11.9

* Tue Feb 28 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.8-1
- Update to 0.11.8

* Mon Feb 27 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.7-1
- Update to 0.11.7

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.6-1
- Update to 0.11.6

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.4-1
- Initial package
