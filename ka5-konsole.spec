#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		qtver		5.15.2
%define		kf5ver		5.71.0
%define		kaname		konsole
Summary:	KDE Terminal Emulator
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	7c7297f44101d0765c9d843fc99a44d6
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Multimedia-devel >= %{qtver}
BuildRequires:	Qt5PrintSupport-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.20
BuildRequires:	kf5-extra-cmake-modules >= %{kf5ver}
BuildRequires:	kf5-kbookmarks-devel >= %{kf5ver}
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
BuildRequires:	libicu-devel >= 61.0
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires:	Qt5Core >= %{qtver}
Requires:	Qt5DBus >= %{qtver}
Requires:	Qt5PrintSupport >= %{qtver}
Requires:	Qt5Widgets >= %{qtver}
Requires:	kf5-kbookmarks >= %{kf5ver}
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

%description -l pl.UTF-8
Konsole jest emulatorem terminala.

Cechy

• Karty • Wiele profili • Monitoring ciszy i aktywności •
Zakładki • Szukanie • Zapisywanie danych wyjściowych

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{sr,zh_CN}

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_desktop_database_post

%postun
/sbin/ldconfig
%update_desktop_database_postun

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/konsolerc
%attr(755,root,root) %{_bindir}/konsole
%attr(755,root,root) %{_bindir}/konsoleprofile
%ghost %{_libdir}/libkonsoleprivate.so.1
%{_libdir}/libkonsoleprivate.so.*.*.*
%ghost %{_libdir}/libkonsoleapp.so.1
%{_libdir}/libkonsoleapp.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/konsolepart.so
%dir %{_libdir}/qt5/plugins/konsoleplugins
%attr(755,root,root) %{_libdir}/qt5/plugins/konsoleplugins/konsole_sshmanagerplugin.so
%{_datadir}/metainfo/org.kde.konsole.appdata.xml
%{_desktopdir}/org.kde.konsole.desktop
%{_datadir}/knotifications5/konsole.notifyrc
%{_datadir}/konsole
%{_datadir}/kservices5/konsolepart.desktop
%{_datadir}/kservicetypes5/terminalemulator.desktop
%{_datadir}/knsrcfiles/konsole.knsrc
%{_datadir}/qlogging-categories5/konsole.categories
%attr(755,root,root) %{_libdir}/qt5/plugins/konsoleplugins/konsole_quickcommandsplugin.so
%{_datadir}/kio/servicemenus/konsolerun.desktop
%attr(755,root,root)%{_libdir}/kconf_update_bin/konsole_globalaccel
%attr(755,root,root)%{_libdir}/kconf_update_bin/konsole_show_menubar
%{_datadir}/kconf_update/konsole.upd
%attr(755,root,root)%{_datadir}/kconf_update/konsole_add_hamburgermenu_to_toolbar.sh
%{zsh_compdir}/_konsole
%{_datadir}/kglobalaccel/org.kde.konsole.desktop
