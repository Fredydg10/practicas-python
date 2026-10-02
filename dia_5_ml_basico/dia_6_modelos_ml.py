import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree

print("\n=== Día 6: Modelos de ML Regresión Logística y Árboles de Decisión ===\n")


# 1. Regresión Logística: ¿Es Spam?

print("--- REGRESIÓN LOGÍSTICA: ¿Es Spam? ---\n")

X_train = np.array([
    [50, 0, 0], [200, 5, 3], [80, 1, 0],
    [300, 8, 5], [60, 0, 1], [250, 6, 4]
])
y_train = np.array([0, 1, 0, 1, 0, 1])

modelo_spam = LogisticRegression()
modelo_spam.fit(X_train, y_train)

emails_nuevos = np.array([[100, 2, 1], [400, 10, 7]])
predicciones = modelo_spam.predict(emails_nuevos)
probabilidades = modelo_spam.predict_proba(emails_nuevos)

for i, email in enumerate(emails_nuevos):
    tipo = "SPAM !!!" if predicciones[i] == 1 else "Normal"
    print(f"Email {email} → {tipo} (Probabilidad: {probabilidades[i][1]*100:.1f}%)")


# ==========================================
# 2. Arboles de Decisión: ¿Aprobar Préstamo?
# ==========================================
print("\n--- ÁRBOLES DE DECISIÓN: ¿Aprobar Préstamo? ---\n")

X_train_prestamo = np.array([
    [5000, 200, 1], [2000, 800, 0], [4000, 300, 1],
    [1500, 1000, 0], [6000, 100, 1], [2500, 600, 1]
])
y_train_prestamo = np.array([1, 0, 1, 0, 1, 0])

arbol = DecisionTreeClassifier(max_depth=3, random_state=42)
arbol.fit(X_train_prestamo, y_train_prestamo)

solicitantes = np.array([[4500, 250, 1], [1800, 900, 0]])
decisiones = arbol.predict(solicitantes)

for i, sol in enumerate(solicitantes):
    decision = "APROBADO" if decisiones[i] == 1 else "RECHAZADO"
    print(f"Solicitante {sol} → {decision}")

# Gráfico mejorado
fig, ax = plt.subplots(figsize=(16, 10))
plot_tree(arbol, 
          feature_names=['Ingreso', 'Deuda', 'Historial'], 
          class_names=['Rechazado', 'Aprobado'], 
          filled=True, 
          rounded=True,
          fontsize=12,
          impurity=False,
          proportion=True)

plt.tight_layout()
plt.title("Árbol de Decisión: Aprobación de Préstamos", fontsize=16, pad=20)
plt.show()

print("\n ¡Día 6 completado!")