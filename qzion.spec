
%define		qtver	4.4.3

Summary:	qzion
Summary(pl.UTF-8):	qzion
Name:		qzion
Version:	0.3.0
Release:	0.1
License:	GPL v2
Group:		X11/Libraries
Source0:	http://dev.openbossa.org/qedje/downloads/source/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	293cb0a9783f7111d97838fea8b6970a
URL:		http://dev.openbossa.org/trac/qzion
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtWebKit-devel >= %{qtver}
BuildRequires:	eet-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qzion

%description -l pl.UTF-8
qzion

%package devel
Summary:        Header files for qzion library
Summary(pl.UTF-8):      Pliki nag�~B처wkowe biblioteki qzion
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
Header files for qzion library.

%description devel -l pl.UTF-8
Pliki nag�~B처wkowe biblioteki qzion.

%prep
%setup -q

%build
qmake-qt4 \
	PREFIX=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqzion.so.*.*.*
%attr(755,root,root) %{_libdir}/libqzion.prl
%attr(755,root,root) %ghost %{_libdir}/libqzion.so.?
%attr(755,root,root) %ghost %{_libdir}/libqzion.so.?.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqzion.so
%{_includedir}/*.h
%{_pkgconfigdir}/qzion.pc
