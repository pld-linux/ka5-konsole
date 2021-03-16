%define		kdeappsver	20.12.3
%define		qtver		5.9.0
%define		kaname		konsole
Summary:	KDE Terminal Emulator
Name:		ka5-%{kaname}
Version:	20.12.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ccb51a46be52c711149f4ea9b3218150
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-kbookmarks-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kemoticons-devel
BuildRequires:	kf5-kguiaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kinit-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kitemmodels-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-kparts-devel
BuildRequires:	kf5-kpty-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
%attr(755,root,root) %ghost %{_libdir}/libkonsoleprivate.so.20
%attr(755,root,root) %{_libdir}/libkonsoleprivate.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/konsolepart.so
%{_datadir}/metainfo/org.kde.konsole.appdata.xml
%{_desktopdir}/org.kde.konsole.desktop
%{_datadir}/knotifications5/konsole.notifyrc
%{_datadir}/konsole
%{_datadir}/kservices5/ServiceMenus/konsolehere.desktop
%{_datadir}/kservices5/ServiceMenus/konsolerun.desktop
%{_datadir}/kservices5/konsolepart.desktop
%{_datadir}/kservicetypes5/terminalemulator.desktop
%{_datadir}/khotkeys/konsole.khotkeys
%{_datadir}/knsrcfiles/konsole.knsrc
%{_datadir}/qlogging-categories5/konsole.categories
