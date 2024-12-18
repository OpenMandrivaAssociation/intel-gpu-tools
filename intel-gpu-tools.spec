%define oname igt-gpu-tools

Name: intel-gpu-tools
Version: 1.30
Release: 1
Summary: Userland and debug tools Intel graphics controllers
Group: System/X11
License: MIT
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/archive/individual/app/%{oname}-%{version}.tar.xz
Source100: %{name}.rpmlintrc

BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(cairo)
BuildRequires:  pkgconfig(dri2proto)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(json-c)
BuildRequires:	pkgconfig(libdrm) >= 2.4.6
BuildRequires:  pkgconfig(libdw)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(libunwind)
BuildRequires:	pkgconfig(libkmod)
BuildRequires:	pkgconfig(pciaccess)
BuildRequires:	pkgconfig(libproc2)
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xorg-server) >= 1.3
BuildRequires:	pkgconfig(xorg-macros) >= 1.0.1
BuildRequires:	pkgconfig(xproto) >= 1.0.0
BuildRequires:	pkgconfig(xvmc) >= 1.0.1
BuildRequires:	pkgconfig(xrandr)
BuildRequires:  pkgconfig(xmlrpc)
BuildRequires:  pkgconfig(valgrind)
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:	gtk-doc
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	byacc
BuildRequires:	python-docutils
BuildRequires:  leg

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

%package devel
Summary:   Xorg X11 Intel video driver development package
Group:     Development/C
Requires:  %{name} = %{EVRD}
Provides:  xorg-x11-drv-intel-devel = %{EVRD}

%description devel
X.Org X11 Intel video driver development package.


%prep
%autosetup -n %{oname}-%{version} -p1

%build
%meson -Doverlay=enabled -Doping=disabled -Ddocs=disabled
%meson_build

%install
%meson_install

# remove docs
rm -rf %{buildroot}%{_datadir}/gtk-doc/html/intel-gpu-tools


%files
%doc NEWS README.md
%{_bindir}/amd_*
%{_bindir}/code_cov_*
%{_bindir}/igt_*
%{_bindir}/i915-perf*
%{_bindir}/intel*
%{_bindir}/dpcd_reg
%{_bindir}/msm_dp_compliance
%{_bindir}/lsgpu
%{_bindir}/gputop
%{_bindir}/power
%{_bindir}/xe-perf*
%{_datadir}/%{oname}/
%{_libdir}/lib*.so.0
%{_libdir}/lib*.so.1.5
%{_libexecdir}/%{oname}/
%{_mandir}/man1/intel*.1*

%files devel
%{_libdir}/pkgconfig/intel-gen4asm.pc
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/xe-oa.pc
%{_includedir}/xe-oa/
%{_libdir}/pkgconfig/i915-perf.pc
%{_includedir}/i915-perf/
