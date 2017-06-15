# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate bytecount

Name:           rust-%{crate}
Version:        0.1.6
Release:        3%{?dist}
Summary:        Count occurrences of a byte in a byte slice, fast

License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/bytecount
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * simd is not what we want
# * Bump quickcheck to 0.4, https://github.com/llogiq/bytecount/commit/67868286c8750e1299eb310be17657bb5822eaed
Patch0:         bytecount-0.1.6-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
%if %{with check}
# [dev-dependencies]
BuildRequires:  (crate(bencher) >= 0.1.0 with crate(bencher) < 0.2.0)
BuildRequires:  (crate(quickcheck) >= 0.4.0 with crate(quickcheck) < 0.5.0)
BuildRequires:  (crate(rand) >= 0.3.14 with crate(rand) < 0.4.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Count occurrences of a byte in a byte slice, fast.

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
%license LICENSE.Apache2 LICENSE.MIT
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.6-3
- Relax quickcheck version

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.6-2
- Port to use rust-packaging

* Sat Feb 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.6-1
- Initial package
