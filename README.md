
# ACTIVIDAD DE LIMPIEZA DE DATOS

### Entorno virtul e instalaciones

- Se crea el entorno virtul
- Se activa entorno virtual
- instalacion de pandas
- instalacion de `requirements.txt`

### Creacion de carpetas y archivos

- Se crea la carpeta data donde tendra implementadas las carpetas raw y processed
- Se crea `READMEE.md`

| Archivo | Descripción |
| :--- | :--- |
| `main.py` | Punto de entrada de la aplicación. Gestiona el menú interactivo. |
| `carga.py` | Módulo encargado de la lectura de archivos CSV utilizando Pandas. |
| `limpieza.py` | Contiene toda la lógica de limpieza, normalización y filtrado de datos. |
| `.gitignore` | Configuración para evitar subir archivos temporales (`__pycache__`) y entornos virtuales. |

## Descripción de los Componentes

### 1. Interfaz de Usuario (`main.py`)
Es el controlador principal del programa. Implementa un bucle `while` con un menú de opciones que permite al usuario:
* **Cargar datos:** Seleccionar entre archivos de "datos" o "cursos".
* **Limpiar datos:** Ejecutar los procesos de transformación sobre los datos cargados.
* **Mostrar datos:** Visualizar las primeras filas y la información estructural (`df.info()`) de los DataFrames.

### 2. Módulo de Carga (`carga.py`)
Contiene funciones robustas para la importación de datos.
* **`cargar_datos(ruta)`**: Lee archivos de usuarios.
* **`cargar_cursos(ruta)`**: Lee archivos de cursos.
Ambas funciones incluyen manejo de excepciones (`try-except`) para asegurar que el programa no se detenga si un archivo no existe o está dañado.

### 3. Módulo de Limpieza (`limpieza.py`)
Es el centro técnico del proyecto. Realiza las siguientes operaciones:

**Para los Datos de Usuarios:**
* **Filtrado de Nulos:** Elimina registros sin nombre o apellido.
* **Validación de Edad:** Filtra registros fuera del rango lógico (0 a 100 años).
* **Validación de Email:** Usa expresiones regulares (Regex) para asegurar que el correo tenga un formato válido (`@` y `.`).
* **Normalización:** Convierte géneros (M/F) a formato completo y pone en mayúscula inicial ciudades y departamentos.

**Para los Datos de Cursos:**
* **Normalización de Texto:** Limpia espacios en blanco y estandariza nombres de cursos y categorías.
* **Corrección de Dificultad:** Mapea valores como "medio" a "intermedio" y añade tildes necesarias ("básico").
* **Validación de Niveles:** Convierte a numérico y filtra cursos que no tengan entre 1 y 10 niveles.

## Archivos de Salida
Tras ejecutar la limpieza, el programa genera archivos optimizados listos para análisis de datos o carga en bases de datos:
* `datos_limpios.csv`
* `cursos_limpios.csv`

###Listado de dependencias 

numpy==2.4.4
pandas==3.0.2
python-dateutil==2.9.0.post0
six==1.17.0
tzdata==2026.2