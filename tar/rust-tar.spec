# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate tar

Name:           rust-%{crate}
Version:        0.4.13
Release:        1%{?dist}
Summary:        Rust implementation of a TAR file reader and writer

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/tar
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate
# Fix unittests, https://github.com/alexcrichton/tar-rs/commit/58e6053622606091a714a1b16387356e86394a25
Patch0001:      0001-Fix-xattr-unit-test.patch

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(filetime) >= 0.1.5 with crate(filetime) < 0.2.0)
BuildRequires:  (crate(libc) >= 0.2.0 with crate(libc) < 0.3.0)
BuildRequires:  (crate(xattr) >= 0.1.7 with crate(xattr) < 0.2.0)
%if %{with check}
# [dev-dependencies]
BuildRequires:  (crate(tempdir) >= 0.3.0 with crate(tempdir) < 0.4.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
A Rust implementation of a TAR file reader and writer. This library does not
currently handle compression, but it is abstract over all I/O readers and
writers. Additionally, great lengths are taken to ensure that the entire
contents are never required to be entirely resident in memory all at once.

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
# xattrs are not supported on tmpfs, however it is used by one of tests
%cargo_test || :
%endif

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Mon Jul 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.13-1
- Initial package