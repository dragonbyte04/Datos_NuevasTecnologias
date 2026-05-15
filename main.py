import pandas as pd
import carga      # Importa sus funciones de carga.py
import grafico
import grafico
import limpieza   # Importa sus funciones de limpieza.py
import analisis   # Importa sus funciones de analisis.py

def menu_principal():
    # Variables para guardar los datos en la memoria del computador
    df_usuarios = None
    df_cursos = None

    while True:
        
        print("   SISTEMA DE GESTIÓN DE DATOS")
        print("1. Cargar y Limpiar Datos")
        print("2. Analizar Usuarios y Cursos")
        print("3. Realizar Merge (Unir Datos)")
        print("4. Graficos")
        print("5. salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            # Paso 1: Cargar los archivos RAW (brutos)
            u_raw = carga.cargar_archivo('data/raw/usuarios.csv')
            c_raw = carga.cargar_archivo('data/raw/cursos.csv')

            if u_raw is not None and c_raw is not None:
                df_usuarios = limpieza.limpiar_usuarios(u_raw)
                df_cursos = limpieza.limpiar_cursos(c_raw)
                print("\n¡Éxito! Los datos han sido cargados y limpiados.")
            else:
                print("\nError: Asegúrate de que los archivos existan en data/raw/")

        elif opcion == "2":
            # Validamos que primero hayan cargado los datos
            if df_usuarios is not None and df_cursos is not None:
                analisis.analizar_usuarios(df_usuarios)
                analisis.analizar_cursos(df_cursos)
            else:
                print("\nPrimero debes cargar los datos en la opción 1.")

        elif opcion == "3":
            if df_usuarios is not None and df_cursos is not None:
                print("\nUniendo tablas...")
                # Hacemos el Merge por la columna 'id_usuario'
                df_final = pd.merge(df_usuarios, df_cursos, on='idUsuarios', how='inner')
                
                # Guardamos el resultado en la carpeta processed
                df_final.to_csv('data/processed/datos_unificados.csv', index=False)
                print(f" Merge completado. Se crearon {len(df_final)} registros unificados.")
                print("Archivo guardado en: data/processed/datos_unificados.csv")
            else:
                print("\nNo hay datos suficientes para unir. Carga los archivos primero.")
                
        elif opcion == "4":
            # Validamos que existan datos antes de graficar
            if df_usuarios is not None and df_cursos is not None:
                print("\nGenerando gráficos... Por favor, cierra la ventana del gráfico para volver al menú.")
                grafico.generar_visualizaciones(df_usuarios, df_cursos)
            else:
                print("\n[!] Error: Primero debes cargar y limpiar los datos (Opción 1).")

        elif opcion == "5":
            print("\nCerrando el sistema. ¡Sigue programando!")
            break
        
        else:
            print("\nOpción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu_principal()