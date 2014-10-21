Name:		stratagus
Summary:	A real time strategy game engine
Version:	2.2.7
Release:	2
Source0:	http://launchpad.net/stratagus/trunk/%{version}/+download/%{name}_%{version}.orig.tar.gz
URL:		http://stratagus.sourceforge.net/
Group:		Games/Strategy
License:	GPLv2
BuildRequires:	cmake
BuildRequires:	bzip2-devel
BuildRequires:	libmikmod-devel
BuildRequires:	lua5.1-devel
BuildRequires:	pkgconfig(mng)
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

