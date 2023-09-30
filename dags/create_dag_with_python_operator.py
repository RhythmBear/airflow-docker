from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "rhythmbear",
    "retries": 5,
    "retries_delay": timedelta(minutes=2)
}

# Define Task
def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"Hello {first_name} of the House {last_name}! It's good to see you are now {age} years old")

def get_name(ti):
    ti.xcom_push(key='first_name', value='Emmanuel')
    ti.xcom_push(key='last_name', value='Adepoju')

def get_age(ti):
    ti.xcom_push(key='age', value=29)
    

# Create DAG Instance
with DAG(
    default_args=default_args,
    dag_id='our_dag_with_pythonoperator_v6',
    description="Our first Dag using python Operators",
    start_date=datetime(2023, 9, 28),
    schedule_interval="@daily"
) as dag:
    task1 = PythonOperator(
        task_id="greet_hello",
        python_callable=greet,
    )
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name

    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    [task2, task3] >> task1
