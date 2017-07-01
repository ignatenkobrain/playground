# Generated by rust2rpm
%bcond_without check

%global crate yubibomb

Name:           rust-%{crate}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Rust command line tool that prints out a 6-digit random number

License:        GPLv3+
URL:            https://crates.io/crates/yubibomb
Source0:        https://crates.io/api/v1/crates/%{crate}/%{version}/download#/%{crate}-%{version}.crate

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
# [dependencies]
BuildRequires:  (crate(rand) >= 0.3.0 with crate(rand) < 0.4.0)

%description
%{summary}.

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate}
Don't you love when you accidentally tap your Yubikey when you have your
IRC client in focus and you send 987947 into Freenode? Want to be able
to have that experience without having to reach all the way over
to your laptop's USB port? Now you can!

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

%files       -n %{crate}
%license LICENSE
%doc README.md
%{_bindir}/yubibomb

%changelog
* Wed Jun 28 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-1
- Initial package