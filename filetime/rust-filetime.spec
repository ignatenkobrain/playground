# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate filetime

Name:           rust-%{crate}
Version:        0.1.10
Release:        2%{?dist}
Summary:        Platform-agnostic accessors of timestamps in File metadata

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/filetime
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(libc) >= 0.2.0 with crate(libc) < 0.3.0)
%if %{with check}
BuildRequires:  (crate(tempdir) >= 0.3.0 with crate(tempdir) < 0.4.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Platform-agnostic accessors of timestamps in File metadata.

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
* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.10-2
- Port to use rust-packaging

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.10-1
- Initial package
