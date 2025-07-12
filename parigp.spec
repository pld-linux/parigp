#
# Conditional build:
%bcond_without	tex	# TeX documentation
#
%define		pari_version		2.13.4
%define		gp2c_version		0.0.12pl1
# because of previous 2.x versions with 8 minor digits, keep trailing zeros in package Version
%define		math_pari_version	2.03052300
%define		math_pari_fversion	2.030523
Summary:	Number Theory-oriented Computer Algebra System
Summary(pl.UTF-8):	Komputerowy system obliczeń algebraicznych zorientowany na metody teorii liczb
Name:		parigp
Version:	%{pari_version}
Release:	4
License:	GPL v2+
Group:		Applications/Math
Source0:	http://pari.math.u-bordeaux.fr/pub/pari/unix/pari-%{pari_version}.tar.gz
# Source0-md5:	b624752c00b4b87b940fd98c910d8c09
Source1:	http://pari.math.u-bordeaux.fr/pub/pari/packages/galdata.tgz
# Source1-md5:	f9f61b2930757a785b568e5d307a7d75
Source2:	http://pari.math.u-bordeaux.fr/pub/pari/GP2C/gp2c-%{gp2c_version}.tar.gz
# Source2-md5:	07e5959df2a08e519532a03ff5b8111f
Source3:	http://www.cpan.org/modules/by-module/Math/Math-Pari-%{math_pari_fversion}.tar.gz
# Source3-md5:	e5489cb047989bf6ef3f1fdc590ca736
Source4:	%{name}.desktop
Source5:	%{name}.png
Patch0:		%{name}-target_arch.patch
Patch2:		%{name}-arch.patch
Patch3:		perl-Math-Pari-crash-workaround.patch
Patch4:		perl-Math-Pari-noproccpuinfo.patch
Patch5:		%{name}-noproccpuinfo.patch
Patch6:		gmp-version.patch
URL:		http://pari.math.u-bordeaux.fr/
BuildRequires:	autoconf
BuildRequires:	ctags
BuildRequires:	gmp-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	readline-devel >= 4.2
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tex}
BuildRequires:	texlive
BuildRequires:	texlive-amstex
BuildRequires:	texlive-csplain
BuildRequires:	texlive-dvips
BuildRequires:	texlive-fonts-cm
BuildRequires:	texlive-format-pdflatex
BuildRequires:	texlive-latex-ams
BuildRequires:	texlive-plain
BuildRequires:	texlive-pdftex
BuildRequires:	texlive-tex-babel
BuildRequires:	texlive-tex-ruhyphen
%endif
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-imake
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
patch -p1 < Math-Pari-%{math_pari_fversion}/patches/diff-2.13.3-all
%patch -P0 -p1
%patch -P2 -p1
%patch -P5 -p1
%patch -P6 -p1
cd Math-Pari-%{math_pari_fversion}
%patch -P3 -p1
%patch -P4 -p1

%build
# pari & parigp
./Configure \
	--target=%{_target_cpu} \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--sysdatadir=%{_libdir}/parigp \
	--datadir=%{_datadir}/parigp \
	--share-prefix=%{_datadir} \
	--with-readline-lib=%{_libdir} \
	--with-ncurses-lib=%{_libdir} \
	--with-gmp-lib=%{_libdir}

%{__make} -C Olinux-%{_target_cpu} all \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fno-strict-aliasing -fomit-frame-pointer -fPIC"

%{__make} ctags

%{?with_tex:%{__make} -j1 -C doc docpdf}
%ifarch x32
ln -s Olinux-%{_target_cpu} Olinux-x86_64
%endif
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
%{?with_tex:%{__make} -j1 -C doc}

cd ..

# math-pari
cd Math-Pari-%{math_pari_fversion}
cp -f ../Olinux-%{_target_cpu}/paricfg.h libPARI/paricfg.h
echo '#define DL_DFLT_NAME NULL' >>libPARI/paricfg.h

%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
%ifarch x32
	machine=none
%endif

%{__make} \
	OPTIMIZE="%{rpmcflags} -I$(pwd)/../Olinux-%{_target_cpu}"

# %{__make} test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/parigp/galdata,%{_examplesdir}/parigp} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

# parigp, pari & pari-devel
%{__make} -C Olinux-%{_target_cpu} install \
	DESTDIR=$RPM_BUILD_ROOT \
	%{!?with_tex:TEX=: LATEX=:}

install src/tags $RPM_BUILD_ROOT%{_datadir}/parigp/misc
install %{SOURCE4} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE5} $RPM_BUILD_ROOT%{_pixmapsdir}

# pari-static
install Olinux-%{_target_cpu}/libpari.a $RPM_BUILD_ROOT%{_libdir}/libpari.a

# parigp-demos
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/parigp

# galdata
tar zxvf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/parigp/galdata

# gp2c
%{__make} install -C gp2c-%{gp2c_version} \
	DESTDIR=$RPM_BUILD_ROOT

# math-pari
%{__make} -j1 install -C Math-Pari-%{math_pari_fversion} \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/pari.1
echo ".so gp.1" > $RPM_BUILD_ROOT%{_mandir}/man1/pari.1

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/parigp/{examples,doc}
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/gp2c
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Math/libPARI*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%post   -n pari -p /sbin/ldconfig
%postun -n pari -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES* COMPAT NEW README examples/Inputrc %{?with_tex:doc/*.pdf}
%attr(755,root,root) %{_bindir}/gp-2.13
%attr(755,root,root) %{_bindir}/gp
%attr(755,root,root) %{_bindir}/gphelp
%attr(755,root,root) %{_bindir}/tex2mail
%dir %{_datadir}/parigp
%{_datadir}/parigp/PARI
%{_datadir}/parigp/misc
%{_datadir}/parigp/pari.desc
%{_mandir}/man1/gp.1*
%{_mandir}/man1/gp-*.1*
%{_mandir}/man1/gphelp.1*
%{_mandir}/man1/pari.1*
%{_mandir}/man1/tex2mail.1*
%{_desktopdir}/parigp.desktop
%{_pixmapsdir}/parigp.png

%files -n pari
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpari-gmp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpari-gmp.so.7
%{_libdir}/parigp

%files -n pari-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpari.so
%{_includedir}/pari

%files -n pari-static
%defattr(644,root,root,755)
%{_libdir}/libpari.a

%files demos
%defattr(644,root,root,755)
%doc examples/EXPLAIN
%{_examplesdir}/parigp

%files galdata
%defattr(644,root,root,755)
%{_datadir}/parigp/galdata

%files gp2c
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gp2c*
%doc gp2c-%{gp2c_version}/{AUTHORS,ChangeLog,NEWS,README,BUGS,doc/*.{html,png}}
%{?with_tex:%doc gp2c-%{gp2c_version}/doc/gp2c.pdf}
%{_datadir}/parigp/gp2c
%{_mandir}/man1/gp2c*.1*

%files -n perl-Math-Pari
%defattr(644,root,root,755)
%doc Math-Pari-%{math_pari_fversion}/{Changes,README,TODO}
%{perl_vendorarch}/Math/Pari.pm
%{perl_vendorarch}/Math/PariInit.pm
%dir %{perl_vendorarch}/auto/Math/Pari
%attr(755,root,root) %{perl_vendorarch}/auto/Math/Pari/Pari.so
%{_mandir}/man3/Math::Pari.3pm*
%{_mandir}/man3/Math::PariInit.3pm*
%{_mandir}/man3/Math::libPARI.3pm*
%{_mandir}/man3/Math::libPARI.dumb.3pm*
