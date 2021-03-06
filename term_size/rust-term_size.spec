# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate term_size

Name:           rust-%{crate}
Version:        0.3.0
Release:        1%{?dist}
Summary:        Functions for determining terminal sizes and dimensions

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/term_size
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * clippy is nightly
Patch0:         term_size-0.3.0-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(libc) >= 0.2.20 with crate(libc) < 0.3.0)

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Functions for determining terminal sizes and dimensions.

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
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3-2
- Port to use rust-packaging

* Sat Feb 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3-1
- Initial package
