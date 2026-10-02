#Tener instalando las librebrias de numpy, matplotlib y seaborn para ejecutar este script
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración para que los gráficos se vean bonitos  (estilo Seaborn)
sns.set_theme(style="whitegrid")

print("=== DÍA 13: PROBABILIDAD Y DISTRIBUCIONES ===\n")

# 1. PROBABILIDAD BÁSICA (Simulación)
# Calculas la probabilidad de que salga cara con P = 1/2, En Python, podemos SIMULAR lanzar una moneda 1000 veces para verlo en acción.

lancamientos = np.random.choice(['Cara', 'Cruz'], size=1000)
probabilidad_cara = np.sum(lancamientos == 'Cara') / len(lancamientos)

print(f"--- Simulación de Moneda ---")
print(f"Lanzamos la moneda 1000 veces.")
print(f"Probabilidad empírica de que salga 'Cara': {probabilidad_cara:.2f} (Debería ser cercano a 0.50)\n")


# 2. DISTRIBUCIÓN NORMAL (La famosa Campana de Gauss)
# Esta es la distribución más importante en Data Analytics,Vamos a simular las alturas de 1000 personas.La mayoría mide alrededor de 1.70m (media), y pocos miden 1.40m o 2.00m.

# Atento: Vamos a Generar 1000 datos aleatorios con Distribución Norma,  media (mu) = 1.70 metros, desviación estándar (sigma) = 0.10
alturas = np.random.normal(loc=1.70, scale=0.10, size=1000)

print("--- Distribución Normal (Alturas) ---")
print(f"Media de la muestra: {np.mean(alturas):.2f} m")
print(f"Desviación Estándar: {np.std(alturas):.2f} m\n")

# 3. VISUALIZAR LA DISTRIBUCIÓN
# Aquí es donde la magia ocurre. Graficamos un histograma con la curva normal encima.

plt.figure(figsize=(10, 6))

# Histograma de los datos (los barritas)
sns.histplot(alturas, bins=30, kde=True, color='skyblue', stat='density')

# Títulos y etiquetas
plt.title("Distribución Normal: Alturas de 1000 Personas", fontsize=14)
plt.xlabel("Altura (metros)", fontsize=12)
plt.ylabel("Densidad de probabilidad", fontsize=12)

# Mostrar el gráfico. Va demorar un poco ejecutando toda la script y es depediendo el tipo de computadora, pero es normal. Paciencia.
plt.show()

print("¡Gráfico generado! Deberías ver la clásica 'Campana de Gauss'.")

#Si les manda un error que no deja abrir la ventana del gráfico, tienen que cambiar el permiso de en la seguridad de aplicaciones,Hagan estos pasos:
# 1. Presionar el boton de widnows y escribir "Seguridad de Windows" y abrirlo
# 2. Ir a "Seguridad de Windows" -> "Protección contra virus y amenazas >- " 
# 3. Se van a la seccion de abajo que diga exclusiones y le dan click en "Agregar o quitar exclusiones"
# 4. Le dan click en "Agregar una exclusión" y seleccionan "Carpeta" IMPORTANTE!
# 5. Seleccionan la carpeta donde tienen el proyecto de python y listo, ya no les va a salir el error y van a poder abrir la ventana del gráfico.