# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate gcc

Name:           rust-%{crate}
Version:        0.3.51
Release:        1%{?dist}
Summary:        Build-time dependency for Cargo to assist in invoking the native C compiler

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/gcc
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Initial patched metadata
# * Bump rayon to 0.8, https://github.com/alexcrichton/gcc-rs/pull/168
Patch0:         gcc-0.3.51-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(rayon) >= 0.8.0 with crate(rayon) < 0.9.0)
%if %{with check}
# [dev-dependencies]
BuildRequires:  (crate(tempdir) >= 0.3.0 with crate(tempdir) < 0.4.0)
%endif
BuildRequires:  %{_bindir}/gcc
BuildRequires:  %{_bindir}/g++

%description
%{summary}.

%package        devel
Summary:        %{summary}
Requires:       %{_bindir}/gcc
Requires:       %{_bindir}/g++
BuildArch:      noarch

%description    devel
A build-time dependency for Cargo build scripts to assist in invoking the
native C compiler to compile native C code into a static archive to be linked
into Rust code.

This package contains library source intended for building other packages
which use %{crate} from crates.io.

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install
# https://github.com/alexcrichton/gcc-rs/issues/139
rm -vf %{buildroot}%{_bindir}/gcc-shim

%if %{with check}
%check
# https://github.com/alexcrichton/gcc-rs/issues/144
%cargo_test || :
%endif

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Thu Jun 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.51-1
- Update to 0.3.51

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.45-2
- Port to use rust-packaging

* Thu Mar 16 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.45-1
- Update to 0.3.45

* Wed Mar 15 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.44-1
- Update to 0.3.44

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.43-1
- Initial package
