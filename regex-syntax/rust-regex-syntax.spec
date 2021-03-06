# Generated by rust2rpm
# regex-syntax -> quickcheck(dev) -> env_logger -> regex(opt) -> regex-syntax
%bcond_with check
%global debug_package %{nil}

%global crate regex-syntax

Name:           rust-%{crate}
Version:        0.4.1
Release:        1%{?dist}
Summary:        Regular expression parser

# https://github.com/rust-lang/regex/issues/342
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/regex-syntax
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
%if %{with check}
# [dev-dependencies]
BuildRequires:  (crate(quickcheck) >= 0.4.1 with crate(quickcheck) < 0.5.0)
BuildRequires:  (crate(rand) >= 0.3.15 with crate(rand) < 0.4.0)
%endif

%description
%{summary}.

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
A regular expression parser.

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
%{cargo_registry}/%{crate}-%{version}/

%changelog
* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1

* Wed Jun 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-3
- Port to use rust-packaging

* Fri Feb 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-2
- Use rich dependencies

* Sat Feb 18 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-1
- Initial package
