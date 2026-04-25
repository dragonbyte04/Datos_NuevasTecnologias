import pandas as pd

def analizar_usuarios(ruta_datos):
    try:
        df = pd.read_csv(ruta_datos)
        print("\n--- ANÁLISIS DE USUARIOS ---")
        print(f"Edad promedio: {df['edad'].mean():.2f} años")
        print(f"Usuario más joven: {df['edad'].min()} años")
        print(f"Usuario mayor: {df['edad'].max()} años")

        print("\nDistribución por Género:")
        print(df['genero'].value_counts())

        print("\nTop 5 Ciudades con más usuarios:")
        print(df['ciudad'].value_counts().head(5))
        
    except Exception as e:
        print(f"Error al analizar usuarios: {e}")

def analizar_cursos(ruta_cursos):
    try:
        df = pd.read_csv(ruta_cursos)
        print("\n--- ANÁLISIS DE CURSOS ---")

        print(f"Promedio de niveles por curso: {df['numeroNiveles'].mean():.1f}")

        print("\nCantidad de cursos por Categoría:")
        print(df['categoria'].value_counts())

        dificultad_top = df['dificultad'].mode()[0]
        print(f"\nLa dificultad más común es: {dificultad_top}")
        
    except Exception as e:
        print(f"Error al analizar cursos: {e}")