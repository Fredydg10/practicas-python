#Tener las librerias para ejecutar este script que son: pandas, numpy y datetime.
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("Generando dataset de Ventas Superstore...")
np.random.seed(42)

fechas = [datetime(2023, 1, 1) + timedelta(days=i) for i in range(365)]
categorias = ['Tecnología', 'Muebles', 'Oficina']
productos = {
    'Tecnología': ['Laptop', 'Teléfono', 'Tablet', 'Monitor'],
    'Muebles': ['Silla', 'Escritorio', 'Estantería', 'Sofá'],
    'Oficina': ['Papel', 'Bolígrafos', 'Carpetas', 'Engrapadora']
}
regiones = ['Norte', 'Sur', 'Este', 'Oeste']

data = []
for _ in range(1000):
    fecha = np.random.choice(fechas)
    cat = np.random.choice(categorias)
    prod = np.random.choice(productos[cat])
    reg = np.random.choice(regiones)
    
    # Lógica de negocio: Tecnología vende más, Muebles tiene mayor margen pero menos volumen
    if cat == 'Tecnología':
        ventas = np.random.uniform(500, 2000)
        beneficio = ventas * np.random.uniform(0.15, 0.25)
    elif cat == 'Muebles':
        ventas = np.random.uniform(200, 1500)
        beneficio = ventas * np.random.uniform(0.20, 0.35)
    else:
        ventas = np.random.uniform(50, 300)
        beneficio = ventas * np.random.uniform(0.30, 0.50)
        
    data.append([fecha.strftime('%Y-%m-%d'), cat, prod, reg, round(ventas, 2), round(beneficio, 2)])

df = pd.DataFrame(data, columns=['Fecha', 'Categoria', 'Producto', 'Region', 'Ventas', 'Beneficio'])
df.to_csv('ventas_superstore.csv', index=False)
print("✅ Dataset 'ventas_superstore.csv' generado exitosamente en la carpeta.")