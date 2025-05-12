Name:		stratagus
Summary:	A real time strategy game engine
Version:	3.3.2
Release:	3
Source0:	https://github.com/Wargus/stratagus/archive/v%{version}/%{name}-%{version}.tar.gz
URL:		https://stratagus.com/
Group:		Games/Strategy
License:	GPLv2
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	bzip2-devel
BuildRequires:	libmikmod-devel
BuildRequires:	lua-devel
BuildRequires:	stdc++-static-devel
BuildRequires:	pkgconfig(libmng)
BuildRequires:	tolua++-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_image)
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
%autosetup -p1
# default build options seem to be fine
%cmake -DENABLE_DEV=ON -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%doc doc/*
%{_gamesbindir}/%{name}
%{_bindir}/png2stratagus

%files devel
%{_includedir}/%{name}*
