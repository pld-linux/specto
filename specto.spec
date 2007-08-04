# TODO:
# - Add desktop file
Summary:	Event notification application
Summary(pl.UTF-8):	Notyfikacja zdarzeń
Name:		specto
Version:	0.2.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://specto.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	2212c1a6e2e72eb2f13c632745330c9f
URL:		http://code.google.com/p/specto/
BuildRequires:	python-dbus
BuildRequires:	python-devel >= 2.10
BuildRequires:	python-pynotify
Requires:	python
Requires:	python-gnome
Requires:	python-gnome-extras
Requires:	python-gnome-gconf
Requires:	python-pygtk-glade
Requires:	python-pygtk-gtk
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
Specto jest desktopową aplikacją, która będzie obserwować
konfigurowalne zdarzenia (takie jak uaktualnienia stron www, poczty
elektronicznej, pliku, zmiany katalogu, procesów systemowych itp.) i
przekazywać zawiadomienia. Dla przykładu, Specto może w
poszukiwaniu uaktualnień obserwować stronę www (lub ... albo
obrazek itp.) i informować użytkownika gdy zmiany nastąpiły (w
przeciwnym razie Specto będzie pracować dalej). To wszystko zmienia
sposób pracy, ponieważ użytkownik może być informowany o
zdarzeniach zamiast szukać ich samemu.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc data/doc/AUTHORS data/doc/ChangeLog  data/doc/HACKING  data/doc/VERSION
%attr(755,root,root) %{_bindir}/specto
%{_desktopdir}/specto.desktop
%{_iconsdir}/hicolor/scalable/apps/*.svg
%dir %{py_sitescriptdir}/spectlib
%{py_sitescriptdir}/spectlib/*.pyc
%{py_sitescriptdir}/specto-0.2.2-py2.5.egg-info
%dir %{_datadir}/specto
%dir %{_datadir}/specto/glade
%{_datadir}/specto/glade/*.glade
%dir %{_datadir}/specto/icons
%{_datadir}/specto/icons/*.png
%{_datadir}/specto/icons/*.svg
