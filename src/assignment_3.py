from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'name',
    'start_date': datetime(2024, 5, 5),
    'retries': 1,
    'retry_delay': timedelta(seconds=1)
}

dag_a = DAG(
    'PARENT_DAG_1',
    default_args=default_args,
    description='An example Airflow DAG with three tasks',
    # schedule_interval='28 11 * * *'
)

def task1_function():
    import time
    print("Executing Task 1")
    # time.sleep(5 * 60)

def task2_function():
    import time
    print("Executing Task 2")
    # time.sleep(8 * 60)

def task3_function():
    import time
    print("Executing Task 3")
    # time.sleep(2 * 60)

task1 = PythonOperator(
    task_id='task1',
    python_callable=task1_function,
    dag=dag_a
)

task2 = PythonOperator(
    task_id='task2',
    python_callable=task2_function,
    dag=dag_a
)

task3 = PythonOperator(
    task_id='task3',
    python_callable=task3_function,
    dag=dag_a
)

task1 >> task2 >> task3
