
%define		qtver	4.5.0

Summary:	qzion
Summary(pl.UTF-8):	qzion
Name:		qzion
Version:	0.4.0
Release:	0.git.1
License:	GPL v2
Group:		X11/Libraries
#Source0:	http://dev.openbossa.org/qedje/downloads/source/%{name}/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}-git.tar.gz
# Source0-md5:	628ef8996686e16131973d8f08d54d49
Patch0:	%{name}-python.patch
URL:		http://dev.openbossa.org/trac/qzion
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtWebKit-devel >= %{qtver}
BuildRequires:	eet-devel
BuildRequires:	pkgconfig
BuildRequires:	python-PyQt4-devel
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qzion

%description -l pl.UTF-8
qzion

%package devel
Summary:	Header files for qzion library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki qzion
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	python-sip-devel

%description devel
Header files for qzion library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki qzion.

%prep
%setup -q -n %{name}-%{version}-git
%patch -p1

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqzion.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqzion.so.?
%dir %{py_sitedir}/qzion
%{py_sitedir}/qzion/__init__.py
%{py_sitedir}/qzion/__init__.pyc
%{py_sitedir}/qzion/qzion.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqzion.so
%{_includedir}/*.h
%{_pkgconfigdir}/qzion.pc
%{_datadir}/sip/qzion
