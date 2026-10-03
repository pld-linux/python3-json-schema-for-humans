Summary:	Generate static HTML documentation from JSON schemas
Summary(pl.UTF-8):	Generowanie dokumentacji w statycznym HTML ze schematów JSON
Name:		python3-json-schema-for-humans
Version:	1.5.1
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/json-schema-for-humans/
Source0:	https://files.pythonhosted.org/packages/source/j/json-schema-for-humans/json_schema_for_humans-%{version}.tar.gz
# Source0-md5:	0433d6a1c43087310348702a2223b1be
URL:		https://pypi.org/project/json-schema-for-humans/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-poetry-core >= 1.0.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quickly generate a beautiful static HTML or Markdown page documenting
a JSON schema.

- Support for JSON Schema Draft-07
- Since the result is static, it is easier to host and faster to load
- HTML and Markdown output support
- Different templates to choose from
- Anchor links, allow to send a user to a specific section of the
  documentation
- Support for references (even circular!)

%description -l pl.UTF-8
Szybkie generowanie estetycznej, statycznej strony HTML lub Markdown
dokumentującej schemat JSON.

- obsługa specyfikacji JSON Schema Draft-07
- dzięki statycznym wynikom, dokumentacja jest łatwa w hostowaniu i
  szybka w ładowaniu
- obsługa wyjścia HTML i Markdown
- różne sablony do wyboru
- linki zakotwiczeń, pozwalające na odesłanie użytkownika do
  określonej sekcji dokumentacji
- obsługa odwołań (nawet cyklicznych!)

%prep
%setup -q -n json_schema_for_humans-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%attr(755,root,root) %{_bindir}/generate-schema-doc
%{py3_sitescriptdir}/json_schema_for_humans
%{py3_sitescriptdir}/json_schema_for_humans-%{version}.dist-info
