# Generated by rust2rpm
# compiletest_rs is nightly
%bcond_with check
%global debug_package %{nil}

%global crate rayon

Name:           rust-%{crate}
Version:        0.8.2
Release:        1%{?dist}
Summary:        Simple work-stealing parallelism for Rust

License:        ASL 2.0 or MIT
URL:            https://crates.io/crates/rayon
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(rayon-core) >= 1.2.0 with crate(rayon-core) < 2.0.0)
%if %{with check}
# [dev-dependencies]
BuildRequires:  (crate(compiletest_rs) >= 0.2.1 with crate(compiletest_rs) < 0.3.0)
BuildRequires:  (crate(docopt) >= 0.7.0 with crate(docopt) < 0.8.0)
BuildRequires:  (crate(futures) >= 0.1.7 with crate(futures) < 0.2.0)
BuildRequires:  (crate(rand) >= 0.3.0 with crate(rand) < 0.4.0)
BuildRequires:  (crate(rustc-serialize) >= 0.3.0 with crate(rustc-serialize) < 0.4.0)
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
* Sat Jul 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.2-1
- Update to 0.8.2

* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-2
- Port to use rust-packaging

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-1
- Initial package
