Name:    xcb-proto
Summary: XCB protocol descriptions
Version: 1.10.1
Release: 1
Group:   Development/Libraries
License: MIT
URL:     http://xcb.freedesktop.org/
Source0: %{name}-%{version}.tar.gz
#Source101:  xcb-proto-rpmlintrc

BuildRequires:  python-devel

Requires:  pkgconfig

# some file to be intalled can be ignored when rpm generates packages
#%define _unpackaged_files_terminate_build 0

%description
Description: %{summary}
XCB is a project to enable efficient language bindings to the X11 protocol.
This package contains the protocol descriptions themselves.  Language
bindings use these protocol descriptions to generate code for marshalling
the protocol.

%prep
%setup -q -n %{name}-%{version}

%build

./autogen.sh
%reconfigure --disable-shared

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%remove_docs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/xcb-proto.pc
%dir %{_datadir}/xcb/
%{_datadir}/xcb/*.xsd
%{_datadir}/xcb/*.xml
%dir %{python_sitearch}/xcbgen/
%{python_sitearch}/xcbgen/*.py*


