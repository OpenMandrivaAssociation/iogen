%define name iogen
%define version 3.1
%define release %mkrel 1
%define subversion p0

Summary: A stress tool to produce heavily fragmented I/O operations
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}_%{version}%{subversion}.tar.bz2
License: BSD
Group: System/Kernel and hardware 
Url: http://www.peereboom.us/iogen/
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
