#Tener las librerías necesarias de pandas, numpy, matplotlib, seaborn y scikit-learn instaladas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import warnings
warnings.filterwarnings('ignore')

print("="*60)
print("Día 11: Mini Proyecto Integrado - Predicción de Ventas E-Commerce")
print("="*60)

# FASE 1: EXTRACCIÓN (Simulación de Datos)

print("\n[1/5] Generando dataset simulado de E-commerce...")
np.random.seed(42)
fechas = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
n_registros = len(fechas) * 3  # 3 ventas promedio por día

data = {
    'fecha': np.random.choice(fechas, n_registros),
    'categoria': np.random.choice(['Electrónica', 'Ropa', 'Hogar', 'Deportes'], n_registros),
    'precio_unitario': np.random.uniform(20, 500, n_registros),
    'calificacion_producto': np.random.choice([1, 2, 3, 4, 5], n_registros, p=[0.05, 0.05, 0.15, 0.35, 0.40]),
    'es_promocion': np.random.choice([0, 1], n_registros, p=[0.7, 0.3])
}
df = pd.DataFrame(data)

# Simulamos la variable objetivo (cantidad vendida) con algo de ruido y lógica de negocio
# (Más promociones y mejores calificaciones = más ventas)
df['cantidad_vendida'] = (df['es_promocion'] * 5) + (df['calificacion_producto'] * 2) + np.random.normal(5, 2, n_registros)
df['cantidad_vendida'] = df['cantidad_vendida'].clip(lower=1).astype(int) # Mínimo 1 venta

print(f"Dataset generado: {df.shape[0]} filas, {df.shape[1]} columnas.")

# Fase 2: Transformación (ETL y Feature Engineering)
print("\n[2/5] Aplicando pipeline ETL y Feature Engineering...")

# 1. Ordenar por fecha
df = df.sort_values('fecha').reset_index(drop=True)

# 2. Extraer características de la fecha (¡Clave para series de tiempo!)
df['mes'] = df['fecha'].dt.month
df['dia_semana'] = df['fecha'].dt.dayofweek # 0=Lunes, 6=Domingo
df['es_fin_de_semana'] = df['dia_semana'].apply(lambda x: 1 if x >= 5 else 0)

# 3. Calcular el ingreso total por transacción
df['ingreso_total'] = df['precio_unitario'] * df['cantidad_vendida']

# 4. Codificación de variables categóricas (One-Hot Encoding)
df = pd.get_dummies(df, columns=['categoria'], drop_first=True)

print(f"ETL completado. Nuevas features creadas: {df.shape[1]} columnas totales.")

# Fase 3: Análisis Exploratorio de Datos (EDA)
print("\n[3/5] Ejecutando Análisis Exploratorio de Datos (EDA)...")

# Agrupar ventas por mes
ventas_mensuales = df.groupby('mes')['ingreso_total'].sum().reset_index()
print("\n--- Top 3 Categorías por Ingreso ---")

# Revertir el get_dummies para agrupar (simplificado para el ejemplo)
categorias_cols = [col for col in df.columns if col.startswith('categoria_')]
for col in categorias_cols:
    nombre_cat = col.replace('categoria_', '')
    ingreso = df[df[col] == 1]['ingreso_total'].sum()
    print(f"  • {nombre_cat}: ${ingreso:,.2f}")

# Fase 4: Modelado (Machine Learning)
print("\n[4/5] Entrenando modelo de Machine Learning (Random Forest)...")

# Definir features (X) y variable objetivo (y)
# Quitamos 'fecha' e 'ingreso_total' porque son la fecha cruda y lo que queremos predecir indirectamente
features = ['precio_unitario', 'calificacion_producto', 'es_promocion', 'mes', 'dia_semana', 'es_fin_de_semana'] + categorias_cols
X = df[features]
y = df['cantidad_vendida']

# Dividir en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
modelo = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=5)
modelo.fit(X_train, y_train)

# Predecir
y_pred = modelo.predict(X_test)

# Evaluar
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Modelo entrenado.")
print(f"   • Error Absoluto Medio (MAE): {mae:.2f} unidades")
print(f"   • Precisión del Modelo (R²): {r2:.2%} (Más cercano a 100% es mejor)")


# Fase 5: Exportación de Resultados
print("\n[5/5] Exportando resultados y predicciones...")

# Crear un DataFrame con las predicciones vs la realidad
resultados = pd.DataFrame({
    'Venta_Real': y_test.values,
    'Venta_Predicha': np.round(y_pred, 0)
})
resultados.to_csv("predicciones_ventas.csv", index=False)

# Guardar la importancia de las características
importancia = pd.DataFrame({
    'Feature': features,
    'Importancia': modelo.feature_importances_
}).sort_values(by='Importancia', ascending=False)

importancia.to_csv("importancia_features.csv", index=False)

print("="*60)
print("¡PROYECTO COMPLETADO CON ÉXITO!")
print("Archivos generados: 'predicciones_ventas.csv' e 'importancia_features.csv'")
print("="*60)

# Opcional: Mostrar gráfico de importancia
plt.figure(figsize=(10, 6))
sns.barplot(x='Importancia', y='Feature', data=importancia, palette='viridis')
plt.title('Importancia de Características en la Predicción de Ventas')
plt.xlabel('Importancia')
plt.ylabel('Característica')
plt.tight_layout()
plt.show()