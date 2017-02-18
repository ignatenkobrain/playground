# Generated by rust2rpm
%bcond_with check
%global debug_package %{nil}

%global crate memchr

Name:           rust-%{crate}
Version:        1.0.1
Release:        3%{?dist}
Summary:        Safe interface to memchr

License:        Unlicense or MIT
URL:            https://crates.io/crates/memchr
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  crate(libc) >= 0.2.18
BuildConflicts: crate(libc) >= 0.3.0
%if %{with check}
BuildRequires:  crate(quickcheck) >= 0.4.1
BuildConflicts: crate(quickcheck) >= 0.5.0
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Safe interface to memchr.

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
* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-3
- Use awk to trim dev-dependencies and get them back before installing

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-2
- Use patch file for dropping dependencies

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-1
- Initial package
