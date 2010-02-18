%define rname 	htmlize
%define name 	emacs-%{rname}
%define version 1.37
%define release  %mkrel 1

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
