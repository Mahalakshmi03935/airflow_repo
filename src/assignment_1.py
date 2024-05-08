from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

# Define the default arguments for DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 8),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Defining the DAG
dag = DAG(
    'simple_demo_dag',
    default_args=default_args,
    description='A simple demo DAG',
    schedule_interval=timedelta(days=1),  # Run the DAG daily
)

# Define the tasks
task1 = DummyOperator(task_id='task1', dag=dag)
task2 = DummyOperator(task_id='task2', dag=dag)
task3 = DummyOperator(task_id='task3', dag=dag)
task4 = DummyOperator(task_id='task4', dag=dag)

# Define the task dependencies
task1 >> task2 >> task3 >> task4

