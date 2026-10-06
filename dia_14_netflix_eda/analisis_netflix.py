# Tener las librerias instaladas de pandas, matplotlib y seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# Configuración de estilo para que los gráficos se vean profesionales
sns.set_theme(style="whitegrid", palette="muted")

print("="*60)
print("Día 14: EDA de Netflix Movies & TV Shows")
print("="*60)

# FASE 1: CARGA Y EXPLORACIÓN INICIAL
print("\n[1/4] Cargando y explorando el dataset...")
df = pd.read_csv("netflix_titles.csv")
print(f"Dataset cargado: {df.shape[0]} filas, {df.shape[1]} columnas.")
print("\n--- Primeras 5 filas ---")
print(df[['type', 'title', 'release_year', 'country']].head())

print("\n--- Valores nulos por columna ---")
print(df.isnull().sum())

# Fase 2 : Limpieza de datos
print("\n[2/4] Limpiando datos...")

# 1. Rellenar valores nulos en columnas categóricas con 'Desconocido'
df['country'] = df['country'].fillna('Desconocido')
df['director'] = df['director'].fillna('Desconocido')
df['cast'] = df['cast'].fillna('Desconocido')

# 2. Convertir 'date_added' a formato de fecha real
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

# 3. Eliminar filas donde el año de agregado sea nulo (no se pudo convertir)
df = df.dropna(subset=['year_added'])
df['year_added'] = df['year_added'].astype(int)

print(f"Limpieza completada. Filas restantes: {df.shape[0]}")


# Fase 3: Visualización de datos y análisis exploratorio
print("\n[3/4] Generando visualizaciones...")

# Crear una figura con 4 subgráficos (2x2)
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Análisis Exploratorio: Catálogo de Netflix', fontsize=20, fontweight='bold')

# Gráfico 1: Películas vs Series (Conteo)
sns.countplot(x='type', data=df, ax=axes[0, 0], palette=['#E50914', '#221f1f'])
axes[0, 0].set_title('Distribución: Películas vs Series de TV', fontsize=14)
axes[0, 0].set_ylabel('Cantidad')
axes[0, 0].tick_params(axis='x', labelsize=12)

# Gráfico 2: Tendencia de contenido agregado por año
conteo_anual = df['year_added'].value_counts().sort_index()
sns.lineplot(x=conteo_anual.index, y=conteo_anual.values, ax=axes[0, 1], color='#E50914', marker='o', linewidth=2)
axes[0, 1].set_title('Tendencia: Contenido Agregado por Año', fontsize=14)
axes[0, 1].set_xlabel('Año')
axes[0, 1].set_ylabel('Cantidad de Títulos')
axes[0, 1].tick_params(axis='x', rotation=45)

# Gráfico 3: Top 10 Países con más contenido
# (Agrupamos por país, ignorando 'Desconocido' para el top)
top_paises = df[df['country'] != 'Desconocido']['country'].value_counts().head(10)
sns.barplot(x=top_paises.values, y=top_paises.index, ax=axes[1, 0], palette='Blues_r')
axes[1, 0].set_title('Top 10 Países Productores de Contenido', fontsize=14)
axes[1, 0].set_xlabel('Cantidad de Títulos')

# Gráfico 4: Top 5 Géneros más comunes
# Separamos los géneros que vienen juntos (ej: "Drama, International")
todos_los_generos = df['listed_in'].str.split(',').explode().str.strip()
top_generos = todos_los_generos.value_counts().head(5)
sns.barplot(x=top_generos.values, y=top_generos.index, ax=axes[1, 1], palette='Greens_r')
axes[1, 1].set_title('Top 5 Géneros/Categorías en Netflix', fontsize=14)
axes[1, 1].set_xlabel('Cantidad de Títulos')

# Ajustar diseño y mostrar
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("dashboard_netflix_eda.png", dpi=300, bbox_inches='tight') # Guarda la imagen en alta calidad
print("Gráficos generados y guardados como 'dashboard_netflix_eda.png'")
plt.show()

# FASE 4: STORYTELLING (Insights Clave)
print("\n[4/4] Insights Clave (Data Storytelling):")
total_peliculas = (df['type'] == 'Movie').sum()
total_series = (df['type'] == 'TV Show').sum()
pico_anio = conteo_anual.idxmax()
max_contenido = conteo_anual.max()

print(f"📌 1. Netflix tiene {total_peliculas} películas y {total_series} series en su catálogo.")
print(f"📌 2. El año con mayor crecimiento de contenido fue {int(pico_anio)}, agregando {max_contenido} títulos.")
print(f"📌 3. Estados Unidos domina la producción, pero el contenido 'International' y 'Drama' son los géneros más frecuentes a nivel global.")
print("\n🎉 ¡Análisis del Día 24 completado con éxito!")

#Importante al correr el mini programa demorara un poco en generar los gráficos debido a la cantidad de datos y la complejidad de las visualizaciones y por los permisos de su pc
#Recuerden darle permisos a la carpeta donde se guardara el archivo dashboard_netflix_eda.png para que no de error al guardar la imagen en seguridad de windows como esta en el repositorio de github de los primeros mini programas :)