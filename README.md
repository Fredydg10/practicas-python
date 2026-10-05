Diagrama Analista de Datos - Mis Prácticas

¡Hola!  Soy Fredy, Estudiante de desarrollo y gestion de software en la UTP Panamá con aspiracion a saber sobre el campo de analisis de datos. 

Este repositorio documenta un aprendizaje en la parte de codigo sobre ser analista de datos,en el lenguaje python.Aquí encontrarás scripts , ejercicios de SQL, y análisis de datos reales.

Objetivo

Dominar las herramientas y conceptos fundamentales del Análisis de Datos:
- SQL (Básico y Avanzado)
- Python para Data Analytics
- Pandas (Manipulación de datos)
- Visualización (Matplotlib, Seaborn)
- Estadística y Probabilidad
- Análisis Exploratorio de Datos (EDA)
- Data Storytelling y Comunicación de Insights


Tecnologías y Herramientas

- Lenguaje: Python 3.14
- Librerías: Pandas, NumPy, Matplotlib, Seaborn, SciPy
- Base de Datos: SQL (SQLite/MySQL)
- IDE: Visual Studio Code
- Plataformas: Kaggle, SQLZoo, HackerRank, LeetCode
- Control de Versiones: Git & GitHub


Cómo Ejecutar los Scripts?

Requisitos previos:
```bash
# Instalar Python 3.14 o superior
# Instalar las librerías necesarias:
pip install pandas numpy matplotlib seaborn scipy


Ejecutar un script:
```bash
python dia_12_estadistica.py
```
Nota sobre Windows Smart App Control:
Si usas Windows 11 y te aparece un bloqueo de seguridad, agrega tu carpeta de prácticas a las **Exclusiones** en:
`Seguridad de Windows → Protección contra virus y amenazas → Administrar la configuración → Exclusiones


Aprendizajes Clave

SQL vs Pandas
| SQL | Pandas |
|-----|--------|
| `WHERE` | `df[df["col"] > valor]` |
| `GROUP BY` | `df.groupby("col")` |
| `ORDER BY` | `df.sort_values()` |
| `JOIN` | `pd.merge()` |

 Conceptos Fundamentales
- EDA (Análisis Exploratorio de Datos):** Proceso de conocer un dataset antes de analizarlo
- Outliers: Valores atípicos detectados con IQR (Q1 - 1.5*IQR, Q3 + 1.5*IQR)
- Teorema de Bayes: Actualizar probabilidades con nueva evidencia
- Distribución Normal: La campana de Gauss, fundamental en estadística


Notas Personales

"La paciencia para entender qué hacen los datos antes de manipularlos es lo que te hace un buen analista."

Este repositorio es mi viaje de aprendizaje. Cada script representa un día de dedicación y práctica. El objetivo final es dominar el análisis de datos al 100% y aplicar estos conocimientos en proyectos reales.


Recursos Utilizados

- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [SQLZoo](https://sqlzoo.net/)
- [HackerRank SQL](https://www.hackerrank.com/domains/sql)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)


Contacto

¿Tienes preguntas o sugerencias? ¡Conectemos!

- GitHub:FredyDg10
- LinkedIn: Proximamente

Última actualización: Septiembre 2026

Instrucciones para subirlo a GitHub:

1. Guarda el archivo como `README.md` (asegúrate que la extensión sea `.md` y no `.txt`).

2. Si ya tienes un repositorio creado:
   ```bash
   git add README.md
   git commit -m "Agregar README con documentación del proyecto"
   git push origin main
   ```

3. Si aún no creas el repositorio:
   ```bash
   cd C:\Users\fredy\OneDrive\Desktop\pruebas_python
   git init
   git add .
   git commit -m "Primer commit: Roadmap Analista de Datos - Días 1-14"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   git push -u origin main
   ```

4. Reemplaza `[Tu usuario de GitHub]` y `[Tu perfil de LinkedIn]` con tus datos reales al final del README.
