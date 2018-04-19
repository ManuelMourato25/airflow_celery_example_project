from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

dag_args = {
    'owner': 'manuelmourato',
    'depends_on_past': False,
    'start_date': datetime(2018, 4, 18, 0, 0, 0),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'queue': 'rawToSQL'
}

task_args = {
    'execution_timeout': timedelta(minutes=5),
    'depends_on_past': True,
    'wait_for_downstream': True,
    'retries': 1,
    'retry_delay': timedelta(seconds=30)
}


dag = DAG('rawFile_to_SQL', default_args=dag_args,
          schedule_interval=timedelta(minutes=10), dagrun_timeout=timedelta(minutes=30))

get_raw_data_task = BashOperator(
    task_id='read_data_from_raw_file',
    bash_command='/working_dir/fetch_file_from_other_folder.sh ',
    dag=dag)

process_data_task = BashOperator(
    task_id='process_data_to_csv_format',
    bash_command='python /working_dir/json_to_csv.py ',
    dag=dag)

send_to_sql_task = BashOperator(
    task_id='insert_to_sql',
    bash_command='/working_dir/csv_to_sql.sh ',
    dag=dag)


get_raw_data_task.set_downstream(process_data_task)
process_data_task.set_downstream(send_to_sql_task)

