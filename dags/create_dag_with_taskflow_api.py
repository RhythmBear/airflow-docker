from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    'owner': 'rhythmbear',
    'retries':5,
    'retry_delay': timedelta(minutes=5)
}

# Define Dag using the dag decorator

@dag(dag_id='dag_with_taskflow_api_v2', 
     default_args=default_args,
     start_date=datetime(2023, 9, 30),
     schedule_interval='@daily')
def hello_world_etl():
    
    # Define each individual task using the task decorator.
    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name' : 'Emmanuel',
            'last_name': 'Adepoju'
        }
    
    @task()
    def get_age():
        return 27
    
    @task()
    def greet(first_name, last_name, age):
        print(f'Hello World! My name is {first_name} {last_name} and i am {age} years old tomorrow.')

    name_dict = get_name()
    age = get_age()

    greet(first_name=name_dict['first_name'],
          last_name=name_dict['last_name'],
            age=age)


greet_dag = hello_world_etl()