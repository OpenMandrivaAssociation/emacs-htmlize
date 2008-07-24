%define rname 	htmlize
%define name 	emacs-%rname
%define version 1.16
%define release  %mkrel 4

Summary: 	HTML-ize font-lock buffers
Name: 		%name
Version:	%version
Release: 	%release
Epoch:		0
Url:		http://fly.srk.fer.hr/~hniksic/emacs/
Source0: 	%url%rname.el.bz2
License: 	GPL
Group: 		Editors
BuildRequires:  emacs
BuildArch:	noarch
BuildRoot: 	%_tmppath/%name-buildroot

%description
This package analyzes the text properties of the buffer and converts
them, along with the text, to HTML.

%prep
%setup -T -q -c
bzcat %SOURCE0 > emacs-%rname.el
cat > %rname.el << EOF
;; -*- Mode: Emacs-Lisp -*-

(if (string-match "GNU Emacs" (version)) (autoload '%rname-buffer "emacs-%rname" nil t))
(if (string-match "GNU Emacs" (version)) (autoload '%rname-region "emacs-%rname" nil t))
(if (string-match "GNU Emacs" (version)) (autoload '%rname-file "emacs-%rname" nil t))
(if (string-match "GNU Emacs" (version)) (autoload '%rname-many-files "emacs-%rname" nil t))
(if (string-match "GNU Emacs" (version)) (autoload '%rname-many-files-dired "emacs-%rname" nil t))
EOF

%build
emacs -batch -q -no-site-file -f batch-byte-compile emacs-%rname.el 

%install
%__rm -rf $RPM_BUILD_ROOT

%__mkdir_p %buildroot%_datadir/emacs/site-lisp
%__install -m 644 emacs-%rname.el %buildroot/%_datadir/emacs/site-lisp
%__install -m 644 emacs-%rname.elc %buildroot/%_datadir/emacs/site-lisp

%__mkdir -p %buildroot%_sysconfdir/emacs/site-start.d
%__install -m 644 %rname.el %buildroot%_sysconfdir/emacs/site-start.d

%clean
%__rm -rf %buildroot

%files
%defattr(0644,root,root,0755)
%config(noreplace) %_sysconfdir/emacs/site-start.d/%rname.el
%_datadir/emacs/site-lisp/emacs-%rname.el
%_datadir/emacs/site-lisp/emacs-%rname.elc

