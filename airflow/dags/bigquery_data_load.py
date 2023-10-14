import os
from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryCreateEmptyDatasetOperator,
    BigQueryExecuteQueryOperator,
)
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.transfers.gcs_to_gcs import GCSToGCSOperator
from airflow.utils.dates import days_ago

PROJECT_ID = Variable.get('project')
LANDING_BUCKET = Variable.get('landing_bucket')
BACKUP_BUCKET = Variable.get('backup_bucket')

default_arguments = {'owner': 'Niko', 'start_date': days_ago(1)}

def list_objects(bucket=None):
        hook = GCSHook()
        storage_objects = hook.list(bucket)
        return storage_objects

def move_objects(source_bucket=None, destination_bucket=None, prefix=None, **kwargs):
    storage_objects = kwargs['ti'].xcom_pull(task_ids='list_files')

    hook = GCSHook()

    for storage_object in storage_objects:
        destination_object = storage_object
        if prefix:
           destination_object = "{}/{}".format(prefix, storage_object)
        hook.copy(source_bucket, storage_object, destination_bucket, destination_object)
        hook.delete(source_bucket, storage_object)

DATASET_NAME = os.environ.get("GCP_DATASET_NAME", 'vehicle_analytics')
TABLE_NAME = os.environ.get("GCP_TABLE_NAME", 'history')

with DAG(
    'bigquery_data_load', 
    schedule='@hourly', 
    catchup=False, 
    default_args=default_arguments,
    max_active_runs=1,
    user_defined_macros={'project': 'airflow-400718'}
) as dag:
        
        list_files = PythonOperator(
                task_id='list_files',
                python_callable=list_objects,
                op_kwargs={'bucket': 'n1-logistics-landing-bucket'}
        )
        
        create_test_dataset = BigQueryCreateEmptyDatasetOperator(
            task_id='create_airflow_dataset', 
            dataset_id=DATASET_NAME
        )

        load_data = GCSToBigQueryOperator(
            task_id='gcs_to_big_query',
            bucket='n1-logistics-landing-bucket',
            source_objects=['*'],
            source_format='CSV',
            skip_leading_rows=1,
            field_delimiter=',',
            destination_project_dataset_table=f"{PROJECT_ID}.{DATASET_NAME}.{TABLE_NAME}",
            create_disposition='CREATE_IF_NEEDED',
            write_disposition='WRITE_TRUNCATE',
            gcp_conn_id='google_cloud_default',
        )

        query = '''
        SELECT * except (rank)
        FROM (
            SELECT
                *,
                ROW_NUMBER() OVER (
                    PARTITION BY vehicle_id ORDER BY DATETIME(date, TIME(hour, minute, 0)) DESC
                ) as rank
            FROM `{{ project }}.vehicle_analytics.history`) as latest
        WHERE rank = 1;
        '''

        create_table = BigQueryExecuteQueryOperator(
            task_id='create_table',
            sql=query,
            destination_dataset_table='vehicle_analytics.latest',
            write_disposition='WRITE_TRUNCATE',
            create_disposition='CREATE_IF_NEEDED',
            use_legacy_sql=False
        )

        move_files = PythonOperator(
               task_id='move_files',
               python_callable=move_objects,
               op_kwargs={
                      'source_bucket': LANDING_BUCKET',
                      'destination_bucket': BACKUP_BUCKET',
                      "prefix": "{{ ts_nodash }}",
               },
               provide_context=True
        )
            
list_files >> create_test_dataset >> load_data >> create_table >> move_files