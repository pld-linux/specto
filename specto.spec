# TODO:
# - program doesn't work, something wrong with gnome icon

Summary:	Event notification application
Summary(pl.UTF-8):	Aplikacja powiadamiająca o zdarzeniach
Name:		specto
Version:	0.2.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://specto.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	2212c1a6e2e72eb2f13c632745330c9f
Patch0:		%{name}-desktop.patch
URL:		http://code.google.com/p/specto/
BuildRequires:	python-dbus
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-pynotify
Requires:	python
Requires:	python-gnome
Requires:	python-gnome-extras
Requires:	python-gnome-gconf
Requires:	python-pygtk-glade >= 2:2.0
Requires:	python-pygtk-gtk >= 2:2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Specto is a desktop application that will watch configurable events
(such as website updates, emails, file and folder changes, system
processes, etc) and then trigger notifications. For example, Specto
can watch a website for updates (or a syndication feed, or an image,
etc), and notify you when there is activity (otherwise, Specto will
just stay out of the way). This changes the way you work, because you
can be informed of events instead of having to look out for them.

%description -l pl.UTF-8
Specto jest aplikacją graficzną, która obserwuje konfigurowalne
zdarzenia (takie jak uaktualnienia stron WWW, wiadomości poczty
elektronicznej, zmiany plików i katalogów, procesy systemowe itp.) i
przekazuje zawiadomienia. Na przykład, Specto może w poszukiwaniu
uaktualnień obserwować stronę WWW (lub łączony feed albo obrazek)
i informować użytkownika o zauważeniu aktywności (w przeciwnym razie
Specto będzie pracować dalej). To wszystko zmienia sposób pracy,
ponieważ użytkownik może być informowany o zdarzeniach zamiast
sprawdzać je samemu.

%prep
%setup -q
%patch0 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc data/doc/AUTHORS data/doc/ChangeLog data/doc/HACKING data/doc/VERSION
%attr(755,root,root) %{_bindir}/specto
%{_datadir}/specto
%dir %{py_sitescriptdir}/spectlib
%{py_sitescriptdir}/spectlib/*.py[co]
%{py_sitescriptdir}/specto-*.egg-info
%{_desktopdir}/specto.desktop
%{_iconsdir}/hicolor/scalable/apps/*.svg
