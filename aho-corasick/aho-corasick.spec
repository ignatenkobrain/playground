# Generated by rust2rpm
%bcond_with check

%global crate aho-corasick

Name:           %{crate}
Version:        0.6.2
Release:        1%{?dist}
Summary:        Fast multiple substring searching with finite state machines

License:        Unlicense or MIT
URL:            https://crates.io/crates/aho-corasick
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

%if ! %{with check}
BuildRequires:  gawk >= 4.1.0
%endif
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  crate(memchr) >= 1.0.0
BuildConflicts: crate(memchr) >= 2.0.0
%if %{with check}
BuildRequires:  crate(csv) >= 0.15.0
BuildRequires:  crate(docopt) >= 0.7.0
BuildRequires:  crate(memmap) >= 0.5.0
BuildRequires:  crate(quickcheck) >= 0.4.0
BuildRequires:  crate(rand) >= 0.3.0
BuildRequires:  crate(rustc-serialize) >= 0.3.0
BuildConflicts: crate(csv) >= 0.16.0
BuildConflicts: crate(docopt) >= 0.8.0
BuildConflicts: crate(memmap) >= 0.6.0
BuildConflicts: crate(quickcheck) >= 0.5.0
BuildConflicts: crate(rand) >= 0.4.0
BuildConflicts: crate(rustc-serialize) >= 0.4.0
%endif

%description
%{summary}.

%package     -n rust-%{crate}-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n rust-%{crate}-devel
Fast multiple substring searching with finite state machines.

This package contains library source intended for building other packages
which use %{crate} from crates.io.

%prep
%autosetup -n %{crate}-%{version} -p1
%if ! %{with check}
# https://github.com/rust-lang/cargo/issues/3732
gawk -i inplace -v INPLACE_SUFFIX=.orig '/^\[dev-dependencies\]$/{f=1;next} /^\[/{f=0}; !f' Cargo.toml
%endif
%cargo_prep

%build
%cargo_build

%install
%cargo_install
%if ! %{with check}
install -p Cargo.toml.orig %{buildroot}%{cargo_registry}/%{crate}-%{version}/Cargo.toml
%endif

%if %{with check}
%check
%cargo_test
%endif

%files
%license UNLICENSE LICENSE-MIT COPYING
%{_bindir}/aho-corasick-dot

%files       -n rust-%{crate}-devel
%license UNLICENSE LICENSE-MIT COPYING
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.2-1
- Initial package
