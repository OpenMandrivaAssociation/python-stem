# Created by pyp2rpm-3.3.3
%global pypi_name stem

%bcond_with tests

Name:           python-%{pypi_name}
Version:        1.8.2
Release:        2
Summary:        Python controller library for Tor
Group:          Development/Python
License:        LGPLv3
URL:            https://stem.torproject.org/
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildSystem:  python
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
 # for tests
 %if %{with tests}
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pyflakes)
BuildRequires:  python3dist(pycodestyle)
BuildRequires:  python3dist(tox)
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(pynacl)
%endif

%description
Stem is a Python controller library for Tor. With it you can use Tor's control
protocol to script against the Tor process, or build things such as Nyx.

%files
%license LICENSE
%doc README.md
%{_bindir}/tor-prompt
%{python_sitelib}/stem-%{version}-py*.*.egg-info
%{python_sitelib}/stem/
