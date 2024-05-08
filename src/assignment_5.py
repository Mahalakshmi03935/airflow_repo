from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

# Define DAG structure
with DAG(
    dag_id="example_dag",
    schedule_interval=timedelta(days=1),  
    start_date=datetime(2024, 5, 8),  
    catchup=False,  
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 2,  # Retry the task twice on failure
        'retry_delay': timedelta(minutes=5),  # Delay between retries
    },
) as dag:

    # Define tasks
    task1 = DummyOperator(task_id="task1")
    task2 = DummyOperator(task_id="task2")
    task3 = DummyOperator(task_id="task3")
    task4 = DummyOperator(task_id="task4")

    # Set task dependencies
    task1 >> task2  # task1 triggers task2
    task1 >> task3  # task1 also triggers task3
    task2 >> task4  # task2 triggers task4
    task3 >> task4  # task3 also triggers task4
