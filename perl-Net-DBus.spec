%define	module Net-DBus
%define	name	perl-%{module}
%define	version	0.33.6
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl API to the DBus message system
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	libdbus-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
#%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_mandir}/*/*
%{perl_vendorarch}/Net
%{perl_vendorarch}/auto/Net
