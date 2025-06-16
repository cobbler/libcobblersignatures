#
# spec file for package libcobblersignatures
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%{?sle15_python_module_pythons}
%define pythons python3
%define parent_tag 0.1.0
Name:           libcobblersignatures
Version:        0.1.0+git40
Release:        0
Summary:        Cobbler Signatures Library
License:        GPL-2.0-or-later
URL:            https://github.com/cobbler/libcobblersignatures
Source:         libcobblersignatures-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
# SECTION tests
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pytest-cov}
#
BuildRequires:  fdupes
# TODO: remove dependencies that are not in Factory
# Requires:     python-PyInquirer
# Requires:     python-questionary
BuildArch:      noarch

%description
This library should be the interface for all applications using cobbler signatures.
Features are:
 - Create a cobbler signatures document from scratch
 - Modify existing cobbler signature documents
 - Read cobbler signatures document
 - Hand over structured data to other applications

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{python_sitelib}/%{name}
%python_expand rm -rf %{buildroot}%{python_sitelib}/tests

%check
# disable test that requires network for OBS build
%pytest -k "not test_importsignatures_url"

%files
%license LICENSE
%doc README.md
%{_bindir}/cobbler-manage-signatures
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{parent_tag}.dist-info

%changelog
