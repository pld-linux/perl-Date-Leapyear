#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Date
%define	pnam	Leapyear
Summary:	Date::Leapear Perl module - is a particular year a leap year?
Summary(pl):	Modu³ Perla Date::Leapyear - sprawdzanie przestêpno¶ci zadanego roku
Name:		perl-Date-Leapyear
Version:	1.71
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Test-Simple
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Is a particular year a leap year?

%description -l pl
Modu³ perla Date::Leapyear - sprawdzaj±cy, czy dany rok jest
przestêpny.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{perl_vendorlib}/Date/Leapyear.pm
%{_mandir}/man3/*
