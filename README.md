# Projet : Classifiez automatiquement des informations

Utilisez des modèles de classification pour prédire les démissions des employés de l'ESN TechNova Partners.

*Ce projet utilise Python avec Poetry pour la gestion d'environnement virtuel, et JupyterLab pour l'exploration des données.*

# Structure du projet

``` 
Projet /
├── Data/                                   # Les jeux de données (csv)
│   ├── extrait_sondage.csv                 # Données brutes
│   ├── extrait_sirh.csv                    # Données brutes
│   ├── extrait_eval.csv                    # Données brutes
│   ├── data.csv                            # Données brutes regroupées
│   ├── data_encoded.csv                    # Données nettoyés (sans la cible)
│   └── data_cible_encoded.csv              # Données nettoyés (cible uniquement)
├── Notebooks/                              # Les notebooks Jupyter
│   ├── Fonkou_Symphor_1_notebook.ipynb     # Première partie Notebooks
│   └── Fonkou_Symphor_2_notebook.ipynb     # Deuxième partie Notebooks
├── Docs/                                   # Les documents annexes (présentation, rapports…)
│   └── Fonkou_Symphor_présentation.pptx    # Présentation PowerPoint du projet
├── pyproject.toml                          # Fichier des dépendances (poetry)
├── poetry.lock                             # Verrouillage des versions
└── README.md                               # Explications du projet

``` 