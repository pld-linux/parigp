%include	/usr/lib/rpm/macros.perl
%define		pari_version		2.1.4
%define		gp2c_version		0.0.0pl12
%define		math_pari_version	2.010305
Summary:	Number Theory-oriented Computer Algebra System
Summary(pl):	Komputerowy system oblicze� algebraicznych zorientowany na metody teorii liczb
Name:		parigp
Version:	%{pari_version}
Release:	2
License:	GPL
Group:		Applications/Math
Source0:	ftp://megrez.math.u-bordeaux.fr/pub/pari/unix/pari-%{pari_version}.tgz
Source1:	ftp://megrez.math.u-bordeaux.fr/pub/pari/galdata.tgz
Source2:	ftp://megrez.math.u-bordeaux.fr/pub/pari/GP2C/gp2c-%{gp2c_version}.tar.gz
Source3:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Math/Math-Pari-%{math_pari_version}.tar.gz
Source4:	%{name}.desktop
Source5:	%{name}.png
Patch0:		%{name}-FHS.patch
Patch1:		%{name}-target_arch.patch
Patch2:		%{name}-termcap.patch
Patch3:		%{name}-arch.patch
Patch30:	Math-Pari-alpha.patch
Icon:		parigp.xpm
URL:		http://www.parigp-home.de/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	readline-devel >= 4.2
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	tetex
BuildRequires:	tetex-ams
BuildRequires:	tetex-dvips
BuildRequires:	tetex-fonts
BuildRequires:	tetex-pdftex
Requires:	pari = %{pari_version}
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
System PARI/GP jest przeznaczony do wydajnych oblicze� z zakresu
teorii liczb, ale zawiera r�wnie� inne przydatne funkcje. Jest nieco
spokrewniony z Komputerowymi Systemami Algebraicznymi, ale nie
identyczny, poniewa� traktuje wyra�enia symboliczne jako obiekty
matematyczne (macierze, wielomiany, szeregi itp.) a nie jako wyra�enia
same w sobie. Jest jednak cz�sto znacznie szybszy od innych KSA-�w a
ponadto zawiera wiele innych funkcji nie spotykanych gdzie indziej, a
przydatnych zw�aszcza w teorii liczb.

%package -n pari
Summary:	Shared PARI library (required by the parigp package)
Summary(pl):	Biblioteka wsp�dzielona PARI (wymagana przez pakiet parigp)
Group:		Libraries

%description -n pari
Shared PARI library. You need it to run PARI/GP.

%description -n pari -l pl
Biblioteka wsp�dzielona PARI. Potrzebujesz jej do uruchomienia
PARI/GP.

%package -n pari-devel
Summary:	Include files for PARI shared library
Summary(pl):	Pliki nag��wkowe do biblioteki wsp�dzielonej PARI
Group:		Development/Libraries
Requires:	pari = %{pari_version}

%description -n pari-devel
Include files for shared PARI library. You need them to use PARI
routines in you own programs.

%description -n pari-devel -l pl
Pliki nag��wkowe biblioteki wsp�dzielonej PARI. B�dziesz ich
potrzebowa�, je�eli b�dziesz chcia� wykorzystywa� procedury PARI w
swoich programach.

%package -n pari-static
Summary:	Static PARI library
Summary(pl):	Statyczna biblioteka PARI
Group:		Development/Libraries
Requires:	pari-devel = %{pari_version}

%description -n pari-static
Static PARI library. You need it to statically link your programs with
PARI.

%description -n pari-static -l pl
Biblioteka statyczna PARI. Potrzebujesz jej do konsolidowania
statycznego swoich program�w korzystaj�cych z biblioteki PARI.

%package demos
Summary:	Example PARI/GP scripts
Summary(pl):	Przyk�adowe skrypty pisane w j�zyku PARI/GP
Group:		Applications/Math
Requires:	%{name} = %{pari_version}

%description demos
Example PARI/GP scripts. You can write such programs on your own.

%description demos -l pl
Przyk�adowe skrypty pisane w j�zyku PARI/GP. Sam mo�esz takie napisa�.

%package galdata
Summary:	Galois data resolvents for PARI/GP
Summary(pl):	Reprezentacje danych Galois fla PARI/GP
Group:		Applications/Math
Requires:	%{name} = %{pari_version}

%description galdata
Galois data resolvents for PARI/GP.

%description galdata -l pl
Reprezentacje danych Galois do PARI/GP.

%package gp2c
Summary:	PARI/GP to C translator
Summary(pl):	Konwerter skrypt�w PARI/GP do j�zyka C
Group:		Development/Tools
Requires:	pari-devel

%description gp2c
PARI/GP to C translator. Use it to compile your own C programs which
use pari library, without necessarily being a C programmer.

%description gp2c -l pl
Konwerter skrypt�w PARI/GP do j�zyka C. Mo�na nim tworzy� w�asne
programy w C korzystaj�ce z biblioteki pari. Znajomo�� j�zyka C nie
jest wymagana.

%package -n xemacs-parigp-mode-pkg
Summary:	PARI/GP mode for Octave
Summary(pl):	Tryb edycji plik�w PARI/GP do XEmacsa
Group:		Applications/Editors/Emacs
Requires:	xemacs

%description -n xemacs-parigp-mode-pkg
PARI/GP editing mode for Xemacs.

%description -n xemacs-parigp-mode-pkg -l pl
Tryb edycji plik�w PARI/GP do Xemacsa.

%package -n perl-Math-Pari
Summary:	Math-Pari perl module
Summary(pl):	Modu� perla Math-Pari
Version:	%{math_pari_version}
Group:		Development/Languages/Perl

%description -n perl-Math-Pari
The PERL interface to the PARI part of GP/PARI

%description -n perl-Math-Pari -l pl
Interfejs perl-a do biblioteki PARI

%prep
%setup -q -n pari-%{pari_version} -a 2 -a 3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch30 -p0

%build
# pari & parigp
./Configure \
	--target=%{_target_cpu} \
	--prefix=%{_prefix} \
	--share-prefix=%{_datadir}

%{__make} all CFLAGS="%{rpmcflags} -DGCC_INLINE"
%{__make} doc
src/make_vi_tags src
%ifarch %{ix86}
ln -s Olinux-%{_target_cpu} Olinux-ix86
%endif

# gp2c
cd gp2c-%{gp2c_version}
ln -sf ../ pari
%{__autoconf}
%configure \
	--datadir=%{_datadir}/parigp
%{__make}
cd ..

# math-pari
cd Math-Pari-%{math_pari_version}
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"
# %{__make} test
 
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Scientific,%{_examplesdir}/parigp} \
	$RPM_BUILD_ROOT{%{_datadir}/parigp/galdata,%{_pixmapsdir}}

# parigp, pari & pari-devel
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install src/tags $RPM_BUILD_ROOT%{_datadir}/parigp/misc
install %{SOURCE4} $RPM_BUILD_ROOT%{_applnkdir}/Scientific
install %{SOURCE5} $RPM_BUILD_ROOT%{_pixmapsdir}

# pari-static
install Olinux-%{_target_cpu}/libpari.a $RPM_BUILD_ROOT%{_libdir}/libpari.a

# parigp-demos
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/parigp

# galdata
tar zxvf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/parigp/galdata/

# xemacs-parigp-mode-pkg
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/parigp-mode
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

# math-pari
cd Math-Pari-%{math_pari_version}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ..

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/pari.1
echo ".so gp.1" > $RPM_BUILD_ROOT%{_mandir}/man1/pari.1

%clean
rm -rf $RPM_BUILD_ROOT

%post   -n pari -p /sbin/ldconfig
%postun -n pari -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gp-2.1
%attr(755,root,root) %{_bindir}/gp
%attr(755,root,root) %{_bindir}/gphelp
%attr(755,root,root) %{_bindir}/tex2mail
%doc AUTHORS Announce* CHANGES COMPAT MACHINES NEW README TODO
%doc examples/Inputrc doc/refcard.ps
%dir %{_datadir}/parigp
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
%attr(755,root,root) %{_libdir}/*.so

%files -n pari-static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files demos
%defattr(644,root,root,755)
%doc examples/EXPLAIN
%{_examplesdir}/parigp

%files galdata
%defattr(644,root,root,755)
%{_datadir}/parigp/galdata

%files -n xemacs-parigp-mode-pkg
%defattr(644,root,root,755)
%doc emacs/pariemacs.txt
%{_datadir}/xemacs-packages/lisp/*

%files gp2c
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gp2c*
%doc gp2c-%{gp2c_version}/{AUTHORS,ChangeLog,NEWS,README}
%{_datadir}/parigp/gp2c

%files -n perl-Math-Pari
%defattr(644,root,root,755)
%doc Math-Pari-%{math_pari_version}/{Changes,README,TODO}
%{perl_sitearch}/Math/*
%dir %{perl_sitearch}/auto/Math/Pari
%{perl_sitearch}/auto/Math/Pari/Pari.bs
%attr(755,root,root) %{perl_sitearch}/auto/Math/Pari/Pari.so
%{_mandir}/man3/*
