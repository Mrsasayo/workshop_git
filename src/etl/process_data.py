import pandas as pd

def load_csv(filepath):
    """Carga un archivo CSV en un DataFrame."""
    return pd.read_csv(filepath)