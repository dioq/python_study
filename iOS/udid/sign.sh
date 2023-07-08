#!/bin/sh

certificate="Apple Development: Lin Sheng (3AHP8847PU)"
mobileconfig=./udid.mobileconfig
outfile=./udid_signed.mobileconfig

/usr/bin/security cms -S -N "$certificate" -i "${mobileconfig}" -o "${outfile}"
