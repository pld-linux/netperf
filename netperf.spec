Summary:	Performance testing tool for TCP/UDP
Summary(es):	Mide la Velocidad de la Conecion entre dos maquinas
Summary(pl):	Narzêdzie do testowania wydajno¶ci dla TCP/UDP
Summary(pt_BR):	Ferramenta para testes de performance de rede TCP/UDP
Name:		netperf
Version:	2.3
Release:	0.1
License:	Freely Distributable
Group:		Networking
#Source0:	ftp://ftp.cup.hp.com/dist/networking/benchmarks/netperf/%{name}-%{version}.tar.gz
Source0:	netperf-2.3.tar.gz
# Source0-md5:	df61b8db5e38d58cdf81748635614d33
Patch0:		%{name}-makefile.patch
URL:		http://www.netperf.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netperf is a tool for measure TCP/UDP speeds.

%description -l es
El netperf mide la velocidad en que la tarjeta de red responde.

%description -l pl
Netperf to narzêdzie do mierzenia szybko¶ci TCP/UDP.

%description -l pt_BR
Ferramenta para medir a velocidade de transferências TCP/UDP.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install netperf $RPM_BUILD_ROOT%{_bindir}
install netserver $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNWLDGMNTS COPYRIGHT README Release_Notes
%attr(755,root,root) %{_bindir}/netperf
%attr(755,root,root) %{_bindir}/netserver
