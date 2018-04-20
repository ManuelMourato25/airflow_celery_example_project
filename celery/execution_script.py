from __future__ import absolute_import, unicode_literals
from .tasks import extract_data_raw_fle,process_raw_data,send_data_to_mysql
from datetime import datetime

if __name__ == '__main__':
    while(True):
        start=datetime.now()
        print("[INFO] Starting set of tasks")
        extract_data_raw_fle.apply_async(eta=start,expiration=600,queue='json_to_sql_celery')
        process_raw_data.apply_async(expiration=600,queue='json_to_sql_celery')
        send_data_to_mysql.apply_async(expiration=600,queue='json_to_sql_celery')
        finish=datetime.now()
        print("[INFO] Ending set of tasks")
