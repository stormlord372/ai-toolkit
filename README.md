# AI TOOLKIT

The AI TOOLKIT is designed to effectively manage the entire life cycle of the models. To achieve this, we have implemented a set of Dockerized services that cater to various needs. The overall infrastructure is divided into two distinct docker-compose projects, ensuring easier maintenance and independent implementations:

* **Cloud:** This docker-compose project provides a set of AI toolkits for the automatization of the set of tasks for model training. It houses a range of essential services like Jupiter notebooks, MLflow, Airflow, and more. These services enable seamless collaboration and efficient handling of machine learning operations.
* **Edge:** This Docker Compose project offers a comprehensive suite of AI toolkits designed for ML model inference at the edge, all accessible through a web API.

Both projects are thoroughly documented, offering clear installation and usage instructions, which can be found in the accompanying `README.md` files available in their respective folders.

## Installation Steps:

1. Clone the source code from the GitHub repository. You can achieve this by running the following command:

```
git clone <repository_url>
```

2. Build and start the docker compose of the **Cloud** project following the instrucctions given in the [README.md](Cloud/README.md) of `Cloud` directory.

3. Build and start the docker compose of the **Edge** project following the instrucctions given in the [README.md](Edge/README.md) of `Edge` directory.