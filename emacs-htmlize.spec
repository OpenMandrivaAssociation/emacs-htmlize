%define rname 	htmlize
%define name 	emacs-%{rname}
%define version 1.37
%define release  3

Summary: 	HTML-ize font-lock buffers
Name: 		%{name}
Version:	%{version}
Release: 	%{release}
Epoch:		0
Group: 		Editors
Url:		http://fly.srk.fer.hr/~hniksic/emacs/
Source0: 	%{url}%{rname}.el.lzma
License: 	GPLv2+
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:  emacs

%description
This package converts text and associated decorations in an emacs
buffer to HTML.

%prep
%setup -T -q -c %{rname}-%{version}
cp -f %SOURCE0 .
unlzma %{rname}.el.lzma
cat > %{rname}-start.el << EOF
;; -*- Mode: Emacs-Lisp -*-

(if (string-match "GNU Emacs" (version)) (autoload '%rname-buffer "%{rname}" nil t))
(if (string-match "GNU Emacs" (version)) (autoload '%rname-region "%{rname}" nil t))
(if (string-match "GNU Emacs" (version)) (autoload '%rname-file "%{rname}" nil t))
(if (string-match "GNU Emacs" (version)) (autoload '%rname-many-files "%{rname}" nil t))
(if (string-match "GNU Emacs" (version)) (autoload '%rname-many-files-dired "%{rname}" nil t))
EOF

%build
emacs -batch -q -no-site-file -f batch-byte-compile %{rname}.el 

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%_datadir/emacs/site-lisp
%__install -m 644 %{rname}.el %{buildroot}/%{_datadir}/emacs/site-lisp
%__install -m 644 %{rname}.elc %{buildroot}/%{_datadir}/emacs/site-lisp

%__mkdir -p %{buildroot}%_sysconfdir/emacs/site-start.d
%__install -m 644 %{rname}-start.el %{buildroot}%{_sysconfdir}/emacs/site-start.d/%{rname}.el

%clean
%__rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/%{rname}.el
%{_datadir}/emacs/site-lisp/%{rname}.el*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0:1.37-2mdv2011.0
+ Revision: 610355
- rebuild

* Fri Feb 19 2010 Lev Givon <lev@mandriva.org> 0:1.37-1mdv2010.1
+ Revision: 507937
- Update to 1.37.
  Don't rename file (#57106).

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0:1.16-5mdv2010.0
+ Revision: 428560
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0:1.16-4mdv2009.0
+ Revision: 244729
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0:1.16-2mdv2008.1
+ Revision: 124571
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import emacs-htmlize


* Fri Apr 29 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.16-2mdk
- rebuild for new emacs

* Fri Apr 22 2004 David Walluck <walluck@mandrake.org> 0:1.16-1mdk
- 1.16
- new %%_sysconfdir/emacs/site-start.d/%%rname.el
- spec cleanup

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.67-6mdk
- rebuild

* Tue Jan 21 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.67-5mdk
- rebuild for latest emacs

* Mon Sep  9 2002 Arnaud Desmons <adesmons@mandrakesoft.com> 0.67-4mdk
- added packager name

* Fri Jun 21 2002 Götz Waschk <waschk@linux-mandrake.com> 0.67-3mdk
- buildrequires emacs-bin

* Thu Jun 20 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.67-2mdk
- fix %%prep
- bzip %%{SOURCE0}
- fix Buildrequires (emacs is in emacs-X11)
- BuildArch noarch

* Sat Jun 01 2002 Yves Duret <yduret@mandrakesoft.com> 0.67-1mdk
- version 0.67.
- fix build (install -D does not work the same way).
- add url.
- s#Copyright#License#.
- buildrequires to perl-base.

* Tue May 29 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.60-2mdk
- Correct cut&past (thnks: Stefan Siegel
  <siegel@informatik.uni-kl.de>).

* Tue May 29 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.60-1mdk
- First version.

# end of file
