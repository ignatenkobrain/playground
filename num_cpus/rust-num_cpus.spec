# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate num_cpus

Name:           rust-%{crate}
Version:        1.3.0
Release:        1%{?dist}
Summary:        Get the number of CPUs on a machine

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/num_cpus
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo
# [dependencies]
BuildRequires:  (crate(libc) >= 0.2.0 with crate(libc) < 0.3.0)

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Get the number of CPUs on a machine.

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
* Wed Mar 01 2017 Igor Gnatenko <ignatenkobrain@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-2
- Use rich dependencies

* Sun Feb 12 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-1
- Initial package
