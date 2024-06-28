from airflow.decorators import dag, task # type: ignore
from datetime import datetime

@dag(
        dag_id = 'minha_dag',
        description = 'bla bla bla',
        schedule = '5 0 * 8 *',
        start_date = datetime(2023,3,24),
        catchup = False
)
def pipeline():

    @task
    def primeira_atividade():
        print("1")
    @task
    def segunda_atividade():
        print("2")
    @task
    def terceira_atividade():
        print("3")
    @task
    def quarta_atividade():
        print("4")

    
    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    t1 >> t2 >> t3 >> t4

pipeline()