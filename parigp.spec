Summary:	Number Theory-oriented Computer Algebra System
Summary(pl):	Komputerowy system obliczeñ algebraicznych zorientowany na metody teorii liczb
Name:		parigp
Version:	2.1.0
Release:	1
License:	GPL
Group:		Applications/Math
Group(de):	Applikationen/Mathematik
Group(pl):	Aplikacje/Matematyczne
Source0:	ftp://megrez.math.u-bordeaux.fr/pub/pari/unix/pari-%{version}.tgz
Source1:	ftp://megrez.math.u-bordeaux.fr/pub/pari/galdata.tgz
Patch0:		%{name}-FHS.patch
Patch1:		%{name}-target_arch.patch
Icon:		%{name}.xpm
URL:		http://www.parigp-home.de/
Requires:	pari = %{version}
Requires:	xdvi
BuildRequires:	xemacs
BuildRequires:	tetex
BuildRequires:	tetex-dvips
BuildRequires:	readline-devel
BuildRequires:	XFree86-devel
BuildRequires:	perl
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
Group(fr):	Librairies
Group(pl):	Biblioteki

%description -n pari
Shared PARI library. You need it to run PARI/GP.

%description -l pl -n pari
Biblioteka wspó³dzielona PARI. Potrzebujesz jej do uruchomienia PARI /
GP.

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

%package static
Summary:	PARI/GP statically linked with PARI library
Summary(pl):	PARI/GP konsolidowane statycznie z bibliotek± PARI
Group:		Applications/Math
Group(de):	Applikationen/Mathematik
Group(pl):	Aplikacje/Matematyczne
Requires:	%{name} = %{version}

%description static
PARI/GP is a package which is aimed at efficient computations in
number theory, but also contains a large number of other useful
functions. It is somewhat related to a Computer Algebra System, but is
not really one since it treats symbolic expressions as mathematical
entities such as matrices, polynomials, series, etc..., and not as
expressions per se. However it is often much faster than other CAS,
and contains a large number of specific functions not found elsewhere,
essentially for use in number theory. This package is statically
linked with PARI library.

%description static -l pl
System PARI/GP jest przeznaczony do wydajnych obliczeñ z zakresu
teorii liczb, ale zawiera równie¿ inne przydatne funkcje. Jest nieco
spokrewniony z Komputerowymi Systemami Algebraicznymi, ale nie
identyczny, poniewa¿ traktuje wyra¿enia symboliczne jako obiekty
matematyczne (macierze, wielomiany, szeregi itp.) a nie jako wyra¿enia
same w sobie. Jest jednak czêsto znacznie szybszy od innych KSA-ów a
ponadto zawiera wiele innych funkcji nie spotykanych gdzie indziej, a
przydatnych zw³aszcza w teorii liczb. Ten pakiet zosta³ zkonsolidowany
statycznie z bibliotek± PARI.

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

%description -n xemacs-parigp-mode-pkg
PARI/GP editing mode for Xemacs.

%description -l pl -n xemacs-parigp-mode-pkg
Tryb edycji plików PARI/GP do Xemacsa.

%prep
%setup0 -q -n pari-%{version}
%patch0 -p1
%patch1 -p1

%build

./Configure --target=%{_target_cpu} --prefix=%{_prefix}

%{__make} all
%{__make} doc

%install
rm -rf $RPM_BUILD_ROOT

# parigp, pari & pari-devel
%{__make} install LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	DATADIR=$RPM_BUILD_ROOT%{_datadir}/parigp/data \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	MISCDIR=$RPM_BUILD_ROOT%{_datadir}/parigp \
	INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir}/pari

# parigp-static
%{__install} Olinux-%{_target_cpu}/gp-sta $RPM_BUILD_ROOT%{_bindir}/gp-2.1.static
ln -sf gp-2.1.static $RPM_BUILD_ROOT%{_bindir}/gp.static
%{__install} Olinux-%{_target_cpu}/libpari.a $RPM_BUILD_ROOT%{_libdir}/libpari.a

# parigp-demos
%{__install} -d $RPM_BUILD_ROOT%{_examplesdir}/parigp
%{__install} examples/* $RPM_BUILD_ROOT%{_examplesdir}/parigp

# galdata
%{__install} -d $RPM_BUILD_ROOT%{_datadir}/parigp/data
tar zxvf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/parigp/data/

# # xemacs-parigp-mode-pkg
# %{__install} -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/parigp-mode
# cp -a emacs/*.el $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/parigp-mode
# cat <<EOF >$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/parigp-mode/auto-autoloads.el
# (autoload 'gp-mode "pari" nil t)
# (autoload 'gp-script-mode "pari" nil t)
# (autoload 'gp "pari" nil t)
# (autoload 'gpman "pari" nil t)
# EOF

gzip -9nf Announce* AUTHORS CHANGES COMPAT CVS.txt INSTALL.tex INSTALL.txt \
	MACHINES NEW README README.DOS TODO emacs/*

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
%doc *.gz misc/*.gz doc/*.gz emacs
%dir %{_datadir}/parigp
%{_datadir}/parigp/*.tex
%{_datadir}/parigp/*.dvi
%{_datadir}/parigp/refcard.ps
%{_datadir}/parigp/translations
%{_mandir}/man1/*
%dir %{_datadir}/parigp/data

%files -n pari
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*

%files -n pari-devel
%defattr(644,root,root,755)
%{_includedir}/pari

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gp-2.1.static
%attr(755,root,root) %{_bindir}/gp.static
%{_libdir}/*.a

%files demos
%defattr(644,root,root,755)
%{_examplesdir}/parigp

%files galdata
%defattr(644,root,root,755)
%{_datadir}/parigp/data/*
