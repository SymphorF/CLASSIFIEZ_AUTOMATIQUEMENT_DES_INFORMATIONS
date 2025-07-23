# test supression des valeurs manquantes
import pandas as pd

def drop_missing(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()
