%include	/usr/lib/rpm/macros.perl
%define	pdir	Date
%define	pnam	Leapyear
Summary:	Is a particular year a leap year?
Summary(pl):	Modu³ perla Date-Leapyear
Name:		perl-Date-Leapyear
Version:	1.7
Release:	4
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Is a particular year a leap year?

%description -l pl
Modu³ perla Date-Leapyear - sprawdzaj±cy, czy dany rok jest
przestêpny.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

#gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc *.gz
%{perl_sitelib}/Date/Leapyear.pm
%{_mandir}/man3/*
