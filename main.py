import pandas as pd
import limpieza
import carga
import analisis

df_usuarios = None
df_curso = None
isLoader = False

while True:
    print("\nMENÚ PRINCIPAL")
    print("1. Cargar")
    print("2. Limpiar")
    print("3. Mostrar")
    print("4. analisis")
    print("5. salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            print("\n¿Qué archivo deseas cargar?")
            print("1. usuarios.")
            print("2. cursos.")

            tipo = input("Seleccione una opción: ")
            if tipo == "1":
                ruta = "./data/raw/usuarios.csv"
                df_usuarios = carga.cargar_usuarios(ruta)
                df_usuarios.info()
            elif tipo == "2":
                ruta = "./data/raw/cursos.csv"
                df_curso = carga.cargar_cursos(ruta)
                df_curso.info()
            else:
                print("\nOpción inválida.")
                continue


            isLoader = True
            print ("Carga completa")

            if df_usuarios is not None:
                df_usuarios.info()
                
            if df_curso is not None:
                df_curso.info()


        case "2":
            print("\n¿Qué archivo deseas limpiar?")
            print("1. usuarios.")
            print("2. cursos.")

            tipo = input("Seleccione una opción: ")
            if tipo == "1":
                if isLoader:
                    df_limpio = limpieza.limpiar_usuarios(df_usuarios)
                    df_limpio.to_csv("./data/processed/usuarios_limpios.csv", index=False)
                    print ("\nLimpieza completada.")
            
            elif tipo == "2":
                if isLoader:
                    df_curso_limpio = limpieza.limpiar_cursos(df_curso)
                    df_curso_limpio.to_csv("./data/processed/cursos_limpio.csv", index=False)
                    print("\nLimpieza completada.")

        case "3":
            if isLoader:
                print("\nDatos actuales:")

                df_usuarios= carga.cargar_usuarios("./data/raw/usuarios.csv")
                df_curso = carga.cargar_cursos("./data/raw/cursos.csv") 
                print(df_usuarios.head())
                print(df_curso.head())
                
            else:
                print("\nNo hay datos cargados.")

        case "4":
            print("\n¿Qué deseas analizar?")
            print("1. Usuarios limpios")
            print("2. Cursos limpios")
            sub_opcion = input("Seleccione: ")

            if sub_opcion == "1":
                analisis.analizar_usuarios("./data/processed/usuarios_limpios.csv")
            elif sub_opcion == "2":
                analisis.analizar_cursos("./data/processed/cursos_limpio.csv")
            else:
                print("Opción inválida.")

        case "5":
            print("\nSaliendo del programa.")
            break

        case _:
            print("\nOpción inválida. Por favor, selecciona un número del 1 al 5.")