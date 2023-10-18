# MLOps Lifecycle Template

This is a template for building an Airflow DAG to automate the MLOps lifecycle. It provides a starting point for users to create their own MLOps pipeline.

## Key concepts

In order to use this template it is necessary to know some basic concepts. Specifically these concepts related to Airflow tool used to define the workflow and Mlflow to track the training of the models.

- **Airflow**: The Airflow Platform is a tool for describing, executing, and monitoring workflows.

    Use airflow to author workflows as directed acyclic graphs (DAGs) of tasks. The airflow scheduler executes your tasks on an array of workers while following the specified dependencies. Rich command line utilities make performing complex surgeries on DAGs a snap. The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed.

    When workflows are defined as code, they become more maintainable, versionable, testable, and collaborative.

    * **DAG** – or a Directed Acyclic Graph – is a collection of all the tasks you want to run, organized in a way that reflects their relationships and dependencies. DAGs are defined in standard Python files that are placed in Airflow’s DAG_FOLDER. Airflow will execute the code in each file to dynamically build the DAG objects. You can have as many DAGs as you want, each describing an arbitrary number of tasks. In general, each one should correspond to a single logical workflow. In summary, **a dag can be defined as a description of the order in which work should take place**.
    * **Operator**: In summary, a operator is as **a class that acts as a template for carrying out some work**.
    * **Tasks**. Once an operator is instantiated, it is referred to as a “task”. The instantiation defines specific values when calling the abstract operator, and the parameterized task becomes a node in a DAG. In summary, a task is **a parameterized instance of an operator**.
    * **Task Instance**. A task instance represents a specific run of a task and is characterized as the combination of a dag, a task, and a point in time. In summary, a task instance is **a task that 1) has been assigned to a DAG and 2) has a state associated with a specific run of the DAG**.

    By combining DAGs and Operators to create TaskInstances, you can build complex workflows.

- **MLflow**:
    MLflow is organized into four components: Tracking, Projects, Models, and Model Registry. You can use each of these components on their own—for example, maybe you want to export models in MLflow’s model format without using Tracking or Projects—but they are also designed to work well together.

    MLflow’s core philosophy is to put as few constraints as possible on your workflow: it is designed to work with any machine learning library, determine most things about your code by convention, and require minimal changes to integrate into an existing codebase. At the same time, MLflow aims to take any codebase written in its format and make it reproducible and reusable by multiple data scientists. On this page, we describe a typical ML workflow and where MLflow fits in.

    * **MLflow Tracking** is an API and UI for logging parameters, code versions, metrics, and artifacts when running your machine learning code and for later visualizing the results. You can use MLflow Tracking in any environment (for example, a standalone script or a notebook) to log results to local files or to a server, then compare multiple runs. Teams can also use it to compare results from different users.

    * **MLflow Projects** are a standard format for packaging reusable data science code. Each project is simply a directory with code or a Git repository, and uses a descriptor file or simply convention to specify its dependencies and how to run the code. For example, projects can contain a conda.yaml file for specifying a Python Conda environment. When you use the MLflow Tracking API in a Project, MLflow automatically remembers the project version (for example, Git commit) and any parameters. You can easily run existing MLflow Projects from GitHub or your own Git repository, and chain them into multi-step workflows.

    * **MLflow Models** offer a convention for packaging machine learning models in multiple flavors, and a variety of tools to help you deploy them. Each Model is saved as a directory containing arbitrary files and a descriptor file that lists several “flavors” the model can be used in. For example, a TensorFlow model can be loaded as a TensorFlow DAG, or as a Python function to apply to input data. MLflow provides tools to deploy many common model types to diverse platforms: for example, any model supporting the “Python function” flavor can be deployed to a Docker-based REST server, to cloud platforms such as Azure ML and AWS SageMaker, and as a user-defined function in Apache Spark for batch and streaming inference. If you output MLflow Models using the Tracking API, MLflow also automatically remembers which Project and run they came from.

    * **MLflow Registry** offers a centralized model store, set of APIs, and UI, to collaboratively manage the full lifecycle of an MLflow Model. It provides model lineage (which MLflow experiment and run produced the model), model versioning, stage transitions (for example from staging to production or archiving), and annotations.



## Getting Started

1. Create a new folder with your project name or copy the template folder and change its name. The structure should be the following.

    - `Data`: Place your data-related Python scripts in this directory. These scripts should handle tasks such as reading data from different sources.

    - `Process`: Put your data processing scripts in this directory. These scripts should define the logic for data preprocessing, feature engineering, or any other data transformations required for your project.

    - `Models`: Store your machine learning model-related scripts in this directory. These scripts should handle tasks such as model training, evaluation, and tracking.

    - `Deployment`: Include your deployment-related scripts in this directory. These scripts should handle tasks such as selecting the best model, deploying the model to a production environment, or monitoring the deployed model.

    - `IDS_templates`: (optional) Contains some auxiliary scripts for integration and communication of ai-toolkit with IDS. It offers a set of functions for reading data from IDS and logging the experiment in IDS.

    - `config.py`: Define the global and common configuration variables to be shared between the different scripts in this file.

2. Place your Python scripts in the corresponding directories:

    - Inside the `Data` directory, add your data reading and preprocessing scripts.

    - Inside the `Process` directory, add your data processing scripts.

    - Inside the `Models` directory, add your machine learning model training and evaluation scripts.

    - Inside the `Deployment` directory, add your model selection and deployment scripts.

3. Navigate to the `DAG` directory and create a new DAG file using the `dag_template.py`:

    - Update the import statements to include your own Python scripts located in the corresponding directories (`Data`, `Process`, `Models`, and `Deployment`). Replace the existing import statements with the appropriate ones for your project.

    - Customize the DAG parameters such as `description`, `schedule_interval`, `catchup`, and `start_date` according to your requirements.

    - Define and remove as many task as needed

    - Instantiate each task and define their dependencies

    - Define the order of the pipeline. 

5. Start Airflow and run the DAG:

5. Access the Airflow web interface to monitor the execution of the DAG and view task logs.

6. Customize the tasks and their logic in the Python scripts to suit your specific project requirements.

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









