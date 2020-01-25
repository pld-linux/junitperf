Summary:	JUnit extension for performance and scalability testing
Summary(pl.UTF-8):	Rozszerzenie JUnita do testowania wydajności i skalowalności
Name:		junitperf
Version:	1.9.1
Release:	0.1
License:	BSD
Group:		Development
Source0:	http://www.clarkware.com/software/%{name}-%{version}.zip
# Source0-md5:	ee91fe1b2bcdbe554bdffe0ffb1d63ab
URL:		http://www.clarkware.com/software/JUnitPerf.html
BuildRequires:	ant
BuildRequires:	jpackage-utils >= 0:1.6
BuildRequires:	junit >= 0:3.2
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	junit >= 0:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JUnitPerf is a collection of JUnit test decorators used to measure the
performance and scalability of functionality contained within existing
JUnit tests.

%description -l pl.UTF-8
JUnitPerf to zestaw dekoratorów testów JUnita służący do mierzenia
wydajności i skalowalności funkcji zawartych w istniejących testach
JUnita.

%package javadoc
Summary:	Javadoc for JUnitPerf
Summary(pl.UTF-8):	Dokumentacja Javadoc do pakietu JUnitPerf
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Javadoc for JUnitPerf.

%description javadoc -l pl.UTF-8
Dokumentacja Javadoc do pakietu JUnitPerf.

%package demo
Summary:	Demos for JUnitPerf
Summary(pl.UTF-8):	Przykłady użycia pakietu JUnitPerf
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for JUnitPerf.

%description demo -l pl.UTF-8
Przykłady użycia pakietu JUnitPerf.

%prep
%setup -q
find -name '*.jar' | xargs rm -fv

%build
CLASSPATH=$(build-classpath junit)
%ant -Dbuild.sysclasspath=first \
	jar test javadoc

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadir}
cp -a dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# demo
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}
cp -pr samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc LICENSE README docs/JUnitPerf.html
%{_javadir}/%{name}*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}
