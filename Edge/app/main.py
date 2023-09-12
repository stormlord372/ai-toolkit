import time
import mlflow
from mlflow.tracking.client import MlflowClient
from fastapi import FastAPI
from mlflow.pyfunc import load_model

import os
import zipfile
import io
import sklearn
import shutil
import numpy as np

MLFLOW_PATH=os.environ["MLFLOW_PATH"]
MLFLOW_EXPERIMENT=os.environ["MLFLOW_EXPERIMENT"]
AWS_ACCESS_KEY_ID=os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY=os.environ["AWS_SECRET_ACCESS_KEY"]
MLFLOW_S3_ENDPOINT_URL=os.environ["MLFLOW_S3_ENDPOINT_URL"] 

# # Create the POST endpoint with path '/predict'
app = FastAPI()
@app.get("/predict")
def deploy_model_predict(datos,model):

    """
    The function implements the logic to do the inference.
    """

    # ADD YOUR CODE HERE
    


