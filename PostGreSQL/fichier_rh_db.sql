-- 1. Création d'une clé id de la table eval, 
/*
on change la clé eval_number du type E_1, E_2... à 1, 2... 
pour la cohérence avec les autres clés
*/

ALTER TABLE eval ADD COLUMN id INT;

UPDATE eval
SET id = CAST(SUBSTRING(eval_number FROM 'E_(\d+)') AS INT);

-- 2. Création d'une clé id de la table sirh 
/*
On créé la clé id à partir de la clé d'origine 
qui est id_employee
*/

ALTER TABLE sirh ADD COLUMN id INTEGER;
UPDATE sirh SET id = id_employee;

SELECT * FROM sirh

-- 3. Création d'une clé id de la table sondage 
/*
On créé la clé id à partir de la clé d'origine 
qui est code_sondage
*/

ALTER TABLE sondage ADD COLUMN id INTEGER;
UPDATE sondage SET id = code_sondage;

-- 4. Jointure des tables sur la clé commune id

CREATE TABLE data_all AS
SELECT 
    s.id_employee
    s.age,
    s.genre,
    s.revenu_mensuel,
    s.statut_marital,
    s.departement,
    s.poste,
    s.nombre_experiences_precedentes,
    s.nombre_heures_travailless,
    s.annee_experience_totale,
    s.annees_dans_l_entreprise,
    s.annees_dans_le_poste_actuel,
    e.satisfaction_employee_environnement,
    e.note_evaluation_precedente,
    e.niveau_hierarchique_poste,
    e.satisfaction_employee_nature_travail,
    e.satisfaction_employee_equipe,
    e.satisfaction_employee_equilibre_pro_perso,
    e.note_evaluation_actuelle,
    e.heure_supplementaires,
    e.augementation_salaire_precedente,
	e.id,
	so.a_quitte_l_entreprise,
    so.nombre_participation_pee,
    so.nb_formations_suivies,
    so.nombre_employee_sous_responsabilite,
	so.code_sondage,
    so.distance_domicile_travail,
    so.niveau_education,
	so.domaine_etude,
	so.ayant_enfants,
	so.frequence_deplacement,
    so.annees_depuis_la_derniere_promotion,
    so.annes_sous_responsable_actuel
	
FROM sirh s
JOIN eval e ON s.id_employee = e.eval.number
JOIN sondage so ON s.id_employee = so.code_sondage;

-- 5. Vérification de l'encodage

SHOW client_encoding;

-- 6. Statistiques descriptives

CREATE TABLE stat_table AS
SELECT 
    a_quitte_l_entreprise,
    COUNT(*) AS nb_employes,
    AVG(age) AS age_moyen,
    STDDEV(age) AS age_ecart_type,
    MIN(age) AS age_min,
    MAX(age) AS age_max,    
    AVG(revenu_mensuel) AS revenu_moyen,
    STDDEV(revenu_mensuel) AS revenu_ecart_type,
    MIN(revenu_mensuel) AS revenu_min,
    MAX(revenu_mensuel) AS revenu_max,    
    AVG(nombre_heures_travailless) AS heures_travail_moyennes,
    STDDEV(nombre_heures_travailless) AS heures_travail_ecart_type,
    MIN(nombre_heures_travailless) AS heures_travail_min,
    MAX(nombre_heures_travailless) AS heures_travail_max,    
    AVG(note_evaluation_actuelle) AS note_evaluation_moyenne,
    STDDEV(note_evaluation_actuelle) AS note_evaluation_ecart_type,
    MIN(note_evaluation_actuelle) AS note_evaluation_min,
    MAX(note_evaluation_actuelle) AS note_evaluation_max,   
    AVG(distance_domicile_travail) AS distance_moyenne,
    STDDEV(distance_domicile_travail) AS distance_ecart_type,
    MIN(distance_domicile_travail) AS distance_min,
    MAX(distance_domicile_travail) AS distance_max
FROM data_all
GROUP BY a_quitte_l_entreprise;

-- 7... Travail sur notebook python (voir notebook connexion_db_postgresql.ipynb)

/* 
 Nettoyage, encodage, modélisation...
*/

-- 8. Vérification des resultats de sortie 

SELECT * FROM model_outputs_logreg
