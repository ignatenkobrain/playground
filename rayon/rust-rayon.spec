# Generated by rust2rpm
# compiletest_rs is nightly
%bcond_with check
%global debug_package %{nil}

%global crate rayon

Name:           rust-%{crate}
Version:        0.6.0
Release:        2%{?dist}
Summary:        Simple work-stealing parallelism for Rust

License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/rayon
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * No [workspace]
Patch0:         rayon-0.6.0-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(deque) >= 0.3.1 with crate(deque) < 0.4.0)
BuildRequires:  (crate(libc) >= 0.2.16 with crate(libc) < 0.3.0)
BuildRequires:  (crate(num_cpus) >= 1.0.0 with crate(num_cpus) < 2.0.0)
BuildRequires:  (crate(rand) >= 0.3.0 with crate(rand) < 0.4.0)
%if %{with check}
BuildRequires:  (crate(compiletest_rs) >= 0.2.1 with crate(compiletest_rs) < 0.3.0)
BuildRequires:  (crate(num) >= 0.1.30 with crate(num) < 0.2.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Simple work-stealing parallelism for Rust.

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
%license LICENSE-APACHE LICENSE-MIT
%doc README.md RELEASES.md
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-2
- Port to use rust-packaging

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-1
- Initial package
