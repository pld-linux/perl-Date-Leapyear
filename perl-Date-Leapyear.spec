#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Date
%define	pnam	Leapyear
Summary:	Date::Leapyear Perl module - is a particular year a leap year?
Summary(pl):	Modu³ Perla Date::Leapyear - sprawdzanie przestêpno¶ci zadanego roku
Name:		perl-Date-Leapyear
Version:	1.71
Release:	4
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ca35097e84896eadf529f7a79f2c2e82
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Test-Simple
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Is a particular year a leap year?

%description -l pl
Modu³ Perla Date::Leapyear sprawdza, czy dany rok jest przestêpny.

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
%doc ChangeLog
%{perl_vendorlib}/Date/Leapyear.pm
%{_mandir}/man3/*
