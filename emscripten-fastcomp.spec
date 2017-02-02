# We need to install it all in its own prefix.
#%define _prefix /usr/lib/emscripten
Name: emscripten-fastcomp
Version: 1.37.2
Release: 1%{?dist}
Summary: The clang+llvm backend for Emscripten

License: NCSA
URL: https://github.com/kripken/emscripten-fastcomp

#Source0: https://github.com/kripken/%{name}/archive/%{version}.tar.gz
Source0: %{name}-%{version}.tar.gz
#Source1: https://github.com/kripken/%{name}-clang/archive/%{version}.tar.gz
Source1: %{name}-clang-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  zlib-devel
BuildRequires:  libffi-devel
BuildRequires:  ncurses-devel
#BuildRequires:  python3-sphinx
#BuildRequires:  libstdc++-static
BuildRequires:  libxml2-devel


%description
emscripten-fastcomp is the clang+llvm backend for Emscripten to
compile C/C++ code into asm.js.

This is a fork of clang and llvm specific to Emscripten.

%prep
%setup -q -n %{name}-clang-%{version} -D -b 1
%setup -q -n %{name}-%{version} -b 0
mv ../%{name}-clang-%{version} tools/clang

%build
mkdir -p _build
cd _build

cmake .. \
       -DCMAKE_BUILD_TYPE=Release \
       -DLLVM_TARGETS_TO_BUILD="X86;JSBackend" \
       -DLLVM_INCLUDE_EXAMPLES=OFF \
       -DLLVM_INCLUDE_TESTS=OFF \
       -DCLANG_INCLUDE_EXAMPLES=OFF \
       -DCLANG_INCLUDE_TESTS=OFF \
       -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DINCLUDE_INSTALL_DIR:PATH=%{_prefix}/include -DLIB_INSTALL_DIR:PATH=%{_prefix}/lib64 -DSYSCONF_INSTALL_DIR:PATH=/etc -DSHARE_INSTALL_PREFIX:PATH=%{_prefix}/share -DLIB_SUFFIX=

make %{?_smp_mflags}

%install
cd _build
make install DESTDIR=%{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_bindir}/*
%{_mandir}/man1/*.1.*
%exclude %{_bindir}/llvm-config-%{__isa_bits}
%exclude %{_mandir}/man1/llvm-config.1.*
%{_libdir}/BugpointPasses.so
%{_libdir}/LLVMHello.so
%{_libdir}/libLLVM-3.8*.so
%{_libdir}/libLTO.so
%{_libdir}/clang/
%{_bindir}/clang*
%{_bindir}/c-index-test



%changelog
