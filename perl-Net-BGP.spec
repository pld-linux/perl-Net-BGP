#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	BGP
Summary:	Net::BGP - Border Gateway Protocol version 4 speaker/listener library
Summary(pl):	Net::BGP - biblioteka obs³uguj±ca Border Gateway Protocol w wersji 4
Name:		perl-Net-BGP
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	946d056bd3db24a44b48d8538f8b5dc3
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

%description -l pl
Ten modu³ jest implementacj± protoko³u routingu miêdzydomenowego
BGP-4. Zawiera on ca³± funkcjonalno¶æ potrzebn± do ustanowienia i
zarz±dzania sesj± BGP oraz wymiany informacji o uaktualnieniach
routingu z drug± stron±. Celem jest dostarczenie prostego API do
protoko³u BGP do celów automatyzacji, logowania, monitorowania,
testowania i podobnych zadañ z u¿yciem potêgi i elastyczno¶ci Perla.
Modu³ nie zawiera implementacji RIB (Routing Information Base) ani
nie modyfikuje tablicy routingu w j±drze systemu, jednak takie
operacje mog± byæ zaimplementowane przy u¿yciu API dostarczonego
przez ten modu³.

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
%{perl_vendorlib}/Net/BGP.pm
%{perl_vendorlib}/Net/BGP
%{_mandir}/man3/*
