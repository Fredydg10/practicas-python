import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

print("=== Día 5: Machine Learning Básico ===\n")

# 1. Datos de entrenamiento (tamaño en m², precio en miles de USD)
# Estos son datos REALES que le damos al modelo para que aprenda

X_train = np.array([[50], [70], [90], [110], [130], [150]])  # Característica (tamaño)
y_train = np.array([150, 210, 270, 330, 390, 450])           # Respuesta (precio)

# 2. Se crea el modelo
modelo = LinearRegression()

# 3. Entrenar el modelo (aquí es donde "aprende o entiende de los datos")
modelo.fit(X_train, y_train)
print(" Modelo entrenado con éxito!")

# 4. Ver qué aprendió el modelo

print(f"\n--- Lo que el modelo aprendió ---")
print(f"Pendiente (coeficiente): {modelo.coef_[0]:.2f}")
print(f"Intercepto: {modelo.intercept_:.2f}")
print(f"Interpretación: Por cada m² adicional, el precio sube ${modelo.coef_[0]:.2f}k")

# 5. ¡Predecir el futuro! (datos nuevos que el modelo nunca vio)

casas_nuevas = np.array([[80], [120], [200]])  # 3 casas nuevas
precios_predichos = modelo.predict(casas_nuevas)

print(f"\n--- Predicciones ---")
for i, tamaño in enumerate(casas_nuevas):
    print(f"Casa de {tamaño[0]}m² → Precio predicho: ${precios_predichos[i]:.2f}k")

# 6. Visualizacion de los resultados pd:importante tener paciencia cuando corra el programa, ya que puede tardar un poco en mostrar la gráfica por el tipo de pc que tengas

plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color='blue', label='Datos reales')
plt.plot(X_train, modelo.predict(X_train), color='red', linewidth=2, label='Línea de regresión')
plt.scatter(casas_nuevas, precios_predichos, color='green', s=100, label='Predicciones', marker='X')
plt.xlabel("Tamaño (m²)")
plt.ylabel("Precio (miles USD)")
plt.title("Regresión Lineal: Precio de Casas")
plt.legend()
plt.grid(True)
plt.show()