import pandas as pd

def cargar_archivo(ruta):
    try:
        df = pd.read_csv(ruta)
        print(f"Archivo {ruta} cargado con éxito.")
        return df
    except Exception as e:
        print(f"Error al cargar: {e}")
        return None