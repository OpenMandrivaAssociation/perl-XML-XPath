%define modname	XML-XPath
%define modver	1.49

Summary:	XML::XPath - a set of modules for parsing and evaluating XPath statements
Name:		perl-%{modname}
Version:	%{modver}
Release:	5
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://sergeant.org
Source0:	https://cpan.metacpan.org/authors/id/M/MA/MANWAR/XML-XPath-%{modver}.tar.gz
# (oe) http://rt.cpan.org/NoAuth/Bug.html?id=6363
Patch0:		XML-XPath-1.13-bug6363.diff
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(Path::Tiny)

%description
This module aims to comply exactly to the XPath specification 
at http://www.w3.org/TR/xpath and yet allow extensions to be 
added in the form of functions. Modules such as XSLT and 
XPointer may need to do this as they support functionality 
beyond XPath.

%prep
%setup -qn %{modname}-%{modver}


%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test || true

%install
%makeinstall_std

%files
%doc README TODO examples
%{_bindir}/*
%{perl_vendorlib}/XML/*
%{_mandir}/man1/*
%{_mandir}/man3/*

