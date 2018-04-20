#!/bin/bash

# echo "[INFO] Creating database and table if they do not exist..."

mysql --host headnode1.rocm --user=root --password=admin -e "CREATE DATABASE IF NOT EXISTS user_db;"
mysql --host headnode1.rocm --user=root --password=admin -e " USE user_db; CREATE TABLE IF NOT EXISTS processed_msg (Name varchar(255),Age int(255), Status varchar(255),Income int(255) );"

# echo "[INFO] Writing data to SQL"

mysqlimport --ignore-lines=1 --fields-terminated-by=, --host=headnode1.rocm --local --user=root --password=admin user_db /working_dir/processed_msg.csv > /dev/null 2>&1

# echo "[INFO] Successfully imported data to MySQL"
exit 0
