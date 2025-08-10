from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import joblib
import pandas as pd
from datetime import datetime
import json

# =============================
# 0. Création de l'application
# =============================
app = FastAPI(title="API prédiction employé")

# =============================
# 1. Connexion à PostgreSQL
# =============================
DATABASE_URL = "postgresql://postgres:1992@localhost:5432/projet_rh"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# =============================
# 2. Modèles SQLAlchemy
# =============================
class InputEmploye(Base):
    __tablename__ = "inputs_employes"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class OutputEmploye(Base):
    __tablename__ = "outputs_employes"
    id = Column(Integer, primary_key=True, index=True)
    prediction = Column(Integer, nullable=False)
    label = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

# Création des tables
Base.metadata.create_all(bind=engine)

# =============================
# 3. Modèle Pydantic
# =============================
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

# =============================
# 4. Chargement du modèle ML
# =============================
model = joblib.load("rfc_model.joblib")

# =============================
# 5. Route de prédiction individuelle
# =============================
@app.post("/status_employe_individuel")
def predict(data: EmployeData):
    session = SessionLocal()

    try:
        # 1️⃣ Enregistrement de l'input
        input_record = InputEmploye(data=data.dict())
        session.add(input_record)
        session.commit()

        # 2️⃣ Conversion en DataFrame pour la prédiction
        input_df = pd.DataFrame([data.dict()])
        pred = model.predict(input_df)[0]
        label = "A quitté" if pred == 1 else "Resté"

        # 3️⃣ Enregistrement de l'output
        output_record = OutputEmploye(prediction=int(pred), label=label)
        session.add(output_record)
        session.commit()

        return {
            "prediction": int(pred),
            "label": label
        }

    except Exception as e:
        session.rollback()
        return {"error": str(e)}

    finally:
        session.close()


# 5. Route pour prédire le statut d'employés à partir d'un fichier CSV
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


'''

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import joblib
import pandas as pd
from datetime import datetime

# =============================
# 0. Création de l'application
# =============================
app = FastAPI(title="API prédiction employé")

# =============================
# 1. Connexion à PostgreSQL
# =============================
DATABASE_URL = "postgresql://username:password@localhost:5432/nom_de_ta_base"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# =============================
# 2. Modèles SQLAlchemy
# =============================
class InputEmploye(Base):
    __tablename__ = "inputs_employes"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relation vers l'output
    output = relationship("OutputEmploye", back_populates="input_data", uselist=False)


class OutputEmploye(Base):
    __tablename__ = "outputs_employes"
    id = Column(Integer, primary_key=True, index=True)
    input_id = Column(Integer, ForeignKey("inputs_employes.id"), nullable=False)
    prediction = Column(Integer, nullable=False)
    label = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relation vers l'input
    input_data = relationship("InputEmploye", back_populates="output")


# Création des tables si elles n'existent pas
Base.metadata.create_all(bind=engine)

# =============================
# 3. Modèle Pydantic
# =============================
class EmployeData(BaseModel):
    # Remplacer par les features réelles de ton modèle
    age: int
    salaire: float
    anciennete: int
    satisfaction: float

# =============================
# 4. Chargement du modèle ML
# =============================
model = joblib.load("rfc_model.joblib")

# =============================
# 5. Route de prédiction
# =============================
@app.post("/status_employe_individuel")
def predict(data: EmployeData):
    session = SessionLocal()

    try:
        # 1️⃣ Enregistrement de l'input
        input_record = InputEmploye(data=data.dict())
        session.add(input_record)
        session.commit()  # on commit pour avoir l'ID

        # 2️⃣ Prédiction
        input_df = pd.DataFrame([data.dict()])
        pred = model.predict(input_df)[0]
        label = "A quitté" if pred == 1 else "Resté"

        # 3️⃣ Enregistrement de l'output lié à l'input
        output_record = OutputEmploye(
            input_id=input_record.id,
            prediction=int(pred),
            label=label
        )
        session.add(output_record)
        session.commit()

        return {
            "input_id": input_record.id,
            "prediction": int(pred),
            "label": label
        }

    except Exception as e:
        session.rollback()
        return {"error": str(e)}

    finally:
        session.close()
'''
