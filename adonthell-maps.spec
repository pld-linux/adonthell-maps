Summary:	Maps for Adonthell game engine.
Summary(pl):	Mapy dla Adonthell'a
Name:		adonthell-maps
Version:	1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://freesoftware.fsf.org/download/adonthell/wastesedge-0.3.%{version}.tar.gz
URL:		http://adonthell.linuxgames.com/download/index.shtml
BuildRequires:	adonthell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define         _bindir         %{_prefix}/bin/
%define         _gamedatadir    share/adonthell/games/

%description
Map packs for Adonthell game

%description -l pl
Paczka z mapami dla Adonthell'a

%package wastesedge
Summary:	Waste's Edge map
Summary(pl):	Mapa Waste's Edge
Group:		X11/Applications/Games

%description wastesedge
As a loyal servant of the elven Lady Silverhair, you arrive at the
remote trading post of Waste's Edge, where she is engaged in
negotiations with the dwarish merchant Bjarn Fingolson. But not all is
well at Waste's Edge, and soon you are confronted with circumstances
that are about to destroy your mistress' high reputation. And you are
the only one to avert this ...

%description wastesedge -l pl
Jako lojalny s³uga elfiej Srebrzystow³osej Pani zostajesz wys³any do
odleg³ejgo miasteczka kupieckiego, Waste's Edge, w celu negocjacji z
krasnoludzkim kupcem Bjarnem Fingolsonem. Lecz w Waste's Edge nie
dzieje siê najlepiej, prêdko znajdujesz siê w okoliczno¶ciach mog±cych
zniszczyæ dobr± reputacjê twej Pani. I tylko ty mo¿esz temu
zapobiec...

%prep
%setup -q -c -a0

%build
cd wastesedge-0.3.1
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/%{_gamedatadir} $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT{%{_prefix}/%{_gamedatadir}/wastesedge/{audio,gfx,maps,scripts}}
cd wastesedge-0.3.1
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} bindir=$RPM_BUILD_ROOT%{_bindir} gamedatadir=$RPM_BUILD_ROOT%{_prefix}/%{_gamedatadir}/wastesedge/ install
gzip -9nf README AUTHORS PLAYING
%clean
rm -fr $RPM_BUILD_ROOT

%files wastesedge
%defattr(644,root,root,755)
#%doc *.gz
%{_prefix}/%{_gamedatadir}/
%attr(755,root,root)%{_bindir}/adonthell-wastesedge
