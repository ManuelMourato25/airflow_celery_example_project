#!/bin/bash


echo "[INFO] Fetching file from file directory to local environment..."

if [ ! -d "/working_dir" ] ;then
    echo "[INFO] Creating working directory..."
    mkdir -p /working_dir/
fi

if [ ! -f "/data_dir/raw_file" ] ; then
    echo "[ERROR] No file in destination. Exiting"
    exit 1
fi

sudo cp /data_dir/raw_file /working_dir/

echo "[INFO] Retrieved file successfully"
exit 0
