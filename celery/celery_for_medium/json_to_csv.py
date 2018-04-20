import csv
import json

with open('/working_dir/raw_file', 'r') as raw_data:
    raw_file = raw_data.read()

raw_file = json.loads(raw_file)

with open("/working_dir/processed_msg.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Name", "Age", "Status", "Income"])
    for line in raw_file:
        writer.writerow(
                    [line["Name"],
                    line["Client_data"]["Age"],
                    line["Client_data"]["Status"],
                    line["Client_data"]["Income"]])

