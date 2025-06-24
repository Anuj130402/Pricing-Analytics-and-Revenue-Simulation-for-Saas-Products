from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Import your scripts
from scripts.etl import run_etl
from scripts.forecast import run_forecast
from scripts.simulate import run_simulation

default_args = {
    'owner': 'data_team',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='pricing_analytics_dag',
    default_args=default_args,
    schedule_interval='@daily',  # or '@weekly'
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    etl_task = PythonOperator(
        task_id='run_etl',
        python_callable=run_etl
    )

    forecast_task = PythonOperator(
        task_id='run_forecast',
        python_callable=run_forecast
    )

    simulate_task = PythonOperator(
        task_id='run_simulation',
        python_callable=run_simulation
    )

    etl_task >> forecast_task >> simulate_task
