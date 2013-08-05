# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       nemo-qml-plugin-contacts

# >> macros
# << macros

Summary:    Nemo QML contacts plugin
Version:    0.0.0
Release:    1
Group:      System/Libraries
License:    BSD
URL:        https://github.com/nemomobile/nemo-qml-plugin-contacts
Source0:    %{name}-%{version}.tar.bz2
Source100:  nemo-qml-plugin-contacts.yaml
BuildRequires:  pkgconfig(QtCore) >= 4.7.0
BuildRequires:  pkgconfig(QtDeclarative)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtContacts)
BuildRequires:  pkgconfig(qtcontacts-sqlite-extensions) >= 0.1.1
BuildRequires:  pkgconfig(contactcache) >= 0.0.6
Provides:   nemo-qml-plugins-contacts > 0.3.26
Obsoletes:   nemo-qml-plugins-contacts <= 0.3.26

%description
%{summary}.

%package tools
Summary:    Development tools for qmlcontacts
License:    BSD
Group:      Applications/System

%description tools
%{summary}.

%package tests
Summary:    QML contacts plugin tests
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description tests
%{summary}.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_libdir}/qt4/imports/org/nemomobile/contacts/libnemocontacts.so
%{_libdir}/qt4/imports/org/nemomobile/contacts/qmldir
# >> files
# << files

%files tools
%defattr(-,root,root,-)
%{_bindir}/vcardconverter
# >> files tools
# << files tools

%files tests
%defattr(-,root,root,-)
/opt/tests/nemo-qml-plugins/contacts/*
# >> files tests
# << files tests
