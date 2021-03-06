Name:           memleax
Version:        1.0.2
Release:        1%{?dist}
Summary:        Debugs memory leak of a running process

License:        GPLv2
URL:            http://wubingzheng.github.io/memleax/
Source0:        https://github.com/WuBingzheng/memleax/archive/v1.0.2.tar.gz

BuildRequires:  libdwarf-devel, elfutils-libelf-devel, libunwind-devel

ExcludeArch:    ARM-hfp, x86

%description
Memleax debugs memory leak of a running process by attaching it.
It is very convenient to use, and suitable for production environment.
There is no need to recompile the program or restart the target process.


%prep
%setup -q


%build
./configure
make


%install
make install DESTDIR=%{buildroot}


%files
%{_bindir}/memleax
%{_mandir}/man1/memleax.1*


%changelog
* Sat Jan 28 2017 Wu Bingzheng <wubingzheng@gmail.com> - 1.0.2-1.el7.centos
- update README.md, and add man page
