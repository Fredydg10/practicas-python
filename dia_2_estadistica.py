#Importante tener instalado pandas para ejecutar este script
import pandas as pd

# 1. Creamos un dataset un poco más grande para que la estadística tenga sentido
datos_ventas = [1200, 25, 200, 80, 350, 150, 90, 1200, 45, 300]
df = pd.DataFrame(datos_ventas, columns=["precio"])

print("=== ESTADÍSTICA DESCRIPTIVA ===\n")

# 2. El comando mágico que lo hace todo
print("--- Resumen automático (describe) ---")
print(df.describe())
print("\n")

# 3. Cálculos manuales (como en la U)
print("--- Cálculos específicos ---")
print(f"Media (Promedio): {df['precio'].mean()}")
print(f"Mediana (Valor central): {df['precio'].median()}")
print(f"Moda (Más repetido): {df['precio'].mode()[0]}")
print(f"Desviación Estándar: {df['precio'].std():.2f}") # :.2f es para redondear a 2 decimales

# 4. Detectando Outliers con IQR
Q1 = df['precio'].quantile(0.25)
Q3 = df['precio'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print(f"\n--- Detección de Outliers (IQR) ---")
print(f"Rango normal: entre {limite_inferior} y {limite_superior}")

outliers = df[(df['precio'] < limite_inferior) | (df['precio'] > limite_superior)]
if not outliers.empty:
    print(f" ¡Outliers detectados!: {outliers['precio'].tolist()}")
else:
    print("✅ No hay outliers en este dataset.")
