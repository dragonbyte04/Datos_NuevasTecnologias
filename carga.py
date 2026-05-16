import requests
import pandas as pd
import matplotlib.pyplot as plt 

def cargar_archivo(ruta):
    try:
        df = pd.read_csv(ruta)
        print(f"Archivo {ruta} cargado con éxito.")
        return df
    except Exception as e:
        print(f"Error al cargar: {e}")
        return None

url = 'https://6a08c14ee7e3f433d482d09c.mockapi.io/Cursos'

response = requests.get(url)
# 1. Verificamos si la petición fue exitosa
if response.status_code == 200:
    # 2. Si lo fue, extraemos el contenido JSON
    datos = response.json()
    print("¡Petición exitosa!")
    print("Tipo de datos recibidos:", type(datos))
    print("Contenido:", datos)
    # A partir de aquí, podrías cargar 'datos' en un DataFrame de Pandas
    # df = pd.DataFrame([datos])
else:
    print(f"Error al hacer la petición. Código de estado: {response.status_code}")
df = pd.DataFrame(datos)
print(df)
df.info()
df['id'] = df['id'].astype('int64')
df.info()

# 1. Preparar el lienzo (Ancho, Alto en pulgadas)
plt.figure(figsize=(10, 6))

colores=['blue', 'red', 'orange', 'yellow']
# 2. Pintar el gráfico (usando la integración directa de Pandas)
df.plot(kind='bar', x='Categoria', y='id', color='blue')
# 3. Personalización y Contexto (Metadata)
plt.title("Dificultad de curso más Común", fontsize=14)
plt.xlabel("Nivel de dificultad")
plt.ylabel("Frecuencia")
plt.xticks(rotation=45) # Rotar textos para que no colisionen

plt.savefig("./data/reports/reporte_impresion.png", format='png', dpi=300, bbox_inches='tight')
plt.savefig("./data/reports/reporte_web.svg", format='svg', bbox_inches='tight')
plt.savefig("./data/reports/reporte_ejecutivo.pdf", format='pdf', bbox_inches='tight')

# 4. Renderizar (Mostrar a pantalla)
plt.show()

# Opción A: PNG (Rasterizado / Mapa de Bits)
# Ideal para: PowerPoint, Word, correos electrónicos o impresión física.
# Parámetro técnico: dpi=300 (Puntos por pulgada). Es el estándar internacional 
# para calidad de imprenta. Si omites el DPI, se guardará a 72 o 100 DPI (se verá borroso).
#plt.savefig("reporte_impresion.png", format='png', dpi=300, bbox_inches='tight')

# Opción B: SVG (Vectorial / Matemático)
# Ideal para: Páginas web, aplicaciones interactivas o diseño gráfico (Illustrator/Figma).
# No usa DPI porque no está hecho de píxeles, sino de fórmulas matemáticas. 
# Puedes hacerle zoom infinito sin que se pixele.
#plt.savefig("reporte_web.svg", format='svg', bbox_inches='tight')

# Opción C: PDF (Vectorial Empaquetado)
# Ideal para: Informes formales, adjuntos gerenciales o entregables académicos.
# Al igual que el SVG, el PDF guarda los gráficos de forma vectorial, garantizando
# texto nítido sin importar cuánto zoom haga el gerente.
#plt.savefig("reporte_ejecutivo.pdf", format='pdf', bbox_inches='tight')




