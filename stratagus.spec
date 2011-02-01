%define	name	stratagus
%define	version 2.2.5.5
%define rel	1
%define	release	%mkrel %{rel}

Name:		%{name} 
Summary:	A real time strategy game engine
Version:	%{version} 
Release:	%{release} 
Source0:	http://launchpad.net/stratagus/trunk/%{version}/+download/%{name}_%{version}.orig.tar.gz
URL:		http://stratagus.sourceforge.net/
Group:		Games/Strategy
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
BuildRequires:	mesagl-devel
BuildRequires:	SDL-devel
BuildRequires:	bzip2-devel
BuildRequires:	libx11-devel
BuildRequires:	lua-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libmng-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	libtheora-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel

%description
Stratagus is a free cross-platform real-time strategy gaming engine.
It includes support for playing over the internet/LAN, or playing a computer
opponent. The engine is configurable and can be used to create games with a
wide-range of features specific to your needs.

%prep
%setup -q

%build
./autogen.sh
%configure2_5x	--with-opengl \
		--with-x \
		--with-bzip2 \
		--with-vorbis \
		--with-mikmod \
		--with-theora \
		--with-mng \
		EXTRA_CFLAGS="%{optflags}"

make

%install
rm -rf %{buildroot}
install -m755 stratagus -D %{buildroot}%{_gamesbindir}/stratagus

# Create and install icons
convert ./contrib/stratagus.ico -resize 32x32 ./stratagus-32.png
convert ./contrib/stratagus.ico -resize 48x48 ./stratagus-48.png
convert ./contrib/stratagus.ico -resize 16x16 ./stratagus-16.png
install -m644 stratagus-16.png -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 stratagus-32.png -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 stratagus-48.png -D %{buildroot}%{_liconsdir}/%{name}.png

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README doc/*
%{_gamesbindir}/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


