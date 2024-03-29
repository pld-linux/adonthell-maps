Summary:	Maps for Adonthell game engine
Summary(pl.UTF-8):	Mapy dla Adonthella
Name:		adonthell-maps
Version:	0.3.3
Release:	3
Epoch:		1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://freesoftware.fsf.org/download/adonthell/wastesedge-%{version}.tar.gz
# Source0-md5:	c208c4c7aa2e8c97ec7b27a5bf4f2cd0
URL:		http://adonthell.linuxgames.com/download/index.shtml
BuildRequires:	adonthell
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamedatadir	%{_prefix}/share/adonthell/games

%description
Map packs for Adonthell game.

%description -l pl.UTF-8
Paczka z mapami dla Adonthella.

%package wastesedge
Summary:	Waste's Edge map
Summary(pl.UTF-8):	Mapa Waste's Edge
Group:		X11/Applications/Games

%description wastesedge
As a loyal servant of the elven Lady Silverhair, you arrive at the
remote trading post of Waste's Edge, where she is engaged in
negotiations with the dwarish merchant Bjarn Fingolson. But not all is
well at Waste's Edge, and soon you are confronted with circumstances
that are about to destroy your mistress' high reputation. And you are
the only one to avert this ...

%description wastesedge -l pl.UTF-8
Jako lojalny sługa elfiej Srebrzystowłosej Pani zostajesz wysłany do
odległejgo miasteczka kupieckiego, Waste's Edge, w celu negocjacji z
krasnoludzkim kupcem Bjarnem Fingolsonem. Lecz w Waste's Edge nie
dzieje się najlepiej, prędko znajdujesz się w okolicznościach mogących
zniszczyć dobrą reputację twej Pani. I tylko ty możesz temu
zapobiec...

%prep
%setup -q -n wastesedge-%{version}

%build
cp -f /usr/share/automake/config.sub .
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_gamedatadir}/wastesedge/{audio,gfx,maps,scripts} \
	$RPM_BUILD_ROOT%{_gamedatadir}/wastesedge/gettext/po \
	$RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	datadir=$RPM_BUILD_ROOT%{_gamedatadir}/%{name} \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	gamedatadir=$RPM_BUILD_ROOT%{_gamedatadir}/wastesedge/ \
	pixmapdir=$RPM_BUILD_ROOT%{_pixmapsdir} \
	gettextsrcdir=$RPM_BUILD_ROOT%{_gamedatadir}/wastesedge/gettext/po

%clean
rm -rf $RPM_BUILD_ROOT

%files wastesedge
%defattr(644,root,root,755)
%doc README AUTHORS PLAYING
%{_gamedatadir}/wastesedge
%{_pixmapsdir}/*
%attr(755,root,root) %{_bindir}/adonthell-wastesedge
