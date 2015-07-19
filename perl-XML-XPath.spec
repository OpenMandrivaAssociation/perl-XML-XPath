%define modname	XML-XPath
%define modver	1.13

Summary:	XML::XPath - a set of modules for parsing and evaluating XPath statements
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	16
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://sergeant.org
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSERGEANT/%{modname}-%{modver}.tar.bz2
# (oe) http://rt.cpan.org/NoAuth/Bug.html?id=6363
Patch0:		XML-XPath-1.13-bug6363.diff
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)

%description
This module aims to comply exactly to the XPath specification 
at http://www.w3.org/TR/xpath and yet allow extensions to be 
added in the form of functions. Modules such as XSLT and 
XPointer may need to do this as they support functionality 
beyond XPath.

%prep
%setup -qn %{modname}-%{modver}
%apply_patches

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
%{perl_vendorlib}/XML/*
%{_mandir}/man3/*

