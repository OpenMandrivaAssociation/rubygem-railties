%define gemname railties
Summary:	Web-application framework with template engine, control-flow layer, and ORM
Name:		rubygem-%{gemname}
Version:	3.2.1
Release:	%mkrel 1
Source0:	http://rubygems.org/downloads/%{gemname}-%{version}.gem
License:	MIT
Group:		System/Servers
Url:		http://www.rubyonrails.org/
BuildRoot:	%{_tmppath}/%{gemname}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	ruby-RubyGems

%description
Rails is a full-stack framework for developing database-backed web
applications according to the Model-View-Control pattern. From the
Ajax in the view, to the request and response in the controller, to
the domain model wrapping the database, Rails gives you a pure-Ruby
development environment. To go live, all you need to add is a database
and a web server.

%prep
%setup -c

%build

%install
rm -rf $RPM_BUILD_ROOT

gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/rails
%{ruby_gemdir}/gems/%{gemname}-%{version}
%{ruby_gemdir}/specifications/%{gemname}-%{version}.gemspec

