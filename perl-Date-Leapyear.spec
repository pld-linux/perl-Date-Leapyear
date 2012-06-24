%include	/usr/lib/rpm/macros.perl
Summary:	Is a particular year a leap year?
Summary(pl):	Modu� perla Date-Leapyear
Name:		perl-Date-Leapyear
Version:	1.7
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Date/Date-Leapyear-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Is a particular year a leap year?

%description -l pl
Modu� perla Date-Leapyear - sprawdzaj�cy, czy dany rok jest
przest�pny.

%prep
%setup -q -n Date-Leapyear-%{version}

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
