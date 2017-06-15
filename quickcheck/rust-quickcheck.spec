# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate quickcheck

Name:           rust-%{crate}
Version:        0.4.2
Release:        1%{?dist}
Summary:        Automatic property based testing with shrinking

License:        Unlicense or MIT
URL:            https://crates.io/crates/quickcheck
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# Bump env_logger to 0.4, https://github.com/BurntSushi/quickcheck/pull/160
Patch0:         quickcheck-0.4.2-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(env_logger) >= 0.4.0 with crate(env_logger) < 0.5.0)
BuildRequires:  (crate(log) >= 0.3.0 with crate(log) < 0.4.0)
BuildRequires:  (crate(rand) >= 0.3.0 with crate(rand) < 0.4.0)

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Automatic property based testing with shrinking.

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
%license UNLICENSE LICENSE-MIT COPYING
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.2-1
- Update to 0.4.2

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-2
- Port to use rust-packaging

* Sat Feb 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-1
- Initial package
