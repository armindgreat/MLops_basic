import joblib  # type: ignore
import numpy as np # type: ignore
import pandas as pd # type: ignore
from pathlib import Path



class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    
    def predict(self, data):
        prediction = self.model.predict(data)
        return prediction