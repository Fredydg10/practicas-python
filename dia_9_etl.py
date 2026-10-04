#Importamos las librerías necesarias de pandas y StringIO para simular la lectura de un CSV desde un string
import pandas as pd
from io import StringIO

print("=== Día 9: Pipeline ETL(Extract, Transform, Load) ===\n")

# 1. Extraemos los datos (Extract)
# Simulamos un CSV sucio que nos mandó el sistema de ventas

datos_crudos = """id,producto,precio,fecha,categoria
1,Laptop,1200,2023-01-15,Electrónica
2,Mouse,,2023-01-20,Electrónica
3,Silla,200,2023/02/10,Muebles
4,Teclado,80,2023-02-15,
5,,350,2023-03-01,Muebles
6,Monitor,400,2023-03-05,Electrónica"""

# Leemos los datos 
df = pd.read_csv(StringIO(datos_crudos))
print("--- 1. EXTRACT: Así nos llegaron los datos (Sucios) ---")
print(df)
print(f"-> Problemas: Hay precios vacíos, fechas con formatos distintos y nombres de productos faltantes.\n")


# 2. Transformamos los datos (Transform)

print("--- 2. TRANSFORM: Limpiando los datos... ---")

# a) Eliminar filas donde falta el producto (no podemos vender algo sin nombre)
df = df.dropna(subset=['producto'])

# b) Rellenar precios vacíos con 0 (o con el promedio, pero usaremos 0 por simplicidad)
df['precio'] = df['precio'].fillna(0)

# c) Rellenar categorías vacías con 'Desconocida'
df['categoria'] = df['categoria'].fillna('Desconocida')

# d) Unificar el formato de fechas (hay unas con '-' y otras con '/')
df['fecha'] = pd.to_datetime(df['fecha'], format='mixed')

# e) Crear una nueva columna calculada (Transformación de negocio)
df['precio_con_iva'] = (df['precio'] * 1.16).round(2)

print(df)
print(f"-> ¡Datos limpios y estandarizados!\n")

# 3. Cargamos los datos limpios (Load)
# Guardamos los datos limpios en un nuevo CSV listo para Power BI o ML

df.to_csv("ventas_limpias.csv", index=False)
print("--- 3. LOAD: Datos cargados ---")
print(" Archivo 'ventas_limpias.csv' generado exitosamente.")