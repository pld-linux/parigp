%define 	gp2c_version 0.0.0pl6
Summary:	Number Theory-oriented Computer Algebra System
Summary(pl):	Komputerowy system obliczeñ algebraicznych zorientowany na metody teorii liczb
Name:		parigp
Version:	2.1.1
Release:	4
License:	GPL
Group:		Applications/Math
Group(de):	Applikationen/Mathematik
Group(pl):	Aplikacje/Matematyczne
Source0:	ftp://megrez.math.u-bordeaux.fr/pub/pari/unix/pari-%{version}.tgz
Source1:	ftp://megrez.math.u-bordeaux.fr/pub/pari/galdata.tgz
Source2:	ftp://megrez.math.u-bordeaux.fr/pub/pari/GP2C/gp2c-%{gp2c_version}.tar.gz
Source3:	%{name}.desktop
Source4:	%{name}.xpm
Patch0:		%{name}-FHS.patch
Patch1:		%{name}-target_arch.patch
Patch2:		%{name}-emacsfix.patch
Patch3:		%{name}-CLK_TCK.patch
Icon:		parigp.xpm
URL:		http://www.parigp-home.de/
BuildRequires:	XFree86-devel
BuildRequires:	perl
BuildRequires:	readline-devel >= 4.2
BuildRequires:	tetex
BuildRequires:	tetex-ams
BuildRequires:	tetex-dvips
BuildRequires:	tetex-fonts
BuildRequires:	tetex-pdftex
Requires:	pari = %{version}
Requires:	xdvi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PARI/GP is a package which is aimed at efficient computations in
number theory, but also contains a large number of other useful
functions. It is somewhat related to a Computer Algebra System, but is
not really one since it treats symbolic expressions as mathematical
entities such as matrices, polynomials, series, etc..., and not as
expressions per se. However it is often much faster than other CAS,
and contains a large number of specific functions not found elsewhere,
essentially for use in number theory.

%description -l pl
System PARI/GP jest przeznaczony do wydajnych obliczeñ z zakresu
teorii liczb, ale zawiera równie¿ inne przydatne funkcje. Jest nieco
spokrewniony z Komputerowymi Systemami Algebraicznymi, ale nie
identyczny, poniewa¿ traktuje wyra¿enia symboliczne jako obiekty
matematyczne (macierze, wielomiany, szeregi itp.) a nie jako wyra¿enia
same w sobie. Jest jednak czêsto znacznie szybszy od innych KSA-ów a
ponadto zawiera wiele innych funkcji nie spotykanych gdzie indziej, a
przydatnych zw³aszcza w teorii liczb.

%package -n pari
Summary:	Shared PARI library (required by the parigp package)
Summary(pl):	Biblioteka wspó³dzielona PARI (wymagana przez pakiet parigp)
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki

%description -n pari
Shared PARI library. You need it to run PARI/GP.

%description -l pl -n pari
Biblioteka wspó³dzielona PARI. Potrzebujesz jej do uruchomienia
PARI/GP.

%package -n pari-devel
Summary:	Include files for PARI shared library
Summary(pl):	Pliki nag³ówkowe do biblioteki wspó³dzielonej PARI
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	pari = %{version}

%description -n pari-devel
Include files for shared PARI library. You need them to use PARI
routines in you own programs.

%description -l pl -n pari-devel 
Pliki nag³ówkowe biblioteki wspó³dzielonej PARI. Bêdziesz ich
potrzebowa³, je¿eli bêdziesz chcia³ wykorzystywaæ procedury PARI w
swoich programach.

%package -n pari-static
Summary:	Static PARI library
Summary(pl):	Statyczna biblioteka PARI
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	pari-devel = %{version}

%description -n pari-static
Static PARI library. You need it to statically link your programs with
PARI.

%description -l pl -n pari-static
Biblioteka statyczna PARI. Potrzebujesz jej do konsolidowania
statycznego swoich programów korzystaj±cych z biblioteki PARI.

%package demos
Summary:	Example PARI/GP scripts
Summary(pl):	Przyk³adowe skrypty pisane w jêzyku PARI/GP
Group:		Applications/Math
Group(de):	Applikationen/Mathematik
Group(pl):	Aplikacje/Matematyczne
Requires:	%{name} = %{version}

%description demos
Example PARI/GP scripts. You can write such programs on your own.

%description demos -l pl
Przyk³adowe skrypty pisane w jêzyku PARI/GP. Sam mo¿esz takie napisaæ.

%package galdata
Summary:	Galois data resolvents for PARI/GP
Group:		Applications/Math
Group(de):	Applikationen/Mathematik
Group(pl):	Aplikacje/Matematyczne
Requires:	%{name} = %{version}

%description galdata
Galois data resolvents for PARI/GP.

%description galdata -l pl
Reprezentacje danych Galois do PARI/GP.

%package -n xemacs-parigp-mode-pkg
Summary:	PARI/GP mode for Octave
Summary(pl):	Tryb edycji plików PARI/GP do XEmacsa
Group:		Applications/Editors/Emacs
Group(de):	Applikationen/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Requires:	xemacs

%package gp2c
Summary:	PARI/GP to C translator
Summary(pl):	Konwerter skryptów PARI/GP do jêzyka C
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Requires:	pari-devel

%description gp2c
PARI/GP to C translator. Use it to compile your own C programs which
use pari library, without necessarily being a C programmer.

%description gp2c -l pl
Konwerter skryptów PARI/GP do jêzyka C. Mo¿na nim tworzyæ w³asne
programy w C korzystaj±ce z biblioteki pari. Znajomo¶æ jêzyka C nie
jest wymagana.

%description -n xemacs-parigp-mode-pkg
PARI/GP editing mode for Xemacs.

%description -l pl -n xemacs-parigp-mode-pkg
Tryb edycji plików PARI/GP do Xemacsa.

%prep
%setup0 -q -n pari-%{version} -a 2 gp2c-%{gp2c_version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build

# pari & parigp
./Configure \
	--target=%{_target_cpu} \
	--prefix=%{_prefix} \
	--share-prefix=%{_datadir}

%{__make} all CFLAGS="%{rpmcflags} -DGCC_INLINE"
%{__make} doc
src/make_vi_tags src

# gp2c
cd gp2c-%{gp2c_version}
ln -s ../ pari
%configure \
	--datadir=%{_datadir}/parigp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT{%{_applnkdir}/Scientific,%{_examplesdir}/parigp} \
	$RPM_BUILD_ROOT{%{_datadir}/parigp/galdata,%{_pixmapsdir}}

# parigp, pari & pari-devel
%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{__install} src/tags $RPM_BUILD_ROOT%{_datadir}/parigp/misc
%{__install} %{SOURCE3} $RPM_BUILD_ROOT%{_applnkdir}/Scientific
%{__install} %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

# pari-static
%{__install} Olinux-%{_target_cpu}/libpari.a $RPM_BUILD_ROOT%{_libdir}/libpari.a

# parigp-demos
%{__install} examples/* $RPM_BUILD_ROOT%{_examplesdir}/parigp

# galdata
tar zxvf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/parigp/galdata/

# xemacs-parigp-mode-pkg
%{__install} -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/parigp-mode
cp -a emacs/*.el $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/parigp-mode
cat <<EOF >$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/parigp-mode/auto-autoloads.el
(autoload 'gp-mode "pari" nil t)
(autoload 'gp-script-mode "pari" nil t)
(autoload 'gp "pari" nil t)
(autoload 'gpman "pari" nil t)
EOF

# gp2c
cd gp2c-%{gp2c_version}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

gzip -9nf Announce* AUTHORS CHANGES COMPAT CVS.txt INSTALL.tex INSTALL.txt \
	MACHINES NEW README README.DOS TODO emacs/pariemacs.txt \
	gp2c-%{gp2c_version}/NEWS gp2c-%{gp2c_version}/README \
	gp2c-%{gp2c_version}/ChangeLog gp2c-%{gp2c_version}/AUTHORS \
	examples/EXPLAIN examples/Inputrc

%post   -n pari -p /sbin/ldconfig
%postun -n pari -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gp-2.1
%attr(755,root,root) %{_bindir}/gp
%attr(755,root,root) %{_bindir}/gphelp
%attr(755,root,root) %{_bindir}/tex2mail
%doc *.gz examples/Inputrc.gz doc/refcard.ps doc/*.gz
%dir %{_datadir}/parigp
%{_datadir}/parigp/galdata
%{_datadir}/parigp/doc
%{_datadir}/parigp/misc
%{_mandir}/man1/*
%{_applnkdir}/Scientific/*
%{_pixmapsdir}/*

%files -n pari
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*

%files -n pari-devel
%defattr(644,root,root,755)
%{_includedir}/pari

%files -n pari-static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files demos
%defattr(644,root,root,755)
%doc examples/EXPLAIN.gz
%{_examplesdir}/parigp

%files galdata
%defattr(644,root,root,755)
%{_datadir}/parigp/galdata/*

%files -n xemacs-parigp-mode-pkg
%defattr(644,root,root,755)
%doc emacs/*.gz
%{_datadir}/xemacs-packages/lisp/*

%files gp2c
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gp2c
%doc gp2c-%{gp2c_version}/*.gz
%{_datadir}/parigp/gp2c
