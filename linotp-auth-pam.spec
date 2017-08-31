Summary:   LinOTP PAM module
Name:      linotp-auth-pam
Version:   2.9.1
Release:   1
License:   BSD (GPL)
Group:     System Environment/Base
URL:       https://github.com/LinOTP/linotp-auth-pam
Packager:  Shane Canon <scanon@lbl.gov>
Source0:   %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
PAM module for LinOTP.

%prep
%setup -q

%build
%configure
MAKEFLAGS=%{?_smp_mflags} %{__make}



%install
%make_install libdir=/%{_lib}/ DESTDIR=%{buildroot}

#%check
#%{__make} check
#
%files
%defattr(-, root, root)
/lib64/security/pam_linotp.so
# %doc AUTHORS Dockerfile LICENSE NEWS README* doc extra/cle6

%changelog
* Thu Aug 31 2017 Shane Canon <scanon@lbl.gov> - 2.9.1
- Initial RPM
