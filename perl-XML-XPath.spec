%define upstream_name 	 XML-XPath
%define upstream_version 1.13

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	XML::XPath - a set of modules for parsing and evaluating XPath statements
License: 	GPL+ or Artistic
Group:		Development/Perl
Url:		http://sergeant.org
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSERGEANT/%{upstream_name}-%{upstream_version}.tar.bz2
# (oe) http://rt.cpan.org/NoAuth/Bug.html?id=6363
Patch0:		XML-XPath-1.13-bug6363.diff

BuildRequires:	perl(XML::Parser)

BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}


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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO examples
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/XML/*
