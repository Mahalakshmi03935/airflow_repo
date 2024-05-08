from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

# Define your DAG
default_args = {
    'owner': 'maha',
    'start_date': datetime(2024, 5, 7),
    'retries': 1,
}

dag = DAG(
    'bash_dag',
    default_args=default_args,
    description='Bash DAG',
    schedule_interval=None,
)

# Define BashOperator tasks within the DAG
task_1 = BashOperator(
    task_id='task_1',
    bash_command='echo "Executing Task 1"',
    dag=dag,
)

task_2 = BashOperator(
    task_id='task_2',
    bash_command='echo "Executing Task 2"',
    dag=dag,
)

# Define the order of execution 
task_1 >> task_2  
