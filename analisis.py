import pandas as pd

def analizar_usuarios(df):
    if df is None or df.empty:
        print("No hay datos de usuarios para analizar.")
        return

    print("\n--- ANÁLISIS DE USUARIOS ---")
    print(f"Edad promedio: {df['edad'].mean():.2f} años")
    print(f"Usuario más joven: {df['edad'].min()} años")
    print(f"Usuario mayor: {df['edad'].max()} años")

    print("\nDistribución por Género:")
    print(df['genero'].value_counts())

    print("\nTop 5 Ciudades con más usuarios:")
    print(df['ciudad'].value_counts().head(5))

def analizar_cursos(df):
    if df is None or df.empty:
        print("No hay datos de cursos para analizar.")
        return

    print("\n--- ANÁLISIS DE CURSOS ---")
    print(f"Promedio de niveles por curso: {df['numeroNiveles'].mean():.1f}")

    print("\nCantidad de cursos por Categoría:")
    print(df['categoria'].value_counts())

    # Usamos try por si la moda devuelve un conjunto vacío
    try:
        dificultad_top = df['dificultad'].mode()[0]
        print(f"\nLa dificultad más común es: {dificultad_top}")
    except IndexError:
        print("\nNo se pudo determinar la dificultad más común.")