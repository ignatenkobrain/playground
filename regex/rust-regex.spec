# Generated by rust2rpm
# regex -> quickcheck -> env_logger -> regex
%bcond_with check
%global debug_package %{nil}

%global crate regex

Name:           rust-%{crate}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Implementation of regular expressions for Rust

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/regex
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * No path dependencies
# * simd is probably nightly-only and we don't want to have such accelerations anyway
Patch0:         regex-0.2.1-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  (crate(aho-corasick) >= 0.6.0 with crate(aho-corasick) < 0.7.0)
BuildRequires:  (crate(memchr) >= 1.0.0 with crate(memchr) < 2.0.0)
BuildRequires:  (crate(regex-syntax) >= 0.4.0 with crate(regex-syntax) < 0.5.0)
BuildRequires:  (crate(thread_local) >= 0.3.2 with crate(thread_local) < 0.4.0)
BuildRequires:  (crate(utf8-ranges) >= 1.0.0 with crate(utf8-ranges) < 2.0.0)
%if %{with check}
BuildRequires:  (crate(lazy_static) >= 0.2.2 with crate(lazy_static) < 0.3.0)
BuildRequires:  (crate(quickcheck) >= 0.4.1 with crate(quickcheck) < 0.5.0)
BuildRequires:  (crate(rand) >= 0.3.15 with crate(rand) < 0.4.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
An implementation of regular expressions for Rust. This implementation uses
finite automata and guarantees linear time matching on all inputs.

This package contains library source intended for building other packages
which use %{crate} from crates.io.

%prep
%autosetup -n %{crate}-%{version} -p1
rm -vrf {appveyor.yml,ci,scripts}
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
* Sat Feb 25 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-1
- Initial package
