# Generated by rust2rpm
# Tests do not work in buildsys due to "Operation not supported"
%bcond_with check
%global debug_package %{nil}

%global crate xattr

Name:           rust-%{crate}
Version:        0.1.11
Release:        3%{?dist}
Summary:        UNIX extended filesystem attributes

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/xattr
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(libc) >= 0.2.0 with crate(libc) < 0.3.0)
%if %{with check}
# [dev-dependencies]
BuildRequires:  (crate(tempfile) >= 2.0.0 with crate(tempfile) < 3.0.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
UNIX extended filesystem attributes.

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
* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.11-3
- Disable tests

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.11-2
- Port to use rust-packaging

* Tue Feb 28 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.11-1
- Update to 0.1.11

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.10-1
- Initial package
