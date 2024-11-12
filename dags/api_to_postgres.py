from airflow.decorators import task, dag

from include.controller import fetch_pokemon_data, add_pokemon_to_db, generate_random_number

from datetime import datetime


@dag(dag_id="api_postgres",
     description="pipeline_to_generate_pokemon",
     start_date=datetime(2024,3,24),
     schedule="* * * * *",
     catchup=False)
def api_postgres():

    @task(task_id='generate_random_number')
    def generate_random_number():
        return generate_random_number()
    
    @task(task_id='fetch_pokemon_data')
    def task_fetch_pokemon_data(randon_number):
        return fetch_pokemon_data(randon_number)
    
    @task(task_id='add_pokemon_to_db')
    def task_add_pokemon_to_db(pokemon_data):
        add_pokemon_to_db(pokemon_data)

    @task
    def print_success(response):
        print(response)
    
    t1 = generate_random_number()
    t2 = task_fetch_pokemon_data(t1)
    t3 = task_add_pokemon_to_db(t2)
    t4 = print_success(t3)

    t1 >> t2 >> t3 >> t4

api_postgres()