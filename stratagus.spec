Name:		stratagus
Summary:	A real time strategy game engine
Version:	2.2.7
Release:	1
Source0:	http://launchpad.net/stratagus/trunk/%{version}/+download/%{name}_%{version}.orig.tar.gz
URL:		http://stratagus.sourceforge.net/
Group:		Games/Strategy
License:	GPLv2
BuildRequires:	cmake
BuildRequires:	bzip2-devel
BuildRequires:	libmikmod-devel
BuildRequires:	lua5.1-devel
BuildRequires:	mng-devel
BuildRequires:	tolua++-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(zlib)

%description
Stratagus is a free cross-platform real-time strategy gaming engine.
It includes support for playing over the internet/LAN, or playing a computer
opponent. The engine is configurable and can be used to create games with a
wide-range of features specific to your needs.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%prep
%setup -q -n %{name}_%{version}.orig

%build
# default build options seem to be fine
%cmake -DENABLE_DEV=ON
%make

%install
%makeinstall_std -C build

%files
%doc README doc/*
%{_gamesbindir}/%{name}
%{_bindir}/png2stratagus
%{_sbindir}/metaserver

%files devel
%{_includedir}/%{name}*

%changelog
* Sun Jan 29 2012 Andrey Bondrov <abondrov@mandriva.org> 2.2.6-1mdv2011.0
+ Revision: 769600
- Update BuildRequires (add tolua++-devel)
- Update BuildRequires (libmng-devel -> mng-devel)
- New version 2.2.6, update file list, switch to cmake, add devel subpackage

* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 2.2.5.5-1
+ Revision: 634641
- brimagemagick
- New version 2.2.5.5

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.4-4mdv2011.0
+ Revision: 614984
- the mass rebuild of 2010.1 packages

* Sat May 01 2010 Funda Wang <fwang@mandriva.org> 2.2.4-3mdv2010.1
+ Revision: 541412
- fix build with latest gcc44

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Aug 14 2008 Götz Waschk <waschk@mandriva.org> 2.2.4-2mdv2009.0
+ Revision: 271854
- use the right configure macro

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 2.2.4-1mdv2009.0
+ Revision: 140863
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat May 19 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.2.4-1mdv2008.0
+ Revision: 28435
- update to 2.2.24


* Tue Mar 13 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.2.3-1mdv2007.1
+ Revision: 142271
- 2.2.3
- builds now against lua 5.1
- work a bit around broken parallell build

* Wed Jan 17 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.2.2-1mdv2007.1
+ Revision: 109768
- new release: 2.2.2
  really drop broken lua 5.1 patch

* Tue Dec 12 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.2-1.061209.1mdv2007.1
+ Revision: 95885
- 2.2 really fix buildrequires
- Fix buildrequires
- try work around stupid buildrequires
- 2.2
- new version
- Import stratagus

* Fri Aug 25 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.1-6mdv2007.0
- rebuild against new liblua
- fix building against new lua (P0)

* Tue Oct 11 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.1-5mdk
- Fix BuildRequires
- Fix Redundant buildrequires 
	- X11-devel is already required by SDL-devel

* Thu Oct 06 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.1-4mdk
- Fix BuildRequires

* Mon Aug 22 2005 Eskild Hustvedt <eskild@mandriva.org> 2.1-3mdk
- Rebuild for new xorg

* Mon Jul 18 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.1-2mdk
- add opengl, mad, flac and cdaudio support
- add buildrequires too
- really use $RPM_OPT_FLAGS

* Sat Jul 09 2005 Eskild Hustvedt <eskild@mandrake.org> 2.1-1mdk
- Initial Mandriva Linux package

