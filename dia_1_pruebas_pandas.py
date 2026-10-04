# Antes de comenzar, importante tener instalado pandas para ejecutar este script
import pandas as pd

# 1. Nuestro "array de objetos" (datos simulados o random)
datos_ventas = [
    {"producto": "Laptop", "precio": 1200, "categoria": "Electrónica"},
    {"producto": "Mouse", "precio": 25, "categoria": "Electrónica"},
    {"producto": "Silla", "precio": 200, "categoria": "Muebles"},
    {"producto": "Teclado", "precio": 80, "categoria": "Electrónica"},
    {"producto": "Escritorio", "precio": 350, "categoria": "Muebles"}
]

# 2. Luego Convertirlo en la tabla mágica (DataFrame)
df = pd.DataFrame(datos_ventas)

# 3. Explorar los datos
print("=== VISTA RÁPIDA (HEAD) ===")
print(df.head())
print("\n=== INFORMACIÓN DEL DATAFRAME ===")
print(df.info())

# Uso de querys o consultas tipo SQL con Pandas 

# FILTRAR Y AGRUPAR

print("\n=== FILTRANDO: Solo productos mayores a $100 ===")
# Equivalente a SQL: WHERE precio > 100
df_filtrado = df[df["precio"] > 100]
print(df_filtrado)

print("\n=== AGRUPANDO: Suma de precios por categoría ===")
# Equivalente a SQL: SELECT categoria, SUM(precio) FROM ... GROUP BY categoria
# Nota: Aquí usamos 'df_filtrado' para que solo sume los que pasaron el filtro
df_agrupado = df_filtrado.groupby("categoria")["precio"].sum()
print(df_agrupado)

# Guarda el resultado en un archivo CSV 
df_agrupado.to_csv("resultado_analisis.csv", index=True)
print("\n ¡Listo! Revisa tu carpeta, se creó el archivo 'resultado_analisis.csv'")