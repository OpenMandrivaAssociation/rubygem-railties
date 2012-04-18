# Generated from railties-3.2.1.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	railties

Summary:	Tools for creating, working with, and running Rails applications
Name:		rubygem-%{rbname}

Version:	3.2.3
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://www.rubyonrails.org
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
Source1:	%{name}.rpmlintrc
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Rails internals: application bootup, plugins, generators, and rake tasks.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f guides

%install
%gem_install

%files
%{_bindir}/rails
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/rails
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/guides
%{ruby_gemdir}/gems/%{rbname}-%{version}/guides/*
