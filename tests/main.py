# FastAPI/main.py
'''
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Chargement du modèle
model = joblib.load("rfc_model.joblib")

# Classe d'entrée (doit refléter les variables utilisées à l'entraînement)
class InputData(BaseModel):
    heure_supp_par_taux_augmentation: float
    revenu_log: float
    heure_supp_niveau_hierarchique: float
    revenu_par_poste: float
    taux_augmentation: float
    experience_stagnee: int
    ratio_distance_experience: float
    effort_vs_gain: float
    ecart_revenu_moyen_poste: float
    satisfaction_moyenne: float
    ratio_experience_age: float
    annee_experience_totale: float
    heure_supplementaires_Oui: int
    score_engagement: float
    anciennete_cat_encoded: int
    ratio_satisfaction_travail_eval: float
    formations_par_anciennete: float
    satisfaction_employee_nature_travail: float
    nombre_participation_pee: float
    age: int
    annees_dans_l_entreprise: int
    distance_domicile_travail: float
    annees_dans_le_poste_actuel: int
    frequence_deplacement_encoded: int
    revenu_bas: int
    ecart_age_experience: float
    nombre_experiences_precedentes: int
    augmentation_salaire_precedent_pct: float
    delta_note_evaluation: float
    heure_supp_anciennete_poste: float
    satisfaction_employee_equilibre_pro_perso: float
    nb_formations_suivies: int

@app.post("/predict")
def predict(data: InputData):
    # Conversion en array dans l'ordre exact des champs
    X = np.array([[
        data.heure_supp_par_taux_augmentation,
        data.revenu_log,
        data.heure_supp_niveau_hierarchique,
        data.revenu_par_poste,
        data.taux_augmentation,
        data.experience_stagnee,
        data.ratio_distance_experience,
        data.effort_vs_gain,
        data.ecart_revenu_moyen_poste,
        data.satisfaction_moyenne,
        data.ratio_experience_age,
        data.annee_experience_totale,
        data.heure_supplementaires_Oui,
        data.score_engagement,
        data.anciennete_cat_encoded,
        data.ratio_satisfaction_travail_eval,
        data.formations_par_anciennete,
        data.satisfaction_employee_nature_travail,
        data.nombre_participation_pee,
        data.age,
        data.annees_dans_l_entreprise,
        data.distance_domicile_travail,
        data.annees_dans_le_poste_actuel,
        data.frequence_deplacement_encoded,
        data.revenu_bas,
        data.ecart_age_experience,
        data.nombre_experiences_precedentes,
        data.augmentation_salaire_precedent_pct,
        data.delta_note_evaluation,
        data.heure_supp_anciennete_poste,
        data.satisfaction_employee_equilibre_pro_perso,
        data.nb_formations_suivies
    ]])

    prediction = model.predict(X)[0]
    proba = model.predict_proba(X)[0].tolist()

    return {
        "prediction": int(prediction),
        "probabilités": proba
    }
'''

# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Chargement du modèle
model = joblib.load("rfc_model.joblib")

# Définition du schéma des données d’entrée
class InputData(BaseModel):
    heure_supp_par_taux_augmentation: float
    revenu_log: float
    heure_supp_niveau_hierarchique: float
    revenu_par_poste: float
    taux_augmentation: float
    experience_stagnee: int
    ratio_distance_experience: float
    effort_vs_gain: float
    ecart_revenu_moyen_poste: float
    satisfaction_moyenne: float
    ratio_experience_age: float
    annee_experience_totale: float
    heure_supplementaires_Oui: int
    score_engagement: float
    anciennete_cat_encoded: int
    ratio_satisfaction_travail_eval: float
    formations_par_anciennete: float
    satisfaction_employee_nature_travail: float
    nombre_participation_pee: float
    age: int
    annees_dans_l_entreprise: int
    distance_domicile_travail: float
    annees_dans_le_poste_actuel: int
    frequence_deplacement_encoded: int
    revenu_bas: int
    ecart_age_experience: float
    nombre_experiences_precedentes: int
    augmentation_salaire_precedent_pct: float
    delta_note_evaluation: float
    heure_supp_anciennete_poste: float
    satisfaction_employee_equilibre_pro_perso: float
    nb_formations_suivies: int

@app.post("/predict")
def predict(data: InputData):
    X = np.array([[getattr(data, field) for field in data.__fields__]])
    prediction = model.predict(X)[0]
    return {"prediction": int(prediction)}


