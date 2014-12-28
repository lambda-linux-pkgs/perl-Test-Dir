%define _buildid .1

Name:           perl-Test-Dir
Version:        1.014
Release:        8%{?_buildid}%{?dist}
Summary:        Some simple tests on directories and folders
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Dir/
Source0:        http://www.cpan.org/authors/id/M/MT/MTHURN/Test-Dir-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(inc::Module::Install)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Test::Builder)
# Tests:
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

This modules provides a collection of test utilities for directory and folder
attributes. Use it in combination with Test::More in your test programs.

%prep
%setup -q -n Test-Dir-%{version}
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Dec 28 2014 Rajiv M Ranganath <rajiv.ranganath@atihita.com> 1.014-8
- Adapt for AL/LL
- Add package support URL
- Import source package FC21/perl-Test-Dir-1.014-8.fc21

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.014-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.014-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 1.014-6
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.014-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.014-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 1.014-3
- Perl 5.16 rebuild

* Fri May 04 2012 Petr Pisar <ppisar@redhat.com> - 1.014-2
- Use Test::Pod for optional test

* Thu Apr 26 2012 Petr Pisar <ppisar@redhat.com> 1.014-1
- Specfile autogenerated by cpanspec 1.78.
