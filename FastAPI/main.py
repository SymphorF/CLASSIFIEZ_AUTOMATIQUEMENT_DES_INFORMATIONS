
from fastapi import FastAPI, UploadFile, File
from FastAPI.model import EmployeData  
import joblib
import pandas as pd
import io

# 0. Création de l'application FastAPI
app = FastAPI(title="API prédiction employé")

# 1. Chargement du modèle
model = joblib.load("rfc_model.joblib")


# 2. Route pour prédire le statut d'un employé à partir des features individuelles
@app.post("/status_employe_individuel")
def predict(data: EmployeData):
    # Conversion des données reçues en DataFrame
    input_df = pd.DataFrame([data.dict()])
    
    # Prédiction avec le modèle
    pred = model.predict(input_df)[0]
    label = "A quitté" if pred == 1 else "Resté"

    return {
        "prediction": int(pred),
        "label": label
    }

# 3. Route pour prédire le statut d'employés à partir d'un fichier CSV
@app.post("/status_employes_via_csv")
async def status_employe(file: UploadFile = File(...)):
    # Vérification du type de fichier
    if not file.filename.endswith(".csv"):
        return {"error": "Le fichier doit être au format CSV."}

    try:
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))

        # Vérifier que toutes les colonnes attendues sont bien présentes
        required_columns = list(EmployeData.schema()["properties"].keys())
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            return {
                "error": "Certaines colonnes sont manquantes dans le fichier.",
                "colonnes_manquantes": missing_cols
            }

        # Prédictions
        preds = model.predict(df)
        df["prediction"] = preds
        df["prediction_label"] = df["prediction"].map({1: "A quitté", 0: "Resté"})

        # Réinitialiser l'index pour plus de clarté
        df = df.reset_index().rename(columns={"index": "ligne"})

        return df[["ligne", "prediction_label"]].to_dict(orient="records")

    except Exception as e:
        return {"error": f"Erreur pendant le traitement du fichier : {str(e)}"}