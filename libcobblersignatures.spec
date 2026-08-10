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

%if 0%{?suse_version}
%{?single_pythons_311plus}
%endif

Name:           libcobblersignatures
Version:        0.3.1
Release:        0
Summary:        Cobbler Signatures Library
License:        GPL-2.0-or-later
URL:            https://github.com/cobbler/libcobblersignatures
Source:         libcobblersignatures-%{version}.tar.gz
BuildRequires:  git-core
BuildRequires:  python3-devel
%if 0%{?suse_version}
BuildRequires:  python-rpm-macros
%endif
%if 0%{?fedora} || 0%{?rhel}
# Provides %%pyproject_wheel / %%pyproject_install, the Fedora/RHEL equivalent
# of SUSE's python-rpm-macros pyproject buildsystem macros
BuildRequires:  pyproject-rpm-macros
%endif
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
# SECTION tests
BuildRequires:  python3-pytest
BuildRequires:  python3-coverage
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-questionary
#
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif
%if 0%{?rhel}
# We need these to build this properly, and OBS doesn't pull them in by default for EPEL
BuildRequires:  epel-rpm-macros
%endif
Requires:       python3-questionary
BuildArch:      noarch
%if 0%{?fedora} || 0%{?rhel}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Automatically-generated-dependencies
# Disable it because it trips over python3-cheetah
%{?python_disable_dependency_generator}
%endif

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
if [ -d "%{_sourcedir}/%{name}-%{version}/.git" ]; then
    cp -r %{_sourcedir}/%{name}-%{version}/.git %{_builddir}/%{name}-%{version}
fi
%pyproject_wheel

%install
%pyproject_install
%if 0%{?suse_version}
%fdupes %{buildroot}%{python3_sitelib}/%{name}
%endif
rm -rf %{buildroot}%{python3_sitelib}/tests

%check
# disable test that requires network for OBS build
%pytest -k "not test_importsignatures_url"

%files
%license LICENSE
%doc README.md
%{_bindir}/cobbler-manage-signatures
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-*.dist-info

%changelog
