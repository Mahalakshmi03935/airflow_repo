from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.sensors.filesystem import FileSensor
from airflow.operators.sensors.http_sensor import HttpSensor
from airflow.operators.sensors.time_sensor import TimeSensor
from datetime import datetime, timedelta

# Define DAG structure
with DAG(
    dag_id="sensor_example_dag",
    schedule_interval=timedelta(days=1),  
    start_date=datetime(2024, 5, 8),  
    catchup=False,  
) as dag:

    # Define sensors
    file_sensor = FileSensor(
        task_id="file_sensor",
        filepath="/data/input/file.txt",  
        poke_interval=60,  
        timeout=600,  
    )

    http_sensor = HttpSensor(
        task_id="http_sensor",
        http_conn_id="http_default",  
        endpoint="/health",  
        request_params={},  
        response_check=lambda response: response.status_code == 200,  
        poke_interval=60,  
        timeout=600,  
    )

    time_sensor = TimeSensor(
        task_id="time_sensor",
        target_time=datetime(2024, 5, 9, 0, 0), 
        poke_interval=60,  
    )

    # Define tasks
    task1 = DummyOperator(task_id="task1")
    task2 = DummyOperator(task_id="task2")
    task3 = DummyOperator(task_id="task3")

    # Set task dependencies
    file_sensor >> task1  # file_sensor triggers task1
    http_sensor >> task2  # http_sensor triggers task2
    time_sensor >> task3  # time_sensor triggers task3
