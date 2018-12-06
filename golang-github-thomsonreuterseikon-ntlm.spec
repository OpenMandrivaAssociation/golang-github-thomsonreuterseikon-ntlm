%global goipath         github.com/ThomsonReutersEikon/go-ntlm
%global commit          51f51a355c40946a10ff9f8f3c1da22977701967

%gometa

Name:           %{goname}
Version:        0
Release:        0.7%{?dist}
Summary:        Native implementation of NTLM for Go
License:        BSD with advertising
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}.

%package devel
Summary:       %{summary}
BuildArch:     noarch

Provides:       golang-github-ThomsonReutersEikon-go-ntlm-devel = %{version}-%{release}
Obsoletes:      golang-github-ThomsonReutersEikon-go-ntlm-devel < 0.6

%description devel
%{summary}.

This package contains library source intended for building other packages
which use import path with %{goipath} prefix.


%prep
%gosetup -q


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license License
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git51f51a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 10 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.6.20180610git51f51a3
- Update to latest commit.
- Rename to match More Go Packaging rules.
- Refresh spec against More Go Packaging template.

* Thu Feb 08 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.5.20171030git2a7c173
- Update to latest commit.
- Add patch to build against latest Go compiler.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20151029gitb00ec39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.3.20151029gitb00ec39
- Add commit date to release.

* Fri Aug 18 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.2.gitb00ec39
- Add documentation to subpackage.

* Sun May 15 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0-0.1.gitb00ec39
- Initial package
