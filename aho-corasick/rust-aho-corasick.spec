# Generated by rust2rpm
%bcond_with check
%global debug_package %{nil}

%global crate aho-corasick

Name:           rust-%{crate}
Version:        0.6.2
Release:        3%{?dist}
Summary:        Fast multiple substring searching with finite state machines

License:        Unlicense or MIT
URL:            https://crates.io/crates/aho-corasick
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo
# [dependencies]
BuildRequires:  (crate(memchr) >= 1.0.0 with crate(memchr) < 2.0.0)
%if %{with check}
# [dev-dependencies]
BuildRequires:  (crate(csv) >= 0.15.0 with crate(csv) < 0.16.0)
BuildRequires:  (crate(docopt) >= 0.7.0 with crate(docopt) < 0.8.0)
BuildRequires:  (crate(memmap) >= 0.5.0 with crate(memmap) < 0.6.0)
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
Fast multiple substring searching with finite state machines.

This package contains library source intended for building other packages
which use %{crate} from crates.io.

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install
rm -vf %{buildroot}%{_bindir}/aho-corasick-dot

%if %{with check}
%check
%cargo_test
%endif

%files          devel
%license UNLICENSE LICENSE-MIT COPYING
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Sat Mar 11 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.2-3
- Rename with rust prefix
- Don't ship useless binary

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.2-2
- Use rich dependencies

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.2-1
- Initial package
