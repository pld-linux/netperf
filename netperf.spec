Summary:	Performance testing tool for TCP/UDP
Summary(pt_BR): Ferramenta para testes de performance de rede TCP/UDP
Summary(es):	Mide la Velocidad de la Conecion entre dos maquinas.
Name:		netperf
Version:	2.3
Release:	0.1
License:	Freely Distributable
Group:		Networking
Source0:	ftp://ftp.cup.hp.com/dist/networking/benchmarks/netperf/%{name}-%{version}.tar.gz
# Source0-md5:	df61b8db5e38d58cdf81748635614d33
URL:		http://www.netperf.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netperf is a tool for measure TCP/UDP speeds

%description -l pt_BR
Ferramenta para medir a velocidade de transferências TCP/UDP

%description -l es
El netperf mide la velocidad en que la tarjeta de red responde.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install netperf $RPM_BUILD_ROOT%{_bindir}
install netserv $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNWLDGMNTS COPYRIGHT README Release_Notes
%attr(755,root,root) %{_bindir}/netpref
%attr(755,root,root) %{_bindir}/netserv
