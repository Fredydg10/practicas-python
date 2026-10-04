# Tener instalando las librebrias de numpy, matplotlib y seaborn para ejecutar este script
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración
sns.set_theme(style="whitegrid")

print("=== DÍA 4: EDA COMPLETO - SPOTIFY SONGS ===\n")


# PASO 1: CARGAR Y EXPLORAR
# Si tienes el CSV real, usa: df = pd.read_csv("spotify_songs.csv")por ahora, creamos datos simulados para practicar:

datos_spotify = {
    'cancion': ['Song A', 'Song B', 'Song C', 'Song D', 'Song E', 'Song F', 'Song G', 'Song H'],
    'artista': ['Artista 1', 'Artista 2', 'Artista 1', 'Artista 3', 'Artista 2', 'Artista 4', 'Artista 3', 'Artista 1'],
    'genero': ['Pop', 'Rock', 'Pop', 'Jazz', 'Rock', 'Pop', 'Jazz', 'Pop'],
    'duracion_seg': [210, 245, 198, 320, 267, 203, 289, 215],
    'popularidad': [85, 72, 90, 65, 78, 88, 70, 92],
    'bailabilidad': [0.8, 0.6, 0.9, 0.4, 0.7, 0.85, 0.5, 0.95],
    'energia': [0.7, 0.9, 0.8, 0.3, 0.85, 0.75, 0.4, 0.88]
}

df = pd.DataFrame(datos_spotify)

print("--- 1. VISTA RÁPIDA ---")
print(df.head())
print(f"\nForma del dataset: {df.shape[0]} filas, {df.shape[1]} columnas\n")

print("--- 2. INFORMACIÓN Y ESTADÍSTICAS ---")
print(df.info())
print("\n", df.describe())


# PASO 2: LIMPIEZA (Simulada)

print("\n--- 3. LIMPIEZA ---")
print(f"Valores nulos por columna:\n{df.isnull().sum()}")
print(f"Duplicados: {df.duplicated().sum()}")

# PASO 3: ANÁLISIS UNIVARIADO

print("\n--- 4. ANÁLISIS UNIVARIADO ---")

# Distribución de géneros
print("Conteo por género:")
print(df['genero'].value_counts())

# Histograma de popularidad
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
sns.histplot(df['popularidad'], bins=5, kde=True)
plt.title("Distribución de Popularidad")

# Boxplot de duración por género
plt.subplot(1, 2, 2)
sns.boxplot(x='genero', y='duracion_seg', data=df)
plt.title("Duración por Género")
plt.tight_layout()
plt.show()


# PASO 4: ANÁLISIS BIVARIADO

print("\n--- 5. ANÁLISIS BIVARIADO ---")

# ¿Las canciones más bailables son más populares?
correlacion = df['bailabilidad'].corr(df['popularidad'])
print(f"Correlación entre bailabilidad y popularidad: {correlacion:.3f}")

# Scatter plot
plt.figure(figsize=(8, 5))
sns.scatterplot(x='bailabilidad', y='popularidad', hue='genero', size='energia', data=df)
plt.title("Bailabilidad vs Popularidad (tamaño = energía)")
plt.show()

# PASO 5: CONCLUSIONES

print("\n--- 6. CONCLUSIONES DEL EDA ---")
genero_mas_popular = df.groupby('genero')['popularidad'].mean().idxmax()
print(f"El género con mayor popularidad promedio es: {genero_mas_popular}")
print(f"La canción más popular es: {df.loc[df['popularidad'].idxmax(), 'cancion']}")
print(f"Correlación bailabilidad-popularidad: {'Positiva' if correlacion > 0 else 'Negativa'} ({correlacion:.2f})")