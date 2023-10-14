from airflow import DAG
from airflow.utils.dates import days_ago
# dag = DAG('core_concepts', schedule_interval='@daily', catchup=False)
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from airflow.utils.helpers import chain, cross_downstream

from random import seed, random

default_arguments = {'owner': 'Niko', 'start_date': days_ago(1)}


"""
Directed Acyclic Graphs(DAGs)

Task
represents a node in the graph. it is a unit of work that gets executed by workers. 
A task is always defined by an operator.

Operator
is the actual logic behind a task. It defines what sort of actions are performed as part of a task.
- action operators(they perform actions or tell a system to perform an action)
- transfer operators (they move data)
- sensors (they keep runing unit a criteria is met)

all operators derive from BaseOperator class (airflow.models.baseoperator)
https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/baseoperator/index.html
"""
with DAG(
    'core_concepts', 
    schedule_interval='@daily', 
    catchup=False,
    default_args=default_arguments
    ) as dag:

    bash_task = BashOperator(
        task_id='bash_command', bash_command='echo $TODAY', env={'TODAY': '2023-10-01'}
    )

    def print_random_number(number):
        seed(number)
        print(random())
    
    python_task = PythonOperator(
        task_id='python_function', python_callable=print_random_number, op_args=[1]
    )

bash_task >> python_task

# bash_task.set_downstream(python_task)

# op1 >> op2 >> op3 >> op4

# chain(bash_task, python_task)

# cross_downstream([op1, op2], [op3, op4])    

# [op1, op2] >> op3
# [op1, op2] >> op4