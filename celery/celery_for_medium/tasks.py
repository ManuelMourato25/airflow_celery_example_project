from __future__ import absolute_import
from .celery import json_to_sql_Celery_app
import os

@json_to_sql_Celery_app.task(bind=True,name='json_to_sql.extract_raw_file', default_retry_delay=5,retry_kwargs={'max_retries': 2})
def extract_data_raw_fle(self):
    """
    Bring raw file to working directory
    :return process_status: a message telling if the insert to kafka was sucessfull
    :rtype string
    """

    print("[INFO] Starting execution of task {0}".format(self.request.id))

    extract_raw_json_command="/working_dir/fetch_file_from_other_folder.sh "
    os.system(extract_raw_json_command)

    print("[INFO] Task {0} done".format(self.request.id))


@json_to_sql_Celery_app.task(bind=True,name='json_to_sql.process_raw_data', default_retry_delay=5,retry_kwargs={'max_retries': 2})
def process_raw_data(self):
    """
    Convert JSON to CSV format
    :return process_status: a message telling if the data processing was sucessfull
    :rtype string
    """
    print("[INFO] Starting execution of task {0}".format(self.request.id))


    processing_data_command="python /working_dir/json_to_csv.py "
    os.system(processing_data_command)

    print("[INFO] Task {0} done".format(self.request.id))

@json_to_sql_Celery_app.task(bind=True,name='json_to_sql.send_to_mysql', default_retry_delay=5,retry_kwargs={'max_retries': 2})
def send_data_to_mysql(self):
    """
    Send data to a MySQL table
    :return process_status: a message telling if the insert to mysql was sucessfull
    :rtype string
    """
    print("[INFO] Starting execution of task {0}".format(self.request.id))

    send_data_mysql_command="/working_dir/csv_to_sql.sh "
    os.system(send_data_mysql_command)

    print("[INFO] Task {0} done".format(self.request.id))
