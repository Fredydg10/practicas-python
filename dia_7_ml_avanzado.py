# Importante tener las librerias instaladas de: numpy, matplotlib y scikit-learn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
from sklearn.datasets import make_blobs

print("=== Día 17: Clustering y Métricas de ML ===\n")

# 1. K-Means Clustering (Segmentación de Clientes)
print("--- 1. Agrupando Clientes con K-Means ---")

# Generamos datos simulados: 150 clientes con 2 características (Edad y Gasto Anual)
# make_blobs crea grupos naturales para que el algoritmo los encuentre
X, _ = make_blobs(n_samples=150, centers=3, cluster_std=1.5, random_state=42)

# Creamos y entrenamos el modelo (le decimos que busque 3 grupos)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
etiquetas_grupos = kmeans.fit_predict(X)

print(f" Modelo entrenado. Se encontraron 3 grupos de clientes.")
print(f"Centros de los grupos (Edad, Gasto): \n{kmeans.cluster_centers_}\n")

# Visualizar los grupos
plt.figure(figsize=(10, 6))
# Graficamos los puntos, coloreados según el grupo que les asignó K-Means
plt.scatter(X[:, 0], X[:, 1], c=etiquetas_grupos, cmap='viridis', s=50, alpha=0.8, label='Clientes')
# Graficamos los centroides (el centro de cada grupo) con una X roja
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', s=200, marker='X', label='Centroides')

plt.title("Segmentación de Clientes con K-Means")
plt.xlabel("Característica 1 (ej. Edad)")
plt.ylabel("Característica 2 (ej. Gasto Anual)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# 2. Métricas de Evaluación (Clasificación)

print("\n--- 2. Métricas de Evaluación ---")

# Imagina que tenemos 10 emails. 1 = Spam, 0 = Normal
y_reales =    [0, 0, 0, 0, 0,  1, 1, 1, 1, 1]  # La verdad (5 normales, 5 spam)
y_predichos = [0, 0, 0, 1, 0,  1, 1, 0, 1, 1]  # Lo que predijo nuestro modelo

# El modelo se equivocó en dos: 
# - Dijo que el 4to era Spam (era Normal) -> Falso Positivo
# - Dijo que el 8vo era Normal (era Spam) -> Falso Negativo

accuracy = accuracy_score(y_reales, y_predichos)
precision = precision_score(y_reales, y_predichos)
recall = recall_score(y_reales, y_predichos)

print(f"Accuracy (Exactitud) : {accuracy:.2f}  -> (Acertó 8 de 10)")
print(f"Precision (Precisión): {precision:.2f}  -> (De los que dijo 'Spam', el 80% realmente lo era)")
print(f"Recall (Sensibilidad): {recall:.2f}  -> (De los que eran 'Spam' de verdad, atrapó el 80%)\n")

print("--- Reporte Completo de Scikit-Learn ---")
print(classification_report(y_reales, y_predichos, target_names=['Normal (0)', 'Spam (1)']))