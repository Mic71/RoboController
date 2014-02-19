Name: libmodbus
Version: 3.0.1
Release: 1%{?dist%}
Summary: A Modbus library written in C

Group: Applications/System
License: LGPLv2.1+
URL: http://www.libmodbus.org/
Source0: https://github.com/downloads/stephane/libmodbus/libmodbus-%{version}.tar.gz

Packager: Stéphane Raimbault
Provides: libmodbus=%{version}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gcc, autoconf, automake, libtool

%description
The library is written in C and designed to run on Linux, Mac OS X, FreeBSD and
QNX and Windows.

This package contains the libmodbus shared library.

%package devel
Summary: Development files for the libmodbus library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, pkgconfig

%description devel
The library is written in C and designed to run on Linux, Mac OS X, FreeBSD and
QNX and Windows.

This package contains libmodbus related development libraries and header files.

%prep
%setup -q

autoreconf

%build
%configure
make %{?_smp_mflags}

%install
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}
%{__make} check
%makeinstall

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)

%doc AUTHORS MIGRATION NEWS COPYING* README.rst

%{_libdir}/libmodbus.so.5
%{_libdir}/libmodbus.so.5.0.0

%files devel
%defattr(-,root,root)
%{_includedir}/modbus/modbus.h
%{_includedir}/modbus/modbus-rtu.h
%{_includedir}/modbus/modbus-tcp.h
%{_includedir}/modbus/modbus-version.h

%{_libdir}/libmodbus.la
%{_libdir}/pkgconfig/libmodbus.pc
%{_libdir}/libmodbus.so

%{_mandir}/man7/libmodbus.7.gz
%{_mandir}/man3/modbus_close.3.gz
%{_mandir}/man3/modbus_connect.3.gz
%{_mandir}/man3/modbus_flush.3.gz
%{_mandir}/man3/modbus_free.3.gz
%{_mandir}/man3/modbus_get_byte_from_bits.3.gz
%{_mandir}/man3/modbus_get_byte_timeout.3.gz
%{_mandir}/man3/modbus_get_float.3.gz
%{_mandir}/man3/modbus_get_header_length.3.gz
%{_mandir}/man3/modbus_get_response_timeout.3.gz
%{_mandir}/man3/modbus_get_socket.3.gz
%{_mandir}/man3/modbus_mapping_free.3.gz
%{_mandir}/man3/modbus_mapping_new.3.gz
%{_mandir}/man3/modbus_new_rtu.3.gz
%{_mandir}/man3/modbus_new_tcp_pi.3.gz
%{_mandir}/man3/modbus_new_tcp.3.gz
%{_mandir}/man3/modbus_read_bits.3.gz
%{_mandir}/man3/modbus_read_input_bits.3.gz
%{_mandir}/man3/modbus_read_input_registers.3.gz
%{_mandir}/man3/modbus_read_registers.3.gz
%{_mandir}/man3/modbus_receive_confirmation.3.gz
%{_mandir}/man3/modbus_receive_from.3.gz
%{_mandir}/man3/modbus_receive.3.gz
%{_mandir}/man3/modbus_reply_exception.3.gz
%{_mandir}/man3/modbus_reply.3.gz
%{_mandir}/man3/modbus_report_slave_id.3.gz
%{_mandir}/man3/modbus_rtu_get_serial_mode.3.gz
%{_mandir}/man3/modbus_rtu_set_serial_mode.3.gz
%{_mandir}/man3/modbus_send_raw_request.3.gz
%{_mandir}/man3/modbus_set_bits_from_bytes.3.gz
%{_mandir}/man3/modbus_set_bits_from_byte.3.gz
%{_mandir}/man3/modbus_set_byte_timeout.3.gz
%{_mandir}/man3/modbus_set_debug.3.gz
%{_mandir}/man3/modbus_set_error_recovery.3.gz
%{_mandir}/man3/modbus_set_float.3.gz
%{_mandir}/man3/modbus_set_response_timeout.3.gz
%{_mandir}/man3/modbus_set_slave.3.gz
%{_mandir}/man3/modbus_set_socket.3.gz
%{_mandir}/man3/modbus_strerror.3.gz
%{_mandir}/man3/modbus_write_and_read_registers.3.gz
%{_mandir}/man3/modbus_write_bits.3.gz
%{_mandir}/man3/modbus_write_bit.3.gz
%{_mandir}/man3/modbus_write_registers.3.gz
%{_mandir}/man3/modbus_write_register.3.gz

%changelog
* Mon Jul 18 2011 Stéphane Raimbault <stephane.raimbault@gmail.com> - 3.0.1-1
- new upstream release

* Thu Jul 11 2011 Stéphane Raimbault <stephane.raimbault@gmail.com> - 3.0.0-1
- revert the license to LGPLv2.1+
- new spec file generated by autoconf
- add documentation, devel package and various changes

* Sun Jun 5 2011 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.9.4-1
- new upstream release

* Mon Jan 10 2011 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.9.3-1
- new upstream release

* Mon Oct 5 2010 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.9.2-1
- new upstream release

* Fri Jul 2 2008 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.0.1-1
- new upstream release

* Fri May 2 2008 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.0.0-1
- integrate extern_for_cpp in upstream.
- update the license to version LGPL v3.

* Tue Apr 30 2008 Todd Denniston <Todd.Denniston@ssa.crane.navy.mil> - 1.9.0-2
- get the license corrected in the spec file.
- add a URL for where to find libmodbus.
- tweak the summary and description.

* Tue Apr 29 2008 Todd Denniston <Todd.Denniston@ssa.crane.navy.mil> - 1.9.0-1
- upgrade to latest upstream (pre-release)
- port extern_for_cpp patch to 1.9.0

* Tue Apr 29 2008 Todd Denniston <Todd.Denniston@ssa.crane.navy.mil> - 1.2.4-2_tad
- add a patch to allow compiling with c++ code.

* Mon Apr 28 2008 Todd Denniston <Todd.Denniston@ssa.crane.navy.mil> - 1.2.4-1_tad
- build spec file.
- include patch for controling error-treat.