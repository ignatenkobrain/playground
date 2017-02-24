# Generated by rust2rpm
# walkdir -> docopt(dev) -> regex -> simd(opt) -> serde_derive(opt) -> syn -> walkdir(dev)
%bcond_with check
%global debug_package %{nil}

%global crate walkdir

Name:           rust-%{crate}
Version:        1.0.7
Release:        2%{?dist}
Summary:        Recursively walk a directory

License:        Unlicense or MIT
URL:            https://crates.io/crates/walkdir
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
Patch0:         walkdir-1.0.7-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  (crate(same-file) >= 0.1.1 with crate(same-file) < 0.2.0)
%if %{with check}
BuildRequires:  (crate(docopt) >= 0.7.0 with crate(docopt) < 0.8.0)
BuildRequires:  (crate(quickcheck) >= 0.4.0 with crate(quickcheck) < 0.5.0)
BuildRequires:  (crate(rand) >= 0.3.0 with crate(rand) < 0.4.0)
BuildRequires:  (crate(rustc-serialize) >= 0.3.0 with crate(rustc-serialize) < 0.4.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Recursively walk a directory.

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
* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.7-2
- Use rich dependencies

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.7-1
- Initial package
