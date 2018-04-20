"""
Celery application to orchestrate tasks to insert data from a JSON file to MySQL
:developer: Manuel Mourato
:date: 20/04/2018

"""

from __future__ import absolute_import, unicode_literals
from celery import Celery


json_to_sql_Celery_app = Celery(main="celery_for_medium.celery", broker="amqp://guest:guest@headnode1.rocm:5672/", backend="db+mysql://root:admin@headnode1.rocm/celery", include=["celery_for_medium.tasks"])

if __name__ == '__main__':
    json_to_sql_Celery_app.start()
