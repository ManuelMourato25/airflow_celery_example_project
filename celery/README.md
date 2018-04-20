# Celery Simple ETL: Raw JSON to MySQL table

## Setup

* Make sure you have RabbitMQ, MySQL server and Celery in your local machine and/or workers
* Clone this git repository
* Create a database called celery in your MySQL server, which will serve as backend for your task results
* Go to the airflow/ folder
* Place working_dir/ in your root dir ( / )
* Place data_dir /in your root dir ( / )
* Place the dags/ folder in your AIRFLOW_HOME dir
* Place the airflow.cfg fle in your AIRFLOW_HOME dir
* Perform the above steps for all your hosts
* Go inside the celery/ folder
* Start your workers in  the following way: "celery worker --app celery_for_medium.celery --loglevel=INFO -n worker1@<WORKER_SERVER> -Q json_to_sql_celery"
* Trigger the execution of the tasks by running "python execution_script.py"

