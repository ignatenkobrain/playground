# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate num_cpus

Name:           rust-%{crate}
Version:        1.2.1
Release:        2%{?dist}
Summary:        Get the number of CPUs on a machine

License:        MIT or ASL 2.0
URL:            https://crates.io/crates/num_cpus
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  (crate(libc) >= 0.2.0 with crate(libc) < 0.3.0)

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
%{summary}.

%prep
%autosetup -n %{crate}-%{version}
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
* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-2
- Use rich dependencies

* Sun Feb 12 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-1
- Initial package
