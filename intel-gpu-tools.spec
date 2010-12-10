Name: intel-gpu-tools
Version: 1.0.2
Release: %mkrel 2
Summary: Userland and debug tools Intel graphics controllers
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/archive/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libdrm-devel >= 2.4.6
BuildRequires: libxvmc-devel >= 1.0.1
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.3
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: GL-devel

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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/intel_*
%{_datadir}/man/man1/intel_*
