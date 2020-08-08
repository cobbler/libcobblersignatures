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


Name:           libcobblersignatures
Version:        1596876389.b382a7d
Release:        0
Summary:        Cobbler Signatures Library
License:        GPL-2.0-or-later
URL:            https://github.com/cobbler/libcobblersignatures
Source:         libcobblersignatures-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  fdupes
Requires:       python3-PyInquirer
BuildArch:      noarch

%description
This library should be the interface for all applications using cobbler signatures.
Features are:
 - Create a cobbler signatures document from scratch
 - Modify existing cobbler signature documents
 - Read cobbler signatures document
 - Hand over structured data to other applications

%prep
%setup -q

%build
%py3_build

%install
%py3_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/%name

%files
%license LICENSE
%doc README.md
%{_bindir}/cobbler-manage-signatures
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*-py*.egg-info

%changelog
