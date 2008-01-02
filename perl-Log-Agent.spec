%define module	Log-Agent
%define name	perl-%{module}
%define version	0.307
%define rel    	2

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Summary:  	Logging agent 
License:	GPL or Artistic
Group:		Development/Perl
Source:         http://search.cpan.org/CPAN/authors/id/M/MR/MROGASKI/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Log::Agent is a general logging framework aimed at reusable modules.

%prep

%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Log
%{perl_vendorlib}/auto/Log
%{_mandir}/man3/*

