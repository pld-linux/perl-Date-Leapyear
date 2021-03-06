#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Date
%define		pnam	Leapyear
Summary:	Date::Leapyear Perl module - is a particular year a leap year?
Summary(pl.UTF-8):	Moduł Perla Date::Leapyear - sprawdzanie przestępności zadanego roku
Name:		perl-Date-Leapyear
Version:	1.72
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bdfe5e8d435d6afcf7103269450e514b
URL:		http://search.cpan.org/dist/Date-Leapyear/
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Is a particular year a leap year?

%description -l pl.UTF-8
Moduł Perla Date::Leapyear sprawdza, czy dany rok jest przestępny.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Date/Leapyear.pm
%{_mandir}/man3/*
