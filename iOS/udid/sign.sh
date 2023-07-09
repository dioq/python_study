#!/bin/sh

certificate="Apple Development: Lin Sheng (3AHP8847PU)"
mobileconfig=./mobileconfig.plist
outfile=./udid.mobileconfig

/usr/bin/security cms -S -N "$certificate" -i "${mobileconfig}" -o "${outfile}"
