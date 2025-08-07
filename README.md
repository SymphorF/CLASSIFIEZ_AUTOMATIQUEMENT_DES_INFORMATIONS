# Projet : Classifiez automatiquement des informations

Utilisez des modèles de classification pour prédire les démissions des employés de l'ESN TechNova Partners.

*Ce projet utilise Python avec Poetry pour la gestion d'environnement virtuel, et JupyterLab pour l'exploration des données.*

# Structure du projet

``` 
Projet /
├── .github/workflows                          # Workflow déploiement sur github
│   └── python-ci-cd.yml                       # Fichier de déploiement pour le workflow CI/CD
├── Docs/                                      # Les documents annexes (présentation, rapports…)
│   ├── Scheam_BDD.pdf                         # Schéma de base de données
│   ├── Scheam_BDD.png                         # Schéma de base de données
│   └── Fonkou_Symphor_présentation.pptx       # Présentation PowerPoint du projet
├── FastAPI/                                   # Dossier FastAPI
│   ├── __pycache__                            # Dossier pycache stockage des données compilées
│   ├── __init__.py                            # Fichier init pour définir le package FastAPI
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
│   ├── .gitattributes                         # Fichier de configuration git
│   ├── README.md                              # README de hugging face
│   ├── app.py                                 # Fichier app pour simulation hugging face
│   ├── data_TEST.csv                          # Données de test pour hugging face et FastAPI
│   ├── logreg_model.joblib                    # Modèle de regression logistique en joblib
│   ├── rfc_model.joblib                       # Modèle random forest classifier en joblib
│   └── requirements.txt                       # Fichier requis pour deploiement hugging face
├── tests/                                     # Fichiers de tests unitaires et fonctionnels
│   ├── __pycache__                            # Dossiers pycache stockage des tests compilés
│   ├── test_sample.py                         # Fichier de test (échantillon)
│   ├── test_chargement.py                     # Fichier de test de chargement des données
│   ├── test_model.py                          # Fichier de test de modélisation
│   ├── test_preprocessing.py                  # Fichier de test de nettoyage
│   └── test_fonctionnel_predict_endpoint.py   # Test fonctionnel (affichage des prédictions selon données d'entrée)
├── rfc_model.joblib                           # Modèle rfc joblib pour déploiment cd du test fonctionnel
├── poetry.lock                                # Fichier des dépendances (poetry)
├── pyproject.toml                             # Verrouillage des versions
├── Requirements.txt                           # Ensemble des outils nécessaires pour ce projet
└── README.md                                  # README global du projet (Explications du projet)

``` 

🚀 **Présentation du projet**
Ce projet vise à prédire des tendances ou des indicateurs RH à partir de jeux de données combinés (SIRH, sondage, évaluation). À l’aide de modèles comme Logistic Regression ou Random Forest, nous fournissons des prédictions accessibles via une API FastAPI et déployées aussi via Hugging Face Spaces.

⚙️ **Instructions d’installation**

1. Cloner le dépôt :

bash

git clone https://github.com/SymphorF/CLASSIFIEZ_AUTOMATIQUEMENT_DES_INFORMATIONS.git

cd CLASSIFIEZ_AUTOMATIQUEMENT_DES_INFORMATIONS


2. Créer un environnement virtuel :

bash

python -m venv venv

source venv\Scripts\activate 


3. Installer les dépendances :

bash

pip install -r deploy_hugging_face/requirements.txt
installez poetry :

bash

poetry install



🧪 **Lancer les tests**

bash

pytest --cov=FastAPI tests/


▶️ **Utilisation locale (FastAPI)**

1. Démarrer le serveur FastAPI :

bash

cd FastAPI

uvicorn main:app --reload

ou 

fastapi dev main.py


2. Accéder à la documentation interactive :

Swagger : http://127.0.0.1:8000/docs

Redoc : http://127.0.0.1:8000/redoc



🌐 **Déploiement**

🔁 **GitHub Actions CI/CD**

Un fichier .github/workflows/python-ci-cd.yml gère les workflows CI/CD :

* Exécution des tests à chaque push
* Vérification du code Python (lint, pytest)

🤗 **Hugging Face**
1. Copier le contenu du dossier deploy_hugging_face/ vers un repo Hugging Face Space.

2. Utiliser app.py comme fichier principal.

3. Les modèles .joblib doivent être présents dans le repo.

4. Hugging Face utilise requirements.txt pour les dépendances.


🔒 **Bonnes pratiques de sécurité**

✅ **Variables secrètes**

* Ne jamais stocker de mot de passe, clé API ou URL de base de données en clair dans le code.
* Utiliser un fichier .env pour les secrets 

env

DATABASE_URL=postgresql://user:pwd@localhost/db
SECRET_KEY=your-secret-key


📚 **Auteurs et crédits**
Fonkou Symphor

Ce projet a été réalisé dans le cadre d’un exercice de modélisation et de déploiement d’un système prédictif RH.