%define debug_package %{nil}
%define major 1

%define libname %mklibname ofono-qt %{major}
%define devname %mklibname -d ofono-qt

%define snapshot 20200827

Summary:	Library for accessing the oFono phone system through Qt and QtQuick
Name:		ofono-qt
Version:	0.0
Release:	%{?snapshot:0.%{snapshot}.}1
Source0:	https://github.com/gemian/ofono-qt/archive/master/ofono-qt-%{snapshot}.tar.gz
BuildRequires:	pkgconfig(ofono)
BuildRequires:	qmake5
BuildRequires:	make
BuildRequires:	doxygen
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(dbus-1)
License:	LGPLv2.1

%description
A library for accessing the ofono daemon, and a declarative plugin for it.
This allows accessing ofono in qtquick and friends.

%package -n %{libname}
Summary:	Library for accessing the oFono phone system through Qt and QtQuick

%description -n %{libname}
A library for accessing the ofono daemon, and a declarative plugin for it.
This allows accessing ofono in qtquick and friends.

%package -n %{devname}
Summary:	Development files for ofono-qt
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
A library for accessing the ofono daemon, and a declarative plugin for it.
This allows accessing ofono in qtquick and friends.

This package contains files needed to develop applications using ofono-qt.

%package tests
Summary:	Tests for ofono-qt
Requires:	%{libname} = %{EVRD}

%description tests
A library for accessing the ofono daemon, and a declarative plugin for it.
This allows accessing ofono in qtquick and friends.

This package contains tests for ofono-qt.

%prep
%autosetup -p1 -n ofono-qt-master
qmake-qt5 *.pro

%build
%make_build

%install
%make_build install INSTALL_ROOT=%{buildroot}

%files -n %{libname}
%{_libdir}/libofono-qt.so.%{major}*

%files -n %{devname}
%{_libdir}/libofono-qt.so
%{_libdir}/libofono-qt.prl
%{_libdir}/pkgconfig/ofono-qt.pc
%{_libdir}/qt5/include/ofono-qt
%{_libdir}/qt5/share/qt5/mkspecs/features/ofono-qt.prf

%files tests
%{_libdir}/qt5/lib/libofono-qt/tests
