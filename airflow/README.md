# Airflow Simple ETL: Raw JSON to MySQL table 

## Setup

* Make sure you have Apache Airflow, RabbitMQ, MySQL server and Celery in your local machine and/or workers 
* Clone this git repository 
* Go to the airflow/ folder 
* Place working_dir/ in your root dir ( / ) 
* Place data_dir /in your root dir ( / ) 
* Place the dags/ folder in your AIRFLOW_HOME dir
* Place the airflow.cfg fle in your AIRFLOW_HOME dir
* Replace values inside <..> in airflow.cfg with values for your environment
* If you are executing the airflow worker as the root user, go to “~/.bashrc” and set the following variable “export C_FORCE_ROOT=true”
* Perform the above steps for all your hosts
* Start your workers in  the following way: "airflow worker -q rawToSQL " 
* Trigger the DAG execution in your webserver
