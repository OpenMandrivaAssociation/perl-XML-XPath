%define module 	XML-XPath
%define version 1.13
%define release %mkrel 9

Summary:	XML::XPath - a set of modules for parsing and evaluating XPath statements
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group:		Development/Perl
URL:		http://sergeant.org 
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSERGEANT/%{module}-%{version}.tar.bz2
# (oe) http://rt.cpan.org/NoAuth/Bug.html?id=6363
Patch0:		XML-XPath-1.13-bug6363.diff
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-devel
Requires:	perl-XML-Parser
Requires:	perl-XML-XSLT
Requires:	perl-XML-Grove
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
This module aims to comply exactly to the XPath specification 
at http://www.w3.org/TR/xpath and yet allow extensions to be 
added in the form of functions. Modules such as XSLT and 
XPointer may need to do this as they support functionality 
beyond XPath.

%prep

%setup -q  -n %{module}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO examples
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/XML/*

