from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import yaml
import os
import sys

from KAFKA.producer import run_producer
from KAFKA.consumer import run_consumer
from ETL_Process.Data_Extraction.data_extraction import DataExtractorclass
from ETL_Process.Data_Transformation.data_transformation import DataTransformerclass
from ETL_Process.Data_Loading.data_loading import load_data_to_s3


def producer():
    run_producer()

def Consumer():
    run_consumer()

def Data_extraction_from_csv():
    data_extraction_obj = DataExtractorclass()
    data_extraction_obj.extract_csv_from_folder()

def Data_transformation_on_csv():
    data_transformation_obj = DataTransformerclass()
    data_transformation_obj.transformkafka()

def Load_into_s3():
    load_data_to_s3()




default_args = {
    'owner': 'airflow',
    'start_date':days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

dag = DAG(
    dag_id = "Final_ETL_dag",
    default_args = default_args,
    descriptions = 'This is my ETL pipeline',
    scheduled_interview = '@daily'
)


trigger_producer = PythonOperator(
    task_id = 'trigger_producer',
    python_callable = producer,
    provide_context = True,
    dag = dag
)


trigger_consumer = PythonOperator(
    task_id = 'trigger_consumer',
    python_callable = producer,
    provide_context = True,
    dag = dag
)


trigger_data_extraction = PythonOperator(
    task_id = 'trigger_data_extraction',
    python_callable = Data_extraction_from_csv,
    provide_context = True,
    dag = dag
)


trigger_data_transformation = PythonOperator(
    task_id = 'trigger_data_transformations',
    python_callable = Data_transformation_on_csv,
    provide_context = True,
    dag = dag
)


trigger_data_loading_to_s3= PythonOperator(
    task_id = 'trigger_data_loading_to_csv',
    python_callable = Load_into_s3,
    provide_context = True,
    dag = dag
)

trigger_producer >> trigger_consumer
trigger_consumer >> trigger_data_extraction
trigger_data_extraction >> trigger_data_transformation
trigger_data_transformation >> trigger_data_loading_to_s3
