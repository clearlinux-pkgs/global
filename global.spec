#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v13
# autospec commit: dc0ff31
#
# Source0 file verified with key 0x2AF9977BDA5E41B1 (shigio@gnu.org)
#
Name     : global
Version  : 6.6.13
Release  : 29
URL      : https://mirrors.kernel.org/gnu/global/global-6.6.13.tar.gz
Source0  : https://mirrors.kernel.org/gnu/global/global-6.6.13.tar.gz
Source1  : https://mirrors.kernel.org/gnu/global/global-6.6.13.tar.gz.sig
Source2  : 2AF9977BDA5E41B1.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: global-bin = %{version}-%{release}
Requires: global-data = %{version}-%{release}
Requires: global-info = %{version}-%{release}
Requires: global-lib = %{version}-%{release}
Requires: global-license = %{version}-%{release}
Requires: global-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : emacs
BuildRequires : file
BuildRequires : gnupg
BuildRequires : ncurses-dev
BuildRequires : sqlite-autoconf-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
___________________________________
|      |  |  |     |  _  |     |  |
|  |___|  |  |  |  |    _|  |  |  |    GNU GLOBAL source code tagging system
|  |   |  |  |  |  |     |     |  |
|  ~~  |   ~~|     |  ~  |  |  |   ~~|          for all hackers.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

%package bin
Summary: bin components for the global package.
Group: Binaries
Requires: global-data = %{version}-%{release}
Requires: global-license = %{version}-%{release}

%description bin
bin components for the global package.


%package data
Summary: data components for the global package.
Group: Data

%description data
data components for the global package.


%package info
Summary: info components for the global package.
Group: Default

%description info
info components for the global package.


%package lib
Summary: lib components for the global package.
Group: Libraries
Requires: global-data = %{version}-%{release}
Requires: global-license = %{version}-%{release}

%description lib
lib components for the global package.


%package license
Summary: license components for the global package.
Group: Default

%description license
license components for the global package.


%package man
Summary: man components for the global package.
Group: Default

%description man
man components for the global package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2AF9977BDA5E41B1' gpg.status
%setup -q -n global-6.6.13
cd %{_builddir}/global-6.6.13
pushd ..
cp -a global-6.6.13 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1719932766
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1719932766
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/global
cp %{_builddir}/global-%{version}/COPYING %{buildroot}/usr/share/package-licenses/global/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/global-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/global/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9 || :
cp %{_builddir}/global-%{version}/libltdl/COPYING.LIB %{buildroot}/usr/share/package-licenses/global/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/global
/V3/usr/bin/gozilla
/V3/usr/bin/gtags
/V3/usr/bin/gtags-cscope
/V3/usr/bin/htags
/usr/bin/global
/usr/bin/globash
/usr/bin/gozilla
/usr/bin/gtags
/usr/bin/gtags-cscope
/usr/bin/htags
/usr/bin/htags-server

%files data
%defattr(-,root,root,-)
/usr/share/gtags/AUTHORS
/usr/share/gtags/BUILD_TOOLS
/usr/share/gtags/COPYING
/usr/share/gtags/COPYING.LIB
/usr/share/gtags/ChangeLog
/usr/share/gtags/DONORS
/usr/share/gtags/FAQ
/usr/share/gtags/INSTALL
/usr/share/gtags/LICENSE
/usr/share/gtags/NEWS
/usr/share/gtags/PLUGIN_HOWTO
/usr/share/gtags/PLUGIN_HOWTO.pygments
/usr/share/gtags/PLUGIN_HOWTO.universal-ctags
/usr/share/gtags/README
/usr/share/gtags/README.PATCHES
/usr/share/gtags/SERVERSIDE_HOWTO
/usr/share/gtags/THANKS
/usr/share/gtags/completion.cgi
/usr/share/gtags/dot_htaccess
/usr/share/gtags/elvis-2.2_0.patch
/usr/share/gtags/elvis.rc
/usr/share/gtags/geco.rc
/usr/share/gtags/global.cgi
/usr/share/gtags/globash.rc
/usr/share/gtags/gtags-cscope.vim
/usr/share/gtags/gtags.conf
/usr/share/gtags/gtags.el
/usr/share/gtags/gtags.pl
/usr/share/gtags/gtags.vim
/usr/share/gtags/icons/back.png
/usr/share/gtags/icons/bottom.png
/usr/share/gtags/icons/c.png
/usr/share/gtags/icons/dir.png
/usr/share/gtags/icons/first.png
/usr/share/gtags/icons/help.png
/usr/share/gtags/icons/index.png
/usr/share/gtags/icons/last.png
/usr/share/gtags/icons/left.png
/usr/share/gtags/icons/n_bottom.png
/usr/share/gtags/icons/n_first.png
/usr/share/gtags/icons/n_last.png
/usr/share/gtags/icons/n_left.png
/usr/share/gtags/icons/n_right.png
/usr/share/gtags/icons/n_top.png
/usr/share/gtags/icons/pglobe.png
/usr/share/gtags/icons/right.png
/usr/share/gtags/icons/text.png
/usr/share/gtags/icons/top.png
/usr/share/gtags/jquery/images/file.png
/usr/share/gtags/jquery/images/folder-closed.png
/usr/share/gtags/jquery/images/folder.png
/usr/share/gtags/jquery/images/minus.png
/usr/share/gtags/jquery/images/plus.png
/usr/share/gtags/jquery/images/treeview-black-line.png
/usr/share/gtags/jquery/images/treeview-black.png
/usr/share/gtags/jquery/images/treeview-default-line.png
/usr/share/gtags/jquery/images/treeview-default.png
/usr/share/gtags/jquery/images/treeview-famfamfam-line.png
/usr/share/gtags/jquery/images/treeview-famfamfam.png
/usr/share/gtags/jquery/images/treeview-gray-line.png
/usr/share/gtags/jquery/images/treeview-gray.png
/usr/share/gtags/jquery/images/treeview-red-line.png
/usr/share/gtags/jquery/images/treeview-red.png
/usr/share/gtags/jquery/jquery.js
/usr/share/gtags/jquery/jquery.suggest.css
/usr/share/gtags/jquery/jquery.suggest.js
/usr/share/gtags/jquery/jquery.treeview.css
/usr/share/gtags/jquery/jquery.treeview.js
/usr/share/gtags/jscode_suggest
/usr/share/gtags/jscode_treeview
/usr/share/gtags/script/elvis-global
/usr/share/gtags/script/global-client
/usr/share/gtags/script/gtags-client
/usr/share/gtags/script/htags-client
/usr/share/gtags/script/less-global
/usr/share/gtags/script/maps2conf.pl
/usr/share/gtags/script/pygments_parser.py
/usr/share/gtags/style.css
/usr/share/gtags/uctags-scheme.c-diff
/usr/share/gtags/vim74-gtags-cscope.patch

%files info
%defattr(0644,root,root,0755)
/usr/share/info/global.info

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/gtags/exuberant-ctags.so
/V3/usr/lib64/gtags/pygments-parser.so
/V3/usr/lib64/gtags/universal-ctags.so
/V3/usr/lib64/gtags/user-custom.so
/usr/lib64/gtags/exuberant-ctags.so
/usr/lib64/gtags/pygments-parser.so
/usr/lib64/gtags/universal-ctags.so
/usr/lib64/gtags/user-custom.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/global/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/global/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/global/e7d563f52bf5295e6dba1d67ac23e9f6a160fab9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/global.1
/usr/share/man/man1/globash.1
/usr/share/man/man1/gozilla.1
/usr/share/man/man1/gtags-cscope.1
/usr/share/man/man1/gtags.1
/usr/share/man/man1/htags-server.1
/usr/share/man/man1/htags.1
/usr/share/man/man5/gtags.conf.5
