#Tener las librerias necesarias instaladas para ejecutar este script de: pandas, numpy, matplotlib, seaborn, sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

# Configuración visual profesional
sns.set_theme(style="whitegrid")

print("="*70)
print("Día 15: Predicción de Precios de Vivienda( Machine Learning )")
print("="*70)

# Fase 1: Carga de datos (California Housing Dataset)
print("\n[1/5] Cargando el dataset de California Housing...")
california = fetch_california_housing()
df = pd.DataFrame(california.data, columns=california.feature_names)
df['Precio'] = california.target # El precio está en cientos de miles de dólares

print(f"Dataset cargado: {df.shape[0]} filas, {df.shape[1]} columnas.")
print("\n--- Primeras 5 filas ---")
print(df.head())

# Fase 2: Preprocesamiento (Train/Test Split)
print("\n[2/5] Dividiendo datos en Entrenamiento (80%) y Prueba (20%)...")

# X = Características (ingreso, edad de la casa, habitaciones, etc.)
# y = Variable objetivo (Precio)
X = df.drop('Precio', axis=1)
y = df['Precio']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalado de características (Crucial para Regresión Lineal)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("Datos divididos y escalados correctamente.")

# Fase 3: Entrenamiento de modelos 
print("\n[3/5] Entrenando modelos de Machine Learning...")

# Modelo 1: Regresión Lineal (El baseline clásico)
modelo_lineal = LinearRegression()
modelo_lineal.fit(X_train_scaled, y_train)
pred_lineal = modelo_lineal.predict(X_test_scaled)

# Modelo 2: Random Forest (El caballo de batalla de la industria)
modelo_rf = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10)
modelo_rf.fit(X_train, y_train) # Random Forest no requiere escalado, usamos los datos originales
pred_rf = modelo_rf.predict(X_test)

print("Ambos modelos entrenados con éxito.")

# Fase 4: Evaluación de modelos
print("\n[4/5] Evaluando el rendimiento de los modelos...")

def evaluar_modelo(nombre, y_real, y_pred):
    mae = mean_absolute_error(y_real, y_pred)
    rmse = np.sqrt(mean_squared_error(y_real, y_pred))
    r2 = r2_score(y_real, y_pred)
    print(f"\n--- {nombre} ---")
    print(f"  • MAE (Error Absoluto Medio): ${mae*1000:,.2f}")
    print(f"  • RMSE (Raíz del Error Cuadrático): ${rmse*1000:,.2f}")
    print(f"  • R² (Precisión explicada): {r2:.2%}")

evaluar_modelo("Regresión Lineal", y_test, pred_lineal)
evaluar_modelo("Random Forest", y_test, pred_rf)

# Fase 5: Visualización e Insights
print("\n[5/5] Generando visualizaciones de resultados...")

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Gráfico 1: Valores Reales vs Predichos (Random Forest)
axes[0].scatter(y_test, pred_rf, alpha=0.3, color='#1f77b4')
axes[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
axes[0].set_xlabel('Precio Real (Cientos de miles de $)')
axes[0].set_ylabel('Precio Predicho (Cientos de miles de $)')
axes[0].set_title('Random Forest: Reales vs Predichos\n(Línea roja = Predicción perfecta)')

# Gráfico 2: Importancia de las Características
importancia = pd.DataFrame({
    'Caracteristica': X.columns,
    'Importancia': modelo_rf.feature_importances_
}).sort_values(by='Importancia', ascending=True)

sns.barplot(x='Importancia', y='Caracteristica', data=importancia, ax=axes[1], palette='viridis')
axes[1].set_title('¿Qué factores aumentan más el precio de la casa?')
axes[1].set_xlabel('Importancia en el Modelo')

plt.tight_layout()
plt.savefig("resultados_prediccion_precios.png", dpi=300, bbox_inches='tight')
print("✅ Gráficos guardados como 'resultados_prediccion_precios.png'")
plt.show()

print("\n" + "="*70)
print("🎉 ¡DÍA 15 COMPLETADO! El modelo Random Forest es claramente superior.")
print("="*70)