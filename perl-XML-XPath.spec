%define upstream_name 	 XML-XPath
%define upstream_version 1.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8

Summary:	XML::XPath - a set of modules for parsing and evaluating XPath statements
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://sergeant.org
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSERGEANT/%{upstream_name}-%{upstream_version}.tar.bz2
# (oe) http://rt.cpan.org/NoAuth/Bug.html?id=6363
Patch0:		XML-XPath-1.13-bug6363.diff

BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)

BuildArch:	noarch

%description
This module aims to comply exactly to the XPath specification 
at http://www.w3.org/TR/xpath and yet allow extensions to be 
added in the form of functions. Modules such as XSLT and 
XPointer may need to do this as they support functionality 
beyond XPath.

%prep
%setup -q  -n %{upstream_name}-%{upstream_version}
%patch0 -p1

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README TODO examples
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/XML/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.130.0-5mdv2012.0
+ Revision: 765858
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.130.0-3
+ Revision: 667462
- mass rebuild

* Mon Apr 26 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.130.0-2mdv2011.0
+ Revision: 539096
- rebuild, remove unused requires:

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.130.0-1mdv2010.0
+ Revision: 408257
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.13-10mdv2009.0
+ Revision: 224676
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.13-9mdv2008.1
+ Revision: 180662
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Apr 25 2007 Olivier Thauvin <nanardon@mandriva.org> 1.13-8mdv2008.0
+ Revision: 18033
- rebuild


* Mon Apr 03 2006 Buchan Milne <bgmilne@mandriva.org> 1.13-7mdk
- Rebuild
- use mkrel

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.13-6mdk
- added the complete patch...
- run the test

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.13-5mdk
- added P0 (http://rt.cpan.org/NoAuth/Bug.html?id=6363)

* Tue Nov 11 2003 Michael Scherer <scherer.michael@free.fr> 1.13-4mdk 
- BuildRequires ( perl-XML-Parser, perl-devel )

* Fri Aug 15 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.13-3mdk
- rebuild for new perl
- don't use PREFIX
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.13-2mdk
- rebuild for new auto{prov,req}

