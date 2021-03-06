%define		kdeappsver	21.04.3
%define		qtver		5.14.0
%define		kf5ver		5.71.0
%define		kaname		konsole
Summary:	KDE Terminal Emulator
Name:		ka5-%{kaname}
Version:	21.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	b482a35fd5e433cfd5553e051219d9a5
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5PrintSupport-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.13
BuildRequires:	kf5-extra-cmake-modules >= %{kf5ver}
BuildRequires:	kf5-kbookmarks-devel >= %{kf5ver}
BuildRequires:	kf5-kcompletion-devel >= %{kf5ver}
BuildRequires:	kf5-kconfig-devel >= %{kf5ver}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kf5ver}
BuildRequires:	kf5-kcoreaddons-devel >= %{kf5ver}
BuildRequires:	kf5-kcrash-devel >= %{kf5ver}
BuildRequires:	kf5-kdbusaddons-devel >= %{kf5ver}
BuildRequires:	kf5-kdoctools-devel >= %{kf5ver}
BuildRequires:	kf5-kglobalaccel-devel >= %{kf5ver}
BuildRequires:	kf5-kguiaddons-devel >= %{kf5ver}
BuildRequires:	kf5-ki18n-devel >= %{kf5ver}
BuildRequires:	kf5-kiconthemes-devel >= %{kf5ver}
BuildRequires:	kf5-kinit-devel >= %{kf5ver}
BuildRequires:	kf5-kio-devel >= %{kf5ver}
BuildRequires:	kf5-knewstuff-devel >= %{kf5ver}
BuildRequires:	kf5-knotifications-devel >= %{kf5ver}
BuildRequires:	kf5-knotifyconfig-devel >= %{kf5ver}
BuildRequires:	kf5-kparts-devel >= %{kf5ver}
BuildRequires:	kf5-kpty-devel >= %{kf5ver}
BuildRequires:	kf5-kservice-devel >= %{kf5ver}
BuildRequires:	kf5-ktextwidgets-devel >= %{kf5ver}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kf5ver}
BuildRequires:	kf5-kwindowsystem-devel >= %{kf5ver}
BuildRequires:	kf5-kxmlgui-devel >= %{kf5ver}
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires:	Qt5Core >= %{qtver}
Requires:	Qt5DBus >= %{qtver}
Requires:	Qt5PrintSupport >= %{qtver}
Requires:	Qt5Widgets >= %{qtver}
Requires:	kf5-kbookmarks >= %{kf5ver}
Requires:	kf5-kcompletion >= %{kf5ver}
Requires:	kf5-kconfig >= %{kf5ver}
Requires:	kf5-kconfigwidgets >= %{kf5ver}
Requires:	kf5-kcoreaddons >= %{kf5ver}
Requires:	kf5-kcrash >= %{kf5ver}
Requires:	kf5-kdbusaddons >= %{kf5ver}
Requires:	kf5-kglobalaccel >= %{kf5ver}
Requires:	kf5-kguiaddons >= %{kf5ver}
Requires:	kf5-ki18n >= %{kf5ver}
Requires:	kf5-kiconthemes >= %{kf5ver}
Requires:	kf5-kio >= %{kf5ver}
Requires:	kf5-knewstuff >= %{kf5ver}
Requires:	kf5-knotifications >= %{kf5ver}
Requires:	kf5-knotifyconfig >= %{kf5ver}
Requires:	kf5-kparts >= %{kf5ver}
Requires:	kf5-kpty >= %{kf5ver}
Requires:	kf5-kservice >= %{kf5ver}
Requires:	kf5-ktextwidgets >= %{kf5ver}
Requires:	kf5-kwidgetsaddons >= %{kf5ver}
Requires:	kf5-kwindowsystem >= %{kf5ver}
Requires:	kf5-kxmlgui >= %{kf5ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Konsole is a terminal emulator.

Features

• Tabs • Multiple profiles • Silence and Activity monitoring •
Bookmark support • Searching • Saving output

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{sr,zh_CN}
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konsole
%attr(755,root,root) %{_bindir}/konsoleprofile
%attr(755,root,root) %{_libdir}/libkdeinit5_konsole.so
%ghost %{_libdir}/libkonsoleprivate.so.21
%attr(755,root,root) %{_libdir}/libkonsoleprivate.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/konsolepart.so
%{_datadir}/metainfo/org.kde.konsole.appdata.xml
%{_desktopdir}/org.kde.konsole.desktop
%{_datadir}/knotifications5/konsole.notifyrc
%{_datadir}/konsole
%{_datadir}/kservices5/ServiceMenus/konsolerun.desktop
%{_datadir}/kservices5/konsolepart.desktop
%{_datadir}/kservicetypes5/terminalemulator.desktop
%{_datadir}/khotkeys/konsole.khotkeys
%{_datadir}/knsrcfiles/konsole.knsrc
%{_datadir}/qlogging-categories5/konsole.categories
