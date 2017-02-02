Name: emscripten
Version: 1.37.2
Release: 2%{?dist}
Summary: The emscripten compiler.

License: NCSA
URL: https://github.com/kripken/emscripten

#https://github.com/kripken/emscripten/archive/1.37.2.tar.gz
Source0: %{name}-%{version}.tar.gz
Source100: em.sh
BuildArch: noarch

Requires: emscripten-fastcomp = %{version}
Requires: python >= 2.7
Requires: nodejs
Requires: gcc-c++
Requires(posttrans): %{_sbindir}/alternatives

%description
Emscripten is the C/C++ to JavaScript compiler. This package is the
GCC compatible front-end driver.

%prep
%setup -q -n %{name}-%{version}

%install
install -d %{buildroot}%{_datadir}/emscripten
install -d %{buildroot}%{_datadir}/emscripten/bin
install -m 0644 emscripten-version.txt %{buildroot}%{_datadir}/emscripten
install -D -m 0755 em* -t %{buildroot}%{_datadir}/emscripten/
install -m 0755 %{SOURCE100} %{buildroot}%{_datadir}/emscripten/bin/_em.sh
cp -va tools -t %{buildroot}%{_datadir}/emscripten/
cp -va system -t %{buildroot}%{_datadir}/emscripten/
cp -va src -t %{buildroot}%{_datadir}/emscripten/

%post
%{_sbindir}/update-alternatives --install %{_bindir}/emcc emcc %{_datadir}/emscripten/bin/_em.sh 10
%{_sbindir}/update-alternatives --install %{_bindir}/em++ em++ %{_datadir}/emscripten/bin/_em.sh 10
%{_sbindir}/update-alternatives --install %{_bindir}/emar emar %{_datadir}/emscripten/bin/_em.sh 10
%{_sbindir}/update-alternatives --install %{_bindir}/emranlib  emranlib %{_datadir}/emscripten/bin/_em.sh 10
%{_sbindir}/update-alternatives --install %{_bindir}/emrun  emrun %{_datadir}/emscripten/bin/_em.sh 10
%{_sbindir}/update-alternatives --install %{_bindir}/emcmake emcmake %{_datadir}/emscripten/bin/_em.sh 10

%postun
[ $1 -eq 0 ] && %{_sbindir}/update-alternatives --remove emcc %{_datadir}/emscripten/bin/_em.sh
[ $1 -eq 0 ] && %{_sbindir}/update-alternatives --remove em++ %{_datadir}/emscripten/bin/_em.sh
[ $1 -eq 0 ] && %{_sbindir}/update-alternatives --remove emar %{_datadir}/emscripten/bin/_em.sh
[ $1 -eq 0 ] && %{_sbindir}/update-alternatives --remove emranlib %{_datadir}/emscripten/bin/_em.sh
[ $1 -eq 0 ] && %{_sbindir}/update-alternatives --remove emrun %{_datadir}/emscripten/bin/_em.sh
[ $1 -eq 0 ] && %{_sbindir}/update-alternatives --remove emcmake %{_datadir}/emscripten/bin/_em.sh

%files
%exclude %{_datadir}/emscripten/*.bat
%{_datadir}/emscripten/*

%changelog
* Thu Feb  2 2017 Hubert Figuiere <hub@figuiere.net> - 1.37.2-2
- em.sh now export PATH to allow autodetection of LLVM_ROOT

* Thu Feb  2 2017 Hubert Figuiere <hub@figuiere.net> - 1.37.2-1
- Initial release for Fedora.
