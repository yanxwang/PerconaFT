#!/usr/bin/bash

start_time=$(date +%s)  # Capture start timestamp

rm -rf /tmp/test-dump-ft.out
rm -rf /mnt/nvme/percona
mkdir /mnt/nvme/percona
rm -rf /tmp/percona500M.io

iostat -ymxt 1 > /tmp/percona500M.io &
ipid=$!
echo "Forked $ipid"

./db-insert --keysize 8 --valsize 100 --noserial --cachesize 64000000000 --periter 500000000 --nolog --env /mnt/nvme/percona 1
# sync
sleep 5

kill $ipid
echo "Killed $ipid"

end_time=$(date +%s)  # Capture end timestamp
runtime=$((end_time - start_time))  # Calculate runtime in seconds

# Convert seconds to minutes
runtime_minutes=$(echo "scale=2; $runtime / 60" | bc)
echo "Runtime: $runtime_minutes minutes"
