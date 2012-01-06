
Name:       xcb-proto
Summary:    XCB protocol descriptions
Version:    1.6
Release:    0
Group:      Development/Libraries
License:    MIT
URL:        http://xcb.freedesktop.org/
Source0:    http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.gz
Source101:  xcb-proto-rpmlintrc
Requires:   pkgconfig
BuildRequires:  python-devel

%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}


%build

%reconfigure --disable-shared

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install







%files
%defattr(-,root,root,-)
%doc COPYING NEWS README TODO doc/xml-xcb.txt
%{_libdir}/pkgconfig/xcb-proto.pc
%dir %{_datadir}/xcb/
%{_datadir}/xcb/*.xsd
%{_datadir}/xcb/*.xml
%dir %{python_sitearch}/xcbgen/
%{python_sitearch}/xcbgen/*.py*


