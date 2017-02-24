# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate time

Name:           rust-%{crate}
Version:        0.1.36
Release:        2%{?dist}
Summary:        Utilities for working with time-related functions in Rust

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/time
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# https://github.com/rust-lang-deprecated/time/pull/143
Patch0:         time-0.1.36-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  (crate(libc) >= 0.2.1 with crate(libc) < 0.3.0)
BuildRequires:  (crate(rustc-serialize) >= 0.3.0 with crate(rustc-serialize) < 0.4.0)
%if %{with check}
BuildRequires:  (crate(log) >= 0.3.0 with crate(log) < 0.4.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Utilities for working with time-related functions in Rust.

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
* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.36-2
- Use rich dependencies

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.36-1
- Initial package