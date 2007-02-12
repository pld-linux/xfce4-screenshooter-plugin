Summary:	Screenshooter plugin for Xfce panel
Summary(pl.UTF-8):   Wtyczka screenshooter dla panelu Xfce
Name:		xfce4-screenshooter-plugin
Version:	1.0.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-screenshooter-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	d12746c635eb28207161a3da1585aa75
URL:		http://goodies.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin allows to take screenshot.

%description -l pl.UTF-8
Ta wtyczka pozwala zrobić zrzut ekranu.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-screenshooter-plugin
%{_datadir}/xfce4/panel-plugins/screenshooter.desktop
