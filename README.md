# Projet : Classifiez automatiquement des informations

Utilisez des modèles de classification pour prédire les démissions des employés de l'ESN TechNova Partners.

*Ce projet utilise Python avec Poetry pour la gestion d'environnement virtuel, et JupyterLab pour l'exploration des données.*

# Structure du projet

``` 
Projet /
├── .github/workflows                          # Le workflow
│   └── python-ci-cd.yml                       # fichier de déploiement pour le workflow
├── Docs/                                      # Les documents annexes (présentation, rapports…)
│   ├── Scheam_BDD.pdf                         # Schéma de base de données
│   ├── Scheam_BDD.png                         # Schéma de base de données
│   └── Fonkou_Symphor_présentation.pptx       # Présentation PowerPoint du projet
├── FastAPI/                                   # Dossier FastAPI
│   ├── __pycache__                            # Dossier pycache
│   ├── __init__.py                            # Fichier init
│   ├── main.py                                # Fichier main
│   ├── model.py                               # Fichier des classes des données
│   └── predict.py                             # Fonction de prédiction
├── Notebooks/                                 # Les notebooks Jupyter
│   ├── Fonkou_Symphor_1_notebook.ipynb        # Première partie Notebooks
│   └── Fonkou_Symphor_2_notebook.ipynb        # Deuxième partie Notebooks
├── PostGreSQL/                                # Fichier PostGreSQL
│   ├── Docs                                   # Documents PostGreSQL
│   ├── connexion_db_postgresql.ipynb          # Fichier de connexion postgresql à python
│   └── fichier_rh_db.sql                      # Fichier script SQL 
├── Data/                                      # Les jeux de données (csv)
│   ├── extrait_sondage.csv                    # Données brutes
│   ├── extrait_sirh.csv                       # Données brutes
│   ├── extrait_eval.csv                       # Données brutes
│   ├── data.csv                               # Données brutes regroupées
│   ├── data_encoded.csv                       # Données nettoyés (sans la cible)
│   └── data_cible_encoded.csv                 # Données nettoyés (cible uniquement)
├── deploy_hugging_face/                       # Deploiement hugging face
│   ├── .gitattributes                         # Données brutes
│   ├── README.md                              # README de hugging face
│   ├── app.py                                 # Fichier app pour simulation hugging face
│   ├── data_TEST.csv                          # Données de test pour hugging face et FastAPI
│   ├── logreg_model.joblib                    # Modèle de regression logistique en joblib
│   ├── rfc_model.joblib                       # Modèle random forest classifier en joblib
│   └── requirements.txt                       # Fichier requis pour deploiement hugging face
├── tests/                                     # Fichiers de tests unitaires et fonctionnels
│   ├── __pycache__                            # Dossiers pycache
│   ├── test_sample.py                         # Fichier de test (échantillon)
│   ├── test_chargement.py                     # Fichier de test de chargement des données
│   ├── test_model.py                          # Fichier de test de modélisation
│   ├── test_preprocessing.py                  # Fichier de test de nettoyage
│   └── test_fonctionnel_predict_endpoint.py   # Test fonctionnel (affIchage des prédiction selon données d'entrée)
├── rfc_model.joblib                           # Modèle rfc joblib pour déploiment cd du test fonctionnel
├── poetry.lock                                # Fichier des dépendances (poetry)
├── pyproject.toml                             # Verrouillage des versions
└── README.md                                  # README global du projet (Explications du projet)

``` 