%define name iogen
%define version 3.1
%define release 6
%define subversion p0

Summary: A stress tool to produce heavily fragmented I/O operations
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}_%{version}%{subversion}.tar.bz2
License: BSD
Group: System/Kernel and hardware 
Url: https://www.peereboom.us/iogen/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: groff-for-man

%description
Iogen is an I/O generator.
It forks child processes that each run a mix of reads and writes.
The idea is to generate heavily fragmented files to make the hardware suffer
as much as possible. This tool has been used to test filesystems, drivers,
firmware, and hardware devices.
It is by no means meant as a performance measuring tool since it tries to 
recreate the worst case scenario I/O.

%prep
%setup -q -n %{name}_%{version}%{subversion}

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%{_bindir}
mkdir -p %buildroot/%{_mandir}/man8
install -m 755 iogen %buildroot/%{_bindir}
mv iogen.cat8 %buildroot/%{_mandir}/man8/iogen.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/iogen
/%{_mandir}/man8/*



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 3.1-5mdv2011.0
+ Revision: 619673
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 3.1-4mdv2010.0
+ Revision: 429514
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 3.1-3mdv2009.0
+ Revision: 247235
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 3.1-1mdv2008.1
+ Revision: 140776
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 21 2007 Erwan Velu <erwan@mandriva.org> 3.1-1mdv2008.0
+ Revision: 29522
- 3.1p0

* Fri May 04 2007 Erwan Velu <erwan@mandriva.org> 3.0-1mdv2008.0
+ Revision: 22463
- Missing buildrequires
- Import iogen

