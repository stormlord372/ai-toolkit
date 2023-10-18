"""
This module provides the register_experiment function, which is utilized by the pipeline orchestrator (Airflow) to 
register the experiment into IDS TrueConnector. If any additional auxiliary functions are required to accomplish 
this step, they can be defined within the same script or separated into different scripts and included in the Data
directory.
"""

import config
from Deployment.main import handle_post
from Data.rest_ids_consumer_connector import RestIDSConsumerConnector

def register_experiment():
    """
        This function implements the logic to regsiter a new experiment into IDS consumer tureconnector
    """
    ids_consumer = RestIDSConsumerConnector()
    print("Register experiment task:")

    if ids_consumer.is_artifact_internal_registered_by_resource_title(config.MLFLOW_EXPERIMENT,config.TRUE_CONNECTOR_CLOUD_IP)==False:
        return handle_post(config.MLFLOW_EXPERIMENT,'Primera prueba',config.TRUE_CONNECTOR_CLOUD_IP)
    else:
        print('The experiment is already registered')