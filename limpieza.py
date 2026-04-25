import pandas as pd

def limpiar_usuarios(df):
    df_limpio = df.copy()
    df_limpio = df_limpio.dropna(subset=["nombre", "apellido"])
    df_limpio = df_limpio[df_limpio["apellido"].str.strip() != ""]
    df_limpio = df_limpio[(df_limpio["edad"] >= 0) & (df_limpio["edad"] <= 100)]
    df_limpio = df_limpio[df_limpio["email"].str.contains(r"@.*\.", na=False, regex=True)]

    df_limpio["genero"] = df_limpio["genero"].replace({
        "M": "Masculino",
        "F": "Femenino",
        "masculino": "Masculino",
        "femenino": "Femenino"
    })

    df_limpio["ciudad"] = df_limpio["ciudad"].str.capitalize()
    df_limpio["departamento"] = df_limpio["departamento"].str.capitalize()
    df_limpio["pais"] = df_limpio["pais"].str.capitalize()

    df_limpio["password"] = df_limpio["password"].astype(str)
    df_limpio = df_limpio[df_limpio["password"].str.len() >= 3]
    df_limpio = df_limpio.reset_index(drop=True)

    return df_limpio

def limpiar_cursos(df):
    print("Columnas originales:")
    print(df.columns)
    
    df.columns = df.columns.str.strip()
    df = df.replace(["", " ", "null", "None"], pd.NA)
    
    columnas_texto = ["nombreCurso", "descripcionCurso", "categoria", "dificultad"]
    for col in columnas_texto:
        df[col] = df[col].astype(str).str.strip()

    df["dificultad"] = df["dificultad"].replace({
        "medio": "intermedio",
        "basico": "básico",
        "avanzado": "avanzado"
    })

    df["numeroNiveles"] = pd.to_numeric(df["numeroNiveles"], errors="coerce")
    df = df[(df["numeroNiveles"] >= 1) & (df["numeroNiveles"] <= 10)]
    df = df.dropna(subset=["nombreCurso", "descripcionCurso", "numeroNiveles"])

    df["nombreCurso"] = df["nombreCurso"].replace({
        "fundamentos java": "fundamentos de java",
        "spring boot avanzado": "spring boot avanzado",
        "arquitectura microservicios spring cloud": "arquitectura de microservicios con spring cloud"
    })

    df.to_csv("cursos_limpio.csv", index=False)
    print("Limpieza completada. Archivo guardado como cursos_limpio.csv")
    print(df.head())

    return df