#!/usr/bin/bash

rowlen=100
keylen=8
nr=100000000
devname="sda"

echo "nr : $nr"

echo -e "count\tIOwGB\tIOwMB/s\tUwGB\tWamp"
gbwritten=$( echo $rowlen $keylen $nr | awk '{ printf "%.6f", (($1 + $2) * $3) / (1000*1000*1000.0) }' )
grep $devname /tmp/percona500M.io | awk '{ c += 1; wmb += $9 } END { printf "%s\t%.1f\t%.1f\t%.1f\t%.1f\n", c, wmb/1000.0, wmb / c, gbw, (wmb/1000.0)/gbw }' gbw=$gbwritten
