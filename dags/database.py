import os
from datetime import datetime

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

#ENV_ID = os.environ.get("SYSTEM_TESTS_ENV_ID")
DAG_ID = "postgres_operator_dag"

with DAG(
    dag_id=DAG_ID,
    start_date=datetime(2024, 5, 6),
    schedule="@once",
    catchup=False,
) as dag:
    create_windturbine_table = PostgresOperator(
        task_id="create_windturbine_table",
        postgres_conn_id="postgres",
        sql="sql/windturbine_schema.sql",
    )