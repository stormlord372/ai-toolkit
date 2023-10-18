# Red Wine MLOps Lifecycle 

This is a example for building an Airflow DAG to automate the MLOps lifecycle for a red wine prediction project.

## Info


1. Inside the `DAG` directory, the script that will create the graph/dag in airflow is `RedWine_MLOps_lifecycle.py`:

    - You can customize the DAG parameters such as `description`, `schedule_interval`, `catchup`, and `start_date`.

2. This script will use the scripts located inside the following folders:

    - Inside the `Data` directory, there is the data reading script.

    - Inside the `Process` directory, there is the data processing script.

    - Inside the `Models` directory, there are the model training and evaluation scripts.

    - Inside the `Deployment` directory, there is the model selection script.

    - `IDS_templates`: (optional) Contains some auxiliary scripts for integration and communication of ai-toolkit with IDS. It offers a set of functions for reading data from IDS and logging the experiment in IDS.

    - `config.py`: Define the global and common configuration variables to be shared between the different scripts in this file.


## Integration with IDS

Make use of the templates provided in `IDS_templates/` folder for data reading and recording the experiment using IDS.

1. Fill in variables `TRUE_CONNECTOR_EDGE_IP` and `TRUE_CONNECTOR_CLOUD_IP` with the IPs where clarus_edge_deploy and true-connector-training projects have been deployed.
    ```python 
    # IDS TRUE CONNECTOR INFORMATION
    TRUE_CONNECTOR_EDGE_IP = "XXX.XX.XXX.XX"        
    TRUE_CONNECTOR_EDGE_PORT = "8889"
    TRUE_CONNECTOR_CLOUD_IP = "XXX.XX.XXX.XX"
    TRUE_CONNECTOR_CLOUD_PORT = "8084"
    ```
2. Import the `rest_ids_consumer_connector.py` template in the `read_data.py` and use it as follow:

    ```python
    from IDS_templates.rest_ids_consumer_connector import RestIDSConsumerConnector
    import config

    # Get dataset from IDS
    ids_consumer = rest_ids_consumer_connector.RestIDSConsumerConnector()
    data = ids_consumer.get_external_artifact_by_resource_title(
        config.MLFLOW_EXPERIMENT, 
        config.TRUE_CONNECTOR_EDGE_IP, 
        config.TRUE_CONNECTOR_EDGE_PORT, 
        config.TRUE_CONNECTOR_CLOUD_IP, 
        config.TRUE_CONNECTOR_CLOUD_PORT
    )

    # Read the file as usual, for example:
    df = pd.read_csv(data, delimiter=';', quotechar='"')
    ```
3. Update the dag script to add the new task to register experiment.

    3.1. Import the new task template. 
    ```python
    from Deployment.register_experiment import register_experiment
    ```

    3.2. Create the new task and add it to the workflow.
    ```python
    @task
    def register_experiment_task():
        print("Register experiment task:")
        return register_experiment()

    ...

    select_best_model_result = select_best_model_task()

    ...

    read_data_result >> processing_result >> [model_training_result] >> select_best_model_result >> register_experiment_result

    ```









