# These and other macros are documented in dhd/droid-hal-device.inc

%define device flo
%define vendor asus

%define vendor_pretty Asus
%define device_pretty Nexus 7 (2013 WiFi)

%define installable_zip 1

# Entries migrated from the old rpm/droid-hal-hammerhead.spec
%define enable_kernel_update 1

%include rpm/dhd/droid-hal-device.inc
