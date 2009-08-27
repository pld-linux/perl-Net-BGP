#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	BGP
Summary:	Net::BGP - Border Gateway Protocol version 4 speaker/listener library
Summary(pl.UTF-8):	Net::BGP - biblioteka obsługująca Border Gateway Protocol w wersji 4
Name:		perl-Net-BGP
Version:	0.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b4498ae384db0524a1da66c9c051cf5f
URL:		http://search.cpan.org/dist/Net-BGP/
%if %{with tests}
BuildRequires:	perl(List::Util) >= 1.01
BuildRequires:	perl-Test-Harness >= 2.00
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is an implementation of the BGP-4 inter-domain routing
protocol. It encapsulates all of the functionality needed to establish
and maintain a BGP peering session and exchange routing update
information with the peer. It aims to provide a simple API to the BGP
protocol for the purposes of automation, logging, monitoring, testing,
and similar tasks using the power and flexibility of Perl. The module
does not implement the functionality of a RIB (Routing Information
Base) nor does it modify the kernel routing table of the host system.
However, such operations could be implemented using the API provided
by the module.

%description -l pl.UTF-8
Ten moduł jest implementacją protokołu routingu międzydomenowego
BGP-4. Zawiera on całą funkcjonalność potrzebną do ustanowienia i
zarządzania sesją BGP oraz wymiany informacji o uaktualnieniach
routingu z drugą stroną. Celem jest dostarczenie prostego API do
protokołu BGP do celów automatyzacji, logowania, monitorowania,
testowania i podobnych zadań z użyciem potęgi i elastyczności Perla.
Moduł nie zawiera implementacji RIB (Routing Information Base) ani
nie modyfikuje tablicy routingu w jądrze systemu, jednak takie
operacje mogą być zaimplementowane przy użyciu API dostarczonego
przez ten moduł.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
mv t/00-Signature.t{,.blah}

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
%{perl_vendorlib}/Net/BGP.pm
%{perl_vendorlib}/Net/BGP
%{_mandir}/man3/*
