# TODO:
# - init for netserver
Summary:	Performance testing tool for TCP/UDP
Summary(es.UTF-8):	Mide la Velocidad de la Conecion entre dos maquinas
Summary(pl.UTF-8):	Narzędzie do testowania wydajności dla TCP/UDP
Summary(pt_BR.UTF-8):	Ferramenta para testes de performance de rede TCP/UDP
Name:		netperf
Version:	2.3
Release:	3
License:	distributable
Group:		Networking
#Source0:	ftp://ftp.cup.hp.com/dist/networking/benchmarks/netperf/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	df61b8db5e38d58cdf81748635614d33
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-scripts.patch
URL:		http://www.netperf.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netperf is a tool for measure TCP/UDP speeds.

%description -l es.UTF-8
El netperf mide la velocidad en que la tarjeta de red responde.

%description -l pl.UTF-8
Netperf to narzędzie do mierzenia szybkości TCP/UDP.

%description -l pt_BR.UTF-8
Ferramenta para medir a velocidade de transferências TCP/UDP.

%package -n netperf-scripts
Summary:	Scripts for Netperf
Summary(pl.UTF-8):	Skrypty dla Netperfa
Group:		Networking

%description -n netperf-scripts
Scripts for Netperf.

%description -n netperf-scripts -l pl.UTF-8
Skrypty dla Netperfa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{doc}/scripts}

install netperf			$RPM_BUILD_ROOT%{_bindir}
install netserver		$RPM_BUILD_ROOT%{_bindir}
install arr_script		$RPM_BUILD_ROOT%{_bindir}/netperf-script_arr
install snapshot_script		$RPM_BUILD_ROOT%{_bindir}/netperf-script_snapshot
install tcp_rr_script		$RPM_BUILD_ROOT%{_bindir}/netperf-script_tcp_rr
install udp_rr_script		$RPM_BUILD_ROOT%{_bindir}/netperf-script_udp_rr
install packet_byte_script	$RPM_BUILD_ROOT%{_bindir}/netperf-script_packet_byte
install tcp_range_script	$RPM_BUILD_ROOT%{_bindir}/netperf-script_tcp_range
install tcp_stream_script	$RPM_BUILD_ROOT%{_bindir}/netperf-script_tcp_stream
install udp_stream_script	$RPM_BUILD_ROOT%{_bindir}/netperf-script_udp_stream
install netperf.man		$RPM_BUILD_ROOT%{_mandir}/man1/netperf.1
install netserver.man		$RPM_BUILD_ROOT%{_mandir}/man1/netserver.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNWLDGMNTS COPYRIGHT README Release_Notes
%attr(755,root,root) %{_bindir}/netperf
%attr(755,root,root) %{_bindir}/netserver
%{_mandir}/man?/*

%files -n netperf-scripts
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/netperf-script_arr
%attr(755,root,root) %{_bindir}/netperf-script_snapshot
%attr(755,root,root) %{_bindir}/netperf-script_tcp_rr
%attr(755,root,root) %{_bindir}/netperf-script_udp_rr
%attr(755,root,root) %{_bindir}/netperf-script_packet_byte
%attr(755,root,root) %{_bindir}/netperf-script_tcp_range
%attr(755,root,root) %{_bindir}/netperf-script_tcp_stream
%attr(755,root,root) %{_bindir}/netperf-script_udp_stream
