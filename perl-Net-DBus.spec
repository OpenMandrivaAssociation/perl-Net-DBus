%define	module Net-DBus

Summary:	Perl API to the DBus message system
Name:		perl-%{module}
Version:	1.2.0
Release:	6
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Net::DBus
Source0:	http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	dbus-devel

%description
Net::DBus provides a Perl API for the DBus message system. The DBus Perl
interface is currently operating against the 0.32 development version of DBus,
but should work with later versions too, providing the API changes have not
been too drastic.

Users of this package are either typically, service providers in which case the
Net::DBus::Service and Net::DBus::Object modules are of most relevance, or are
client consumers, in which case Net::DBus::RemoteService and
Net::DBus::RemoteObject are of most relevance.

%prep
%autosetup -n %{module}-%{version} -p1

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build OPTIMIZE="%{optflags}"

%check
#make test

%install
%make_install

%files
%doc README
%{perl_vendorarch}/Net
%{perl_vendorarch}/auto/Net
%{_mandir}/man3/*

