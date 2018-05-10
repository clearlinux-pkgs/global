#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2AF9977BDA5E41B1 (shigio@gnu.org)
#
Name     : global
Version  : 6.6.2
Release  : 10
URL      : https://tamacom.com/global/global-6.6.2.tar.gz
Source0  : https://tamacom.com/global/global-6.6.2.tar.gz
Source99 : https://tamacom.com/global/global-6.6.2.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: global-bin
Requires: global-lib
Requires: global-data
Requires: global-doc
BuildRequires : emacs
BuildRequires : ncurses-dev
BuildRequires : sqlite-autoconf-dev

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
Requires: global-data

%description bin
bin components for the global package.


%package data
Summary: data components for the global package.
Group: Data

%description data
data components for the global package.


%package doc
Summary: doc components for the global package.
Group: Documentation

%description doc
doc components for the global package.


%package lib
Summary: lib components for the global package.
Group: Libraries
Requires: global-data

%description lib
lib components for the global package.


%prep
%setup -q -n global-6.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1518144663
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1518144663
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/gtags/vim74-gtags-cscope.patch

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/gtags/exuberant-ctags.so
/usr/lib64/gtags/pygments-parser.so
/usr/lib64/gtags/universal-ctags.so
/usr/lib64/gtags/user-custom.so
