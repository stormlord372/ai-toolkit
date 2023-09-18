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

3. Start Airflow and run the DAG.

4. Access the Airflow web interface to monitor the execution of the DAG and view task logs.








