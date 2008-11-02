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
BuildRequires:	eet-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qzion

%description -l pl.UTF-8
qzion

%prep
%setup -q

%build
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/kde4/plasma_applet_wifi_signal.so
