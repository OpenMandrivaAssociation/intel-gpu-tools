Name: intel-gpu-tools
Version: 1.9
Release: 2
Summary: Userland and debug tools Intel graphics controllers
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(libdrm) >= 2.4.6
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xorg-server) >= 1.3
BuildRequires:	pkgconfig(xorg-macros) >= 1.0.1
BuildRequires:	pkgconfig(xproto) >= 1.0.0
BuildRequires:	pkgconfig(xvmc) >= 1.0.1
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	byacc

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
%setup -q

%build
%configure
%make

%install
%makeinstall_std

# remove docs
rm -rf %{buildroot}%{_datadir}/gtk-doc/html/intel-gpu-tools

%files
%{_bindir}/gem_userptr_benchmark
%{_bindir}/intel-gpu-overlay
%{_bindir}/intel_*
%{_mandir}/man1/intel_*
