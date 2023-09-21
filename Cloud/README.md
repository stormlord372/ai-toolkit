# MLOPS CLOUD ARCHITECTURE

This document provides a comprehensive guide on setting up the MLOps cloud architecture for automatic model training and utilization. It covers the steps required to deploy the architecture and offers detailed instructions on how to leverage its functionalities effectively.

The architecture has been dockerized to improve management and deployment efficiency. It employs a Docker Compose setup, enabling a seamless integration of various components necessary for the MLOPS project. This approach simplifies the management of services and provides a unified environment for deploying services, ensuring a smooth workflow throughout the project lifecycle.

## ARCHITECTURE DESCRIPTION

The Docker Compose setup consists of a collection of services that work together to support various components of a machine learning project and workflow management. Below is the folder structure tree that includes additional details about each service:

```
├── Cloud
│   ├── airflow
│   │   ├── dags/
│   │   ├── logs/
│   │   ├── plugins/   
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   └── src/
│   ├── jupyter
│   │   ├── notebooks/
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   ├── minio
│   │   ├── Dockerfile
│   ├── mlflow
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   └── postgres
│       └── init.sh
├── docker-compose.yml
├── .env
├── README.md
```

### Docker Compose Setup

The Docker Compose setup is configured in the `docker-compose.yml` file. It defines the services and their dependencies, enabling you to run multiple services with a single command. The `.env` file contains configuration parameters and passwords for the services.

### Services

1. **Airflow:** An open-source platform to programmatically author, schedule, and monitor workflows. The DAGs (Directed Acyclic Graphs) for different tasks related to data processing, model training, and deployment are stored in the `airflow/dags` directory.

2. **Jupyter:** Jupyter Notebooks for interactive data exploration and analysis are stored in the `jupyter/notebooks` directory. Jupyter's Dockerfile and dependencies are located in the `jupyter` folder.

3. **MLflow:** An open-source platform for managing the end-to-end machine learning lifecycle. It tracks experiments, stores model artifacts, and provides a user interface for monitoring and managing models. MLflow's Dockerfile and dependencies are located in the `mlflow` folder.

4. **PostgreSQL:** A relational database used for storing MLflow data and other application data. Multiple databases are configured for different services. The initialization script is stored in the `postgres` folder.

5. **MinIO:** An object storage server compatible with Amazon S3. It is used to store MLflow artifacts and data. The Dockerfile is inside the `minio` folder

### Additional Details
1. The `Dockerfile` in the directory of each service is likely a global Dockerfile that configures the base environment for all services.
2. The `requirements.txt` files in each service folder contain the necessary Python packages and dependencies required for the corresponding service.


## INSTALLATION AND CONFIGURATION GUIDE

Before starting the installation, make sure you have Docker and Docker Compose installed on your machine, following these instructions: https://docs.docker.com/compose/install/linux/ 

1. Move to AI_TOOLKIT

```
cd AI_TOOLKIT
```

2. Update the `.env` file with your desired configuration parameters. 
<!-- Replace the placeholders (xxx) with your actual values for passwords and other parameters. -->

3. Build the Docker containers and start the services:

```
docker-compose build
docker-compose up -d
```

4. Wait for the services to start up. You can check the logs for each service to ensure everything is running correctly:

```
docker-compose logs -f <service_name>
```

5. Once all services are up and running, you can access the following:

    * Airflow UI: `http://<Server_IP_or_localhost>:8080`
    * Jupyter Notebooks: `http://<Server_IP_or_localhost>:1998`
    * MLflow UI: `http://<Server_IP_or_localhost>:5000`
    * MINIO UI: `http://<Server_IP_or_localhost>:9002`
    * PostgreSQL: Port 5432

## USAGE GUIDE

### Jupyter Notebooks
1. Access Jupyter Notebooks at `http://<Server_IP_or_localhost>:1998` in your browser.
2. Use the notebooks in the notebooks directory for data exploration, analysis, and experimentation.

### Airflow
1. Access the Airflow UI at `http://<Server_IP_or_localhost>:8080` in your browser.
2. You'll need to create and enable DAGs to schedule tasks. DAGs are Python scripts located in the `airflow/dags` directory. Refer to the Airflow documentation README.md inside airflow folder.

### MLflow
1. MLflow UI can be accessed at `http://<Server_IP_or_localhost>:5000`.
2. Use MLflow to track and manage experiments, store model artifacts, and monitor models' performance. Refer to the MLflow documentation for more details on using MLflow.

### MinIO
1. The Minio UI is available at `http://<Server_IP_or_localhost>:9002` in your browser.

### PostgreSQL
1. PostgreSQL a backend services that is utilized by the above services. They are accessible within the Docker network using their respective `hostname`, `database name` and `port` that are defined in the `.env` file.
2. The initialization configuration is available in the `postgres` directory.
