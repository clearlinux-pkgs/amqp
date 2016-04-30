#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : amqp
Version  : 1.4.9
Release  : 26
URL      : https://pypi.python.org/packages/source/a/amqp/amqp-1.4.9.tar.gz
Source0  : https://pypi.python.org/packages/source/a/amqp/amqp-1.4.9.tar.gz
Summary  : Low-level AMQP client for Python (fork of amqplib)
Group    : Development/Tools
License  : LGPL-2.1
Requires: amqp-python
BuildRequires : amqp
BuildRequires : coverage
BuildRequires : linecache2
BuildRequires : nose
BuildRequires : nose-cover3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : traceback2
BuildRequires : unittest2

%description
generate_skeleton_0_8.py was used to create an initial Python
module from the AMQP 0.8 spec file.

%package python
Summary: python components for the amqp package.
Group: Default

%description python
python components for the amqp package.


%prep
%setup -q -n amqp-1.4.9

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 -v funtests/ || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
