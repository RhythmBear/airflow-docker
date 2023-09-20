from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Create Default arguments for dag
default_args = {
    'owner': 'rhythmbear',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
    }

# Create DAG Instance 
with DAG(
    default_args=default_args,
    dag_id='my_first_dag_v2',
    description='This is the first dag i am creating',
    start_date=datetime(2023, 9, 20, 5),
    schedule_interval='@hourly'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo hello World, this is the first task'
        )
    
    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo I am the 2nd task, I run after the first'
        )
    
    task1 >> task2
    