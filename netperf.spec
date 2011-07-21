# TODO:
# - init for netserver (maybe not, you don't need it running 24x7, do you?)
Summary:	Performance testing tool for TCP/UDP
Summary(es.UTF-8):	Mide la Velocidad de la Conecion entre dos maquinas
Summary(pl.UTF-8):	Narzędzie do testowania wydajności dla TCP/UDP
Summary(pt_BR.UTF-8):	Ferramenta para testes de performance de rede TCP/UDP
Name:		netperf
Version:	2.5.0
Release:	1
License:	distributable
Group:		Networking
Source0:	ftp://ftp.netperf.org/netperf/%{name}-%{version}.tar.bz2
# Source0-md5:	fe23629f061a161b9d52d39b16620318
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
%patch1 -p1

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

for a in doc/examples/*; do
	s=${a##*/}
	install -p $a $RPM_BUILD_ROOT%{_bindir}/%{name}-$s
done

rm -f $RPM_BUILD_ROOT%{_bindir}/*Makefile*
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README Release_Notes
%attr(755,root,root) %{_bindir}/netperf
%attr(755,root,root) %{_bindir}/netserver
%{_infodir}/netperf.info*
%{_mandir}/man1/netperf.1*
%{_mandir}/man1/netserver.1*

%files -n netperf-scripts
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/netperf-arr_script
%attr(755,root,root) %{_bindir}/netperf-packet_byte_script
%attr(755,root,root) %{_bindir}/netperf-sctp_stream_script
%attr(755,root,root) %{_bindir}/netperf-snapshot_script
%attr(755,root,root) %{_bindir}/netperf-tcp_range_script
%attr(755,root,root) %{_bindir}/netperf-tcp_rr_script
%attr(755,root,root) %{_bindir}/netperf-tcp_stream_script
%attr(755,root,root) %{_bindir}/netperf-udp_rr_script
%attr(755,root,root) %{_bindir}/netperf-udp_stream_script
