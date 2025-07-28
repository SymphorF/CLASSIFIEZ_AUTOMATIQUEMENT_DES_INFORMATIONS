import joblib
import pandas as pd

# Charger le modèle
model = joblib.load("rfc_model.joblib")

def make_prediction(data: dict) -> dict:
    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)[0]
    label = "A quitté" if prediction == 1 else "Resté"
    return {
        "prediction": int(prediction),
        "label": label
    }
