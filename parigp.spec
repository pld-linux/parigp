#
# Conditional build:
%bcond_without	tex	# don't build tex documentation
#
%include	/usr/lib/rpm/macros.perl
%define		pari_version		2.3.5
%define		gp2c_version		0.0.5pl9
%define		math_pari_version	2.01080604
Summary:	Number Theory-oriented Computer Algebra System
Summary(pl.UTF-8):	Komputerowy system obliczeń algebraicznych zorientowany na metody teorii liczb
Name:		parigp
Version:	%{pari_version}
Release:	0.1
License:	GPL
Group:		Applications/Math
Source0:	ftp://megrez.math.u-bordeaux.fr/pub/pari/unix/pari-%{pari_version}.tar.gz
# Source0-md5:	6077c6db56fdd32e39a06a9bf320e1f7
Source1:	ftp://megrez.math.u-bordeaux.fr/pub/pari/galdata.tgz
# Source1-md5:	25eab5f9dfdb8715b9ace8cd68210425
Source2:	ftp://megrez.math.u-bordeaux.fr/pub/pari/GP2C/gp2c-%{gp2c_version}.tar.gz
# Source2-md5:	746811f01af37b463a4bf3e981e5ea55
Source3:	http://www.cpan.org/modules/by-module/Math/Math-Pari-%{math_pari_version}.tar.gz
# Source3-md5:	27f5999671fe2a29cfd2e8c8a1f9308e
Source4:	%{name}.desktop
Source5:	%{name}.png
Patch2:		%{name}-termcap.patch
Patch3:		%{name}-arch.patch
Patch6:		%{name}-no-proccpuinfo.patch
Patch7:		perl-Math-Pari-crash-workaround.patch
URL:		http://pari.math.u-bordeaux.fr/
BuildRequires:	autoconf
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	readline-devel >= 4.2
BuildRequires:	rpm-perlprov >= 3.0.3-16
%if %{with tex}
BuildRequires:	texlive
BuildRequires:	texlive-amstex
BuildRequires:	texlive-csplain
BuildRequires:	texlive-dvips
BuildRequires:	texlive-fonts-cm
BuildRequires:	texlive-plain
BuildRequires:	texlive-pdftex
BuildRequires:	texlive-tex-babel
BuildRequires:	texlive-tex-ruhyphen
%endif
BuildRequires:	xorg-lib-libX11-devel
Requires:	pari = %{pari_version}-%{release}
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

%description -l pl.UTF-8
System PARI/GP jest przeznaczony do wydajnych obliczeń z zakresu
teorii liczb, ale zawiera również inne przydatne funkcje. Jest nieco
spokrewniony z Komputerowymi Systemami Algebraicznymi, ale nie
identyczny, ponieważ traktuje wyrażenia symboliczne jako obiekty
matematyczne (macierze, wielomiany, szeregi itp.) a nie jako wyrażenia
same w sobie. Jest jednak często znacznie szybszy od innych KSA-ów a
ponadto zawiera wiele innych funkcji nie spotykanych gdzie indziej, a
przydatnych zwłaszcza w teorii liczb.

%package -n pari
Summary:	Shared PARI library (required by the parigp package)
Summary(pl.UTF-8):	Biblioteka współdzielona PARI (wymagana przez pakiet parigp)
Group:		Libraries

%description -n pari
Shared PARI library. You need it to run PARI/GP.

%description -n pari -l pl.UTF-8
Biblioteka współdzielona PARI. Potrzebujesz jej do uruchomienia
PARI/GP.

%package -n pari-devel
Summary:	Include files for PARI shared library
Summary(pl.UTF-8):	Pliki nagłówkowe do biblioteki współdzielonej PARI
Group:		Development/Libraries
Requires:	pari = %{pari_version}-%{release}

%description -n pari-devel
Include files for shared PARI library. You need them to use PARI
routines in you own programs.

%description -n pari-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki współdzielonej PARI. Będziesz ich
potrzebował, jeżeli będziesz chciał wykorzystywać procedury PARI w
swoich programach.

%package -n pari-static
Summary:	Static PARI library
Summary(pl.UTF-8):	Statyczna biblioteka PARI
Group:		Development/Libraries
Requires:	pari-devel = %{pari_version}-%{release}

%description -n pari-static
Static PARI library. You need it to statically link your programs with
PARI.

%description -n pari-static -l pl.UTF-8
Biblioteka statyczna PARI. Potrzebujesz jej do konsolidowania
statycznego swoich programów korzystających z biblioteki PARI.

%package demos
Summary:	Example PARI/GP scripts
Summary(pl.UTF-8):	Przykładowe skrypty pisane w języku PARI/GP
Group:		Applications/Math
Requires:	%{name} = %{pari_version}-%{release}

%description demos
Example PARI/GP scripts. You can write such programs on your own.

%description demos -l pl.UTF-8
Przykładowe skrypty pisane w języku PARI/GP. Sam możesz takie napisać.

%package galdata
Summary:	Galois data resolvents for PARI/GP
Summary(pl.UTF-8):	Reprezentacje danych Galois fla PARI/GP
Group:		Applications/Math
Requires:	%{name} = %{pari_version}-%{release}

%description galdata
Galois data resolvents for PARI/GP.

%description galdata -l pl.UTF-8
Reprezentacje danych Galois do PARI/GP.

%package gp2c
Summary:	PARI/GP to C translator
Summary(pl.UTF-8):	Konwerter skryptów PARI/GP do języka C
Version:	%{gp2c_version}
Epoch:		1
Group:		Development/Tools
Requires:	pari-devel = %{pari_version}-%{release}
Requires:	%{name} = %{pari_version}-%{release}

%description gp2c
PARI/GP to C translator. Use it to compile your own C programs which
use pari library, without necessarily being a C programmer. Note: use
gp2c-run to run your programs inside the PARI/GP environment.

%description gp2c -l pl.UTF-8
Konwerter skryptów PARI/GP do języka C. Można nim tworzyć własne
programy w C korzystające z biblioteki pari. Znajomość języka C nie
jest wymagana. Uwaga: do uruchamiania programów w środowisku PARI/GP
należy używać gp2c-run.

%package -n xemacs-parigp-mode-pkg
Summary:	PARI/GP mode for Octave
Summary(pl.UTF-8):	Tryb edycji plików PARI/GP do XEmacsa
Group:		Applications/Editors/Emacs
Requires:	xemacs

%description -n xemacs-parigp-mode-pkg
PARI/GP editing mode for Xemacs.

%description -n xemacs-parigp-mode-pkg -l pl.UTF-8
Tryb edycji plików PARI/GP do Xemacsa.

%package -n perl-Math-Pari
Summary:	Math-Pari perl module
Summary(pl.UTF-8):	Moduł perla Math-Pari
Version:	%{math_pari_version}
Group:		Development/Languages/Perl

%description -n perl-Math-Pari
The Perl interface to the PARI part of GP/PARI.

%description -n perl-Math-Pari -l pl.UTF-8
Interfejs Perla do biblioteki PARI.

%prep
%setup -q -n pari-%{pari_version} -a 2 -a 3
%patch2 -p1
%patch3 -p1
%patch6 -p1
%patch7 -p1

%build
# pari & parigp
./Configure \
	--host=%{_target_cpu} \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--share-prefix=%{_datadir}

%{__make} all \
	CFLAGS="%{rpmcflags} -fPIC -DGCC_INLINE"

%{?with_tex:%{__make} doc}
src/make_vi_tags src
%ifarch %{ix86}
ln -s Olinux-%{_target_cpu} Olinux-ix86
%endif
%ifarch sparc sparc64
# allow building sparc package on sparc64
ln -s Olinux-sparc Olinux-sparc64
%endif

# gp2c
cd gp2c-%{gp2c_version}
ln -sf .. pari
%{__autoconf}
%configure \
	--datadir=%{_datadir}/parigp
%{__make}
cd ..

# math-pari
cd Math-Pari-%{math_pari_version}
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"
# %{__make} test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/parigp/galdata,%{_examplesdir}/parigp} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

# parigp, pari & pari-devel
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install src/tags $RPM_BUILD_ROOT%{_datadir}/parigp/misc
install %{SOURCE4} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE5} $RPM_BUILD_ROOT%{_pixmapsdir}

# pari-static
install Olinux-%{_target_cpu}/libpari.a $RPM_BUILD_ROOT%{_libdir}/libpari.a

# parigp-demos
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/parigp

# galdata
tar zxvf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/parigp/galdata

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
%{__make} install -C gp2c-%{gp2c_version} \
	DESTDIR=$RPM_BUILD_ROOT

# math-pari
%{__make} install -C Math-Pari-%{math_pari_version} \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/pari.1
echo ".so gp.1" > $RPM_BUILD_ROOT%{_mandir}/man1/pari.1

%clean
rm -rf $RPM_BUILD_ROOT

%post   -n pari -p /sbin/ldconfig
%postun -n pari -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS Announce* CHANGES COMPAT MACHINES NEW README TODO
%doc examples/Inputrc doc/refcard.ps
%attr(755,root,root) %{_bindir}/gp-2.1
%attr(755,root,root) %{_bindir}/gp
%attr(755,root,root) %{_bindir}/gphelp
%attr(755,root,root) %{_bindir}/tex2mail
%dir %{_datadir}/parigp
%{?with_tex:%{_datadir}/parigp/doc}
%{_datadir}/parigp/misc
%{_mandir}/man1/[!g]*.1*
%{_mandir}/man1/gp.1*
%{_mandir}/man1/gphelp.1*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*

%files -n pari
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*

%files -n pari-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/pari

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
%doc gp2c-%{gp2c_version}/{AUTHORS,ChangeLog,NEWS,README,BUGS%{?with_tex:,doc/gp2c.dvi},doc/html/*}
%{_datadir}/parigp/gp2c
%{_mandir}/man1/gp2c*.1*

%files -n perl-Math-Pari
%defattr(644,root,root,755)
%doc Math-Pari-%{math_pari_version}/{Changes,README,TODO}
%{perl_vendorarch}/Math/*.pm
%dir %{perl_vendorarch}/auto/Math/Pari
%{perl_vendorarch}/auto/Math/Pari/Pari.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Math/Pari/Pari.so
%{_mandir}/man3/*
