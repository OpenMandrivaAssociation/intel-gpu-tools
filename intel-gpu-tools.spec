%define oname igt-gpu-tools

Name: intel-gpu-tools
Version: 1.26
Release: 1
Summary: Userland and debug tools Intel graphics controllers
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/archive/individual/app/%{oname}-%{version}.tar.xz
Source100: %{name}.rpmlintrc

BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(libdrm) >= 2.4.6
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libunwind)
BuildRequires:	pkgconfig(libkmod)
BuildRequires:	pkgconfig(pciaccess)
BuildRequires:	pkgconfig(libprocps)
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xorg-server) >= 1.3
BuildRequires:	pkgconfig(xorg-macros) >= 1.0.1
BuildRequires:	pkgconfig(xproto) >= 1.0.0
BuildRequires:	pkgconfig(xvmc) >= 1.0.1
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	gtk-doc
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	byacc
BuildRequires:	python-docutils

%rename igt-gpu-tools

%description
This little package is an amalgamation of a few things:
- miscellaneous userland tools that don't really fit into the 2D driver tree
- standalone regression tests for the DRM (make check)
- microbenchmarks of the DRM for kernel performance regression testing

By far the most popular tool here is intel_gpu_dump (thanks cworth!),
which can be run when your GPU is hung with KMS to produce a log of a
bunch of interesting information for submitting bug reports.  We'll
hopefully be hooking this up to a kerneloops style submission daemon
soon.

intel_gpu_top also gives you information on a few performance bits for
graphical apps, useful for pairing with sysprof+top.

The intel_regdumper tool didn't make it into this release, since I want
to get it rewritten when I move it over.

%prep
%autosetup -n %{oname}-%{version} -p1
./autogen.sh

%build
CC=gcc CXX=g++ %configure
%make_build
# DEBUG_CFLAGS="%{optflags}"

%install
%make_install

# remove docs
rm -rf %{buildroot}%{_datadir}/gtk-doc/html/intel-gpu-tools

%files
%{_bindir}/intel_*
%{_bindir}/igt_stats
%{_bindir}/intel-gen4asm
%{_bindir}/intel-gen4disasm
%{_libdir}/intel_aubdump.so
%{_libdir}/pkgconfig/intel-gen4asm.pc
%{_libexecdir}/intel-gpu-tools
%{_datadir}/intel-gpu-tools
%{_mandir}/man1/intel_*
