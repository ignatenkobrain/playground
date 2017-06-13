# Generated by rust2rpm
%bcond_without check
%global debug_package %{nil}

%global crate permutohedron

Name:           rust-%{crate}
Version:        0.2.2
Release:        2%{?dist}
Summary:        Generate permutations of sequences

# https://github.com/bluss/permutohedron/issues/5
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/permutohedron
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
Generate permutations of sequences. Either lexicographical order permutations,
or a minimal swaps permutation sequence implemented using Heap's algorithm.

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
%doc README.rst
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-2
- Port to use rust-packaging

* Sun Feb 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-1
- Initial package
