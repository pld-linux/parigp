Summary:	Number Theory-oriented Computer Algebra System
Summary(pl):	Komputerowy system obliczeñ algebraicznych zorientowany na metody teorii liczb
Name:		pari
Version:	1.39.03
Release:	1
License:	GPL
Group:		Applications/Math
Group(de):	Applikationen/Mathematik
Group(pl):	Aplikacje/Matematyczne
Source0:	ftp://megrez.math.u-bordeaux.fr/pub/pari/unix/OLD/pari-%{version}.tar.gz
Patch0:		%{name}-asm.patch
URL:		http://www.parigp-home.de/
ExclusiveArch:	%{ix86}
Requires:	xdvi
BuildRequires:	tetex
BuildRequires:	tetex-dvips
BuildRequires:  tetex-ams
BuildRequires:	readline-devel
BuildRequires:	XFree86-devel
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

%package devel
Summary:	Include files for PARI shared library
Summary(pl):	Pliki nag³ówkowe do biblioteki wspó³dzielonej PARI
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	pari = %{version}

%description devel
Include files and PARI library. You need them to use PARI
routines in you own programs.

%description -l pl devel 
Pliki nag³ówkowe i biblioteki PARI. Bêdziesz ich potrzebowa³,
je¿eli bêdziesz chcia³ wykorzystywaæ procedury PARI w swoich
programach.

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
Przyk³adowe skrypty pisane w jêzyku PARI/GP. Sam mo¿esz takie
napisaæ.

%prep
%setup -q
%patch0 -p1

%build
cd src
CFLAGS="$RPM_OPT_FLAGS -ansi" \
XLIBOPTION="-L/usr/X11R6/lib" ./Makemakefile i386
%{__make}
cd ../doc
%{__make}
dvips users.dvi -o

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}/pari} \
	$RPM_BUILD_ROOT{%{_mandir}/man1,%{_examplesdir}/pari}

# parigp, pari & pari-devel
%{__make} -C src install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

%{__install} examples/* $RPM_BUILD_ROOT%{_examplesdir}/pari

gzip -9nf src/{README,THANKS,TODO} doc/*.ps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src/*.gz doc/*.gz
%attr(755,root,root) %{_bindir}/gp
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/pari
%{_libdir}/lib*.a

%files demos
%defattr(644,root,root,755)
%{_examplesdir}/pari
