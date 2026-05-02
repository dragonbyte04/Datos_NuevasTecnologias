import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_ciudad = pd.read_csv('data/processed/usuarios_limpios.csv')

orden = df_ciudad['ciudad'].value_counts().index

sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

sns.countplot(data=df_ciudad, x='ciudad', color='red', hue='ciudad', legend=False)

plt.title('Distribución de Usuarios por Ciudad', fontsize=16)
plt.xlabel('Ciudad', fontsize=12)
plt.ylabel('Cantidad de Usuarios', fontsize=12)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()