import pandas as pd

def cargar_usuarios(ruta_archivo):
    try:
        df_usuarios = pd.read_csv(ruta_archivo)
        print("\n¡Archivo cargado con éxito!")
        df_usuarios.info()
        return df_usuarios
    except FileNotFoundError:
        print(f"\nError: No se encontró el archivo en {ruta_archivo}")
        return df_usuarios

def cargar_cursos(ruta_archivo):
    try:
        
        df_curso = pd.read_csv(ruta_archivo)
        print("\n¡Archivo de cursos cargado con éxito!")
        return df_curso 
    except Exception as e:
        print(f"\nError al cargar cursos: {e}")
        return df_curso