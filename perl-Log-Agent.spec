%define module	Log-Agent
%define upstream_version 1.000

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	1
Summary:  	Logging agent 
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/authors/id/M/MR/MROGASKI/Log-Agent-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Log::Agent is a general logging framework aimed at reusable modules.

%prep
%setup -q -n %{module}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Log
%{perl_vendorlib}/auto/Log
%{_mandir}/man3/*

%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.307-3mdv2010.0
+ Revision: 430482
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.307-2mdv2009.0
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu May 03 2007 Michael Scherer <misc@mandriva.org> 0.307-2mdv2008.0
+ Revision: 21206
- Rebuild, use %%mkrel


* Tue Oct 04 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.307-1mdk
- New release 0.307
- spec cleanup
- better url
- better summary
- enable tests

* Fri Dec 10 2004 Michael Scherer <misc@mandrake.org> 0.306-1mdk
- compress to bz2
- do not own standard dir
- from Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 
  - initial contrib.


