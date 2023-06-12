import pendulum

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLColumnCheckOperator

from trino_operator import TrinoOperator

## This method is called by task2 (below) to retrieve and print to the logs the return value of task1
def print_command(**kwargs):
        task_instance = kwargs['task_instance']
        print('Return Value: ',task_instance.xcom_pull(task_ids='uploads_performed',key='return_value'))

with DAG(
    default_args={
        'depends_on_past': False
    },
    dag_id='starburst-galaxy-example',
    schedule_interval='0 8 * * *',
    start_date=pendulum.datetime(2022, 10, 27, tz="US/Central"),
    catchup=False,
    tags=['demo'],
) as dag:

    ## Task 1 runs a Trino select statement to count the number of records 
    ## in the tpch.tiny.customer table
    ## Ouput of this should be 1500 and printed in task2
    task1 = TrinoOperator(
      task_id='uploads_performed',
      trino_conn_id='galaxy_connection',
      sql='''
        select
                count(*) as customers
        from
            tpch.tiny.customer;
                    ''')
    
    ## Task 2 is a Python Operator that runs the print_command method above 
    task2 = PythonOperator(
      task_id = 'print_number_of_uploads',
      python_callable = print_command,
      provide_context = True,
      dag = dag)
    

    ## Task 3 is SQL DQ Check Operator that validates that the distinct values in custkey is 1500
    task3 = SQLColumnCheckOperator(
        task_id="data_validation_check",
        conn_id="galaxy_connection",
        table="tpch.tiny.customer",
        column_mapping={
            "custkey": {
                "distinct_check": {"equal_to": 1500},
            }
        }
    )
    # Defining Execution Order
    task1 >> task2 >> task3
