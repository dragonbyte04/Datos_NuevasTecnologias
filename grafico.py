import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generar_visualizaciones(df_usuarios, df_cursos):
    # --- GRÁFICO 1: TOP 5 CIUDADES ---
    plt.figure(figsize=(10, 6))
    
    # Calculamos el top 5
    top_5_ciudades = df_usuarios['ciudad'].value_counts().head(5)
    
    sns.barplot(x=top_5_ciudades.index, y=top_5_ciudades.values, palette='viridis')
    
    plt.title('Top 5 Ciudades con Más Usuarios', fontsize=16)
    plt.xlabel('Ciudad', fontsize=12)
    plt.ylabel('Cantidad de Usuarios', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()  # Se abre la primera ventana

    # --- GRÁFICO 2: DIFICULTAD MÁS COMÚN ---
    plt.figure(figsize=(8, 5))

    df_cursos['dificultad'] = df_cursos['dificultad'].str.lower()
    
    # Usamos countplot para ver cuál se repite más
    sns.countplot(data=df_cursos, x='dificultad', palette='magma', order=df_cursos['dificultad'].value_counts().index)
    
    plt.title('Dificultad de Cursos Más Común', fontsize=16)
    plt.xlabel('Nivel de Dificultad', fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)
    plt.tight_layout()
    plt.show()  # Se abre la segunda ventana al cerrar la anterior