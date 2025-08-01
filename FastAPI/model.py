from pydantic import BaseModel

class EmployeData(BaseModel):
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

