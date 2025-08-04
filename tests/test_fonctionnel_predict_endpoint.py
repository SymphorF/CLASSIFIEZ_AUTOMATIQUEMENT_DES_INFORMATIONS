from fastapi.testclient import TestClient
from FastAPI.main import app

client = TestClient(app)

def test_predict_endpo():
    payload = {
       "heure_supp_par_taux_augmentation": 3.50, 
        "revenu_log": 10500.00,
        "heure_supp_niveau_hierarchique": 0.55,
        "revenu_par_poste": 2950.00,
        "taux_augmentation": 0.0055,
        "experience_stagnee": 1, 
        "ratio_distance_experience":0.285,
        "effort_vs_gain": 0.056,
        "ecart_revenu_moyen_poste": -155.25,
        "satisfaction_moyenne": 2.5,
        "ratio_experience_age":0.025,
        "annee_experience_totale": 7.0,
        "heure_supplementaires_Oui": 1,
        "score_engagement": 0.75,
        "anciennete_cat_encoded": 4,
        "ratio_satisfaction_travail_eval": 0.85,
        "formations_par_anciennete":2.0,
        "satisfaction_employee_nature_travail":2.0,
        "nombre_participation_pee":1,
        "age": 30,
        "annees_dans_l_entreprise": 4,
        "distance_domicile_travail": 7.5,
        "annees_dans_le_poste_actuel": 4, 
        "frequence_deplacement_encoded":1, 
        "revenu_bas": 1, 
        "ecart_age_experience":23.0,
        "nombre_experiences_precedentes":1,
        "augmentation_salaire_precedent_pct":15.0,
        "delta_note_evaluation":1.0,
        "heure_supp_anciennete_poste":0.0,
        "satisfaction_employee_equilibre_pro_perso":3,
        "nb_formations_suivies": 2
    }

    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    assert "prediction" in response.json()

    