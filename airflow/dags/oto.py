from airflow.decorators import dag, task # type: ignore
from datetime import datetime
from airflow.operators.bash_operator import BashOperator # type: ignore

@dag(
        dag_id = 'ETL',
        description = 'Pipeline of ETL',
        schedule = '5 0 * 8 *',
        start_date = datetime(2023,3,24),
        catchup = False
)

def pipeline():

    run_spider = BashOperator(
    task_id='run_spider',
    bash_command='cd /usr/local/airflow/tasks/src/coleta && scrapy crawl mercadolivre -o data.csv'
)
    transformation = BashOperator(
    task_id='transformation',
    bash_command='python /usr/local/airflow/tasks/src/coleta/tranformação/transformação.py'
)
    load_db = BashOperator(
    task_id='load_db',
    bash_command='python /usr/local/airflow/tasks/src/coleta/load_database/load.py'
)
    

    run_spider >> transformation >> load_db


pipeline()