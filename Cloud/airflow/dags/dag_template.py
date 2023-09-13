"""
This module defines the Airflow DAG for the Red Wine MLOps lifecycle. The DAG includes tasks
for various stages of the pipeline, including data reading, data processing, model training, 
and selecting the best model. 

The tasks are defined as functions and executed within the DAG. The execution order of the tasks 
is defined using task dependencies.

Note: The actual logic inside each task is not shown in the code, as it may reside in external 
script files.

The DAG is scheduled to run every day at 12:00 AM.

Please ensure that the necessary dependencies are installed and accessible for executing the tasks.
"""

from datetime import datetime
from airflow import DAG
from airflow.decorators import task
import sys

# Import all functions to be used
sys.path.append("src/project_template/") 
from Data.read_data import read_data
from Process.data_processing import data_processing
from Models.model_training import model_training
from Deployment.Select_Best_Model import select_best_model

with DAG(
    'Template_MLOps_lifecycle', # Add the DAG name
    description='MLOps lifecycle', # Add a description
    schedule_interval='* 12 * * *', 
    catchup=False,
    start_date=datetime.now()
) as dag:

    # Define as many task as needed
    @task
    def read_data_task():
        print(f"read data task:")
        return read_data()

    @task
    def data_processing_task(df=None):
        print(f"data processing task:")
        return data_processing(df)

    @task
    def model_training_task(res=None):
        print(f"ElasticNet model training task train_x: {res}")
        return model_training(res)
    
    @task
    def select_best_model_task():
        print("Selection of the best model task:")
        return select_best_model()
    

    # Instantiate each task and define task dependencies
    read_data_result = read_data_task()
    processing_result = data_processing_task(read_data_result)
    model_training_result = model_training_task(processing_result)
    select_best_model_result = select_best_model_task()

    # Define the order of the pipeline
    read_data_result >> processing_result >> [model_training_result] >> select_best_model_result