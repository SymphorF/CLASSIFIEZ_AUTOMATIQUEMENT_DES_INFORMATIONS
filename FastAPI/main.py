# Partie FastAPI pour création de l'API de prédiction
from fastapi import FastAPI
from model import EmployeData  
import joblib
import pandas as pd

app = FastAPI(title="API prédiction employé")

# Charger le modèle
model = joblib.load("rfc_model.joblib")

@app.post("/predict")
def predict(data: EmployeData):
    # Convertir les données Pydantic en DataFrame
    input_df = pd.DataFrame([data.dict()])
    
    # Faire une prédiction
    pred = model.predict(input_df)[0]
    label = "A quitté" if pred == 1 else "Resté"

    return {
        "prediction": int(pred),
        "label": label
    }
