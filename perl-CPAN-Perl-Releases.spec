#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-CPAN-Perl-Releases
Version  : 3.88
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/B/BI/BINGOS/CPAN-Perl-Releases-3.88.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BI/BINGOS/CPAN-Perl-Releases-3.88.tar.gz
Summary  : Mapping Perl releases on CPAN to the location of the tarballs
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
NAME
CPAN::Perl::Releases - Mapping Perl releases on CPAN to the location of
the tarballs

%package dev
Summary: dev components for the perl-CPAN-Perl-Releases package.
Group: Development
Provides: perl-CPAN-Perl-Releases-devel = %{version}-%{release}

%description dev
dev components for the perl-CPAN-Perl-Releases package.


%prep
%setup -q -n CPAN-Perl-Releases-3.88

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/CPAN/Perl/Releases.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/CPAN::Perl::Releases.3
