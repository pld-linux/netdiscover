Summary:	Netdiscover - an active/passive address reconnaissance tool
Summary(pl.UTF-8):   Netdiscover - aktywno-pasywne narzędzie do wyszukiwania adresów
Name:		netdiscover
Version:	0.3
%define		_beta	beta5
Release:	0.%{_beta}.1
License:	GPL v2
Group:		Applications
Source0:	http://nixgeneration.com/~jaime/netdiscover/releases/%{name}-%{version}-%{_beta}.tar.gz
# Source0-md5:	de30ff57b01584789d6bec0d1466e66d
URL:		http://nixgeneration.com/~jaime/netdiscover/
BuildRequires:	libnet-devel
BuildRequires:	libpcap-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netdiscover is an active/passive address reconnaissance tool, mainly
developed for those wireless networks without DHCP server, when you
are wardriving. It can be also used on hub/switched networks.

%description -l pl.UTF-8
Netdiscover to aktywno-pasywne narzędzie do wyszukiwania adresów,
stworzone głównie dla sieci bezprzewodowych bez serwera DHCP. Może
być używane także w sieciach opartych o huby/switche.

%prep
%setup -q -n %{name}-%{version}-%{_beta}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install src/%{name} $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_sbindir}/*
