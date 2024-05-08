from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define DAG structure
with DAG(
    dag_id="trigger_dag",
    schedule_interval=None,
    start_date=datetime(2024, 5, 8),  # Add start_date parameter here
) as dag:

    def generate_data():
        
        print("Generating data")

    def process_data():
        
        print("Processing data")

    # Generate data task
    generate_data_task = PythonOperator(
        task_id="generate_data",
        python_callable=generate_data,
    )

    # Process data task, triggered by generate_data_task
    process_data_task = PythonOperator(
        task_id="process_data",
        python_callable=process_data,
        trigger_rule="success",
    )

    # Set task dependencies
    generate_data_task >> process_data_task
