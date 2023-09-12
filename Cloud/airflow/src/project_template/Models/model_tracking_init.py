import warnings
import mlflow
from mlflow.tracking.client import MlflowClient

import config

def model_tracking_init():
    ''' Auxiliar function to create expemient before parallel run tracking '''
    client = MlflowClient(config.MLFLOW_ENDPOINT)
    mlflow.set_tracking_uri(config.MLFLOW_ENDPOINT)
    mlflow.set_experiment(config.MLFLOW_EXPERIMENT)
    warnings.filterwarnings('ignore')
