Name:		stratagus
Summary:	A real time strategy game engine
Version:	2.2.6
Release:	%mkrel 1
Source0:	http://launchpad.net/stratagus/trunk/%{version}/+download/%{name}_%{version}.orig.tar.gz
URL:		http://stratagus.sourceforge.net/
Group:		Games/Strategy
License:	GPLv2
BuildRequires:	cmake
BuildRequires:	mesagl-devel
BuildRequires:	SDL-devel
BuildRequires:	bzip2-devel
BuildRequires:	libx11-devel
BuildRequires:	lua-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libmng-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	libtheora-devel
BuildRequires:	png-devel
BuildRequires:	zlib-devel
BuildRequires:	sqlite3-devel

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
%__rm -rf %{buildroot}
%makeinstall_std -C build

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README doc/*
%{_gamesbindir}/%{name}
%{_bindir}/png2stratagus
%{_sbindir}/metaserver

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}*

