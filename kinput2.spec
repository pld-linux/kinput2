# --with canna
# --with wnn6
%if %{?_with_wnn6:0}%{!?_with_wnn6:1}
%define _with_canna 1
%endif
Summary:	Kanji input server for X11
Summary(pl):	Serwer wprowadzania znaków Kanji dla X11
Name:		kinput2
Version:	v3
Release:	1
License:	distributable
Group:		X11/Applications
Source0:	ftp://ftp.sra.co.jp/pub/x11/kinput2/%{name}-%{version}.tar.gz
%if %{?_with_canna:1}
%{?_with_wnn6:Source1:	Kinput2.conf.canna-wnn6}
%{!?_with_wnn6:Source1:	Kinput2.conf.canna}
%else
%{?_with_wnn6:Source1:	Kinput2.conf.wnn6}
%endif
%{?_with_canna:BuildRequires:	Canna-devel}
%{?_with_wnn6:BuildRequires:	Wnn6-SDK-devel}
BuildRequires:	imake
BuildRequires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kinput2 is an input server for X11 applications that want Japanese
text input.

%description -l pl
Kinput2 jest serwerem wprowadzania danych dla aplikacji X11 które
wymagaj± danych w jêzyku japoñskim.

%prep
%setup -q

%build
cat %{SOURCE1} | sed -e 's#$(LIBDIR)#%{_datadir}#' > ./Kinput2.conf
xmkmf -a
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/ccdef,%{_mandir}/man1,%{_libdir}/X11/app-defaults}
install cmd/%{name} $RPM_BUILD_ROOT%{_bindir}
install cmd/Kinput2.ad $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/Kinput2
install cmd/kinput2.man $RPM_BUILD_ROOT%{_mandir}/man1/kinput2.1x
install ccdef/ccdef* $RPM_BUILD_ROOT%{_datadir}/ccdef
install ccdef/rule* $RPM_BUILD_ROOT%{_datadir}/ccdef
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README doc/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/ccdef
%{_libdir}/X11/app-defaults/Kinput2
%{_mandir}/man1/kinput2.1x*
