#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	Test
%define	pnam	LongString
Summary:	Test::LongString - tests strings for equality, with more helpful failures
Summary(pl.UTF-8):	Test::LongString - sprawdzanie łańcuchów pod kątem identyczności
Name:		perl-Test-LongString
Version:	0.17
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8baab770f61ebd5647a9dd3679f42fbd
URL:		https://metacpan.org/dist/Test-LongString
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tests strings for equality, with more helpful failures.

%description -l pl.UTF-8
Sprawdzanie łańcuchów pod kątem identyczności z bardziej pomocnymi
niepowodzeniami.

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
%doc Changes README
%{perl_vendorlib}/Test/LongString.pm
%{_mandir}/man3/Test::LongString.3pm*
