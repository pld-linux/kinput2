#
# Conditional build:
%bcond_with canna		# Canna support (default if neither option specified)
%bcond_with wnn6		# Wnn6 support
#
%if ! %{with wnn6}
%define _with_canna 1
%endif
Summary:	Kanji input server for X11
Summary(pl):	Serwer wprowadzania znaków Kanji dla X11
Name:		kinput2
Version:	v3.1
Release:	1
License:	distributable
Group:		X11/Applications
Source0:	ftp://ftp.sra.co.jp/pub/x11/kinput2/%{name}-%{version}.tar.gz
# Source0-md5:	2de20576f150248d1fdfe66d7cc4e510
Source1:	Kinput2.conf.canna-wnn6
Source2:	Kinput2.conf.canna
Source3:	Kinput2.conf.wnn6
BuildRequires:	XFree86-devel
%{?with_canna:BuildRequires:	Canna-devel}
%{?with_wnn6:BuildRequires:	Wnn6-SDK-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir		/usr/X11R6/lib/X11/app-defaults

%description
Kinput2 is an input server for X11 applications that want Japanese
text input.

%description -l pl
Kinput2 jest serwerem wprowadzania danych dla aplikacji X11 które
wymagaj± danych w jêzyku japoñskim.

%prep
%setup -q

%if 0%{with canna}
%{?with_wnn6:cp %{SOURCE1} Kinput2.conf.in}
%{!?with_wnn6:cp %{SOURCE2} Kinput2.conf.in}
%else
%{?with_wnn6:cp %{SOURCE3} Kinput2.conf.in}
%endif

%build
cat Kinput2.conf.in | sed -e 's#$(LIBDIR)#%{_datadir}#' > Kinput2.conf
xmkmf -a
%{__make} \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/ccdef,%{_mandir}/man1,%{_appdefsdir}}
install cmd/%{name} $RPM_BUILD_ROOT%{_bindir}
install cmd/Kinput2.ad $RPM_BUILD_ROOT%{_appdefsdir}/Kinput2
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
%{_appdefsdir}/Kinput2
%{_mandir}/man1/kinput2.1x*
