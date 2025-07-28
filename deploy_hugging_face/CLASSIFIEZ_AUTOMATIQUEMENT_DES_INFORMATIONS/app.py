import gradio as gr
import pandas as pd
import joblib

# Charger le modèle
model = joblib.load("rfc_model.joblib")

# Fonction de prédiction
def predict_from_csv(file):
    df = pd.read_csv(file.name)

    # Prédiction
    preds = model.predict(df)
    df["prediction"] = preds
    df["prediction_label"] = df["prediction"].map({1: "A quitté", 0: "Resté"})

    # Ajouter l'index comme colonne pour l'afficher (optionnel mais plus clair)
    df = df.reset_index()  # "index" devient une colonne
    df.rename(columns={"index": "ligne"}, inplace=True)

    return df[["ligne", "prediction_label"]]

# Définir un DataFrame vide avec colonnes "ligne" et "prediction_label"
empty_df = pd.DataFrame(columns=["ligne", "prediction_label"])

# Interface Gradio
interface = gr.Interface(
    fn=predict_from_csv,
    inputs=gr.File(label="Téléversez un fichier CSV"),
    outputs=gr.Dataframe(
        value=empty_df, 
        headers=["ligne", "prediction_label"],
        label="Résultats de la prédiction"
    ),
    title="Prédiction de départ d'employés",
    description="Téléversez un fichier CSV avec les bonnes colonnes pour prédire qui quitte l'entreprise."
)

if __name__ == "__main__":
    interface.launch()

