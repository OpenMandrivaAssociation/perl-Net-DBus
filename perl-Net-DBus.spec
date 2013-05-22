%define	module Net-DBus
%define	name	perl-%{module}
%define	version	1.0.0

Name:		%{name}
Version:	%{version}
Release:	6
Summary:	Perl API to the DBus message system
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	dbus-devel
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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-4mdv2012.0
+ Revision: 765523
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-3
+ Revision: 764039
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2
+ Revision: 763284
- force it
- rebuild

* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-1
+ Revision: 688855
- new version

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.33.6-8
+ Revision: 667269
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.33.6-7mdv2011.0
+ Revision: 564556
- rebuild for perl 5.12.1

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for 5.12

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.33.6-5mdv2010.1
+ Revision: 426531
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.33.6-4mdv2009.1
+ Revision: 351838
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.33.6-3mdv2009.0
+ Revision: 265419
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 29 2008 Olivier Blin <blino@mandriva.org> 0.33.6-2mdv2009.0
+ Revision: 199340
- remove useless Data::Dumper import (frees 236 kB from net_applet RSS)

* Fri Feb 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.33.6-1mdv2008.1
+ Revision: 173856
- update to new version 0.33.6

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.33.5-2mdv2008.1
+ Revision: 151368
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.33.5-1mdv2008.0
+ Revision: 55599
- new version

* Mon Apr 23 2007 Olivier Blin <blino@mandriva.org> 0.33.4-1mdv2008.0
+ Revision: 17245
- 0.33.4 (and drop merged patch)


* Tue Aug 01 2006 Frederic Crozat <fcrozat@mandriva.com> 0.33.3-2mdv2007.0
- Patch0: don't use deprecated API

* Sun Jul 16 2006 Emmanuel Andry <eandry@mandriva.org> 0.33.3-1mdv2007.0
- New release 0.33.3

* Tue Jun 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.33.2-1mdv2007.0
- New release 0.33.2
- better source URL

* Sun Mar 12 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.33.1-1mdk
- New release 0.33.1
- spec cleanup
- fix directory ownership
- better summary
- TODO: fix tests

* Wed Jan 25 2006 Frederic Crozat <fcrozat@mandriva.com> 0.32.3-1mdk
- Release 0.32.3

* Mon Nov 21 2005 Olivier Blin <oblin@mandriva.com> 0.32.3-0.1mdk
- 0.32.3 (pre-release)
- remove Patch0, merged upstream

* Fri Nov 04 2005 Olivier Blin <oblin@mandriva.com> 0.32.2-2mdk
- Patch0: support servers not exporting introspection data
  (make RemoteObject able to use methods not exported,
   add back the Value class)

* Thu Oct 27 2005 Olivier Blin <oblin@mandriva.com> 0.32.2-1mdk
- 0.32.2
- drop Patch0 (merged upstream)
- skip tests, _dispatch_prop_read doesn't work if message serial is 0

* Mon Feb 21 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.0.1-3mdk
- use pkg-config to get dbus compilation flags, aka. lib64 fixes

* Sat Feb 12 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.0.1-2mdk
- add BuildRequires: libdbus-devel

* Thu Feb 10 2005 Olivier Blin <oblin@mandrakesoft.com> 0.0.1-1mdk
- initial Mandrakelinux release

