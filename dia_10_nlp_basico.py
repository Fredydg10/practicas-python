#Importamos las librerías necesarias para el análisis de texto (pandas y sklearn)
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

print("=== Día 10: NLP Básico (Análisis de Texto) ===\n")

# Reseñas de Amazon simuladas
resenas = [
    "El producto es excelente y llegó muy rápido, me encanta.",
    "Terrible calidad, se rompió a los dos días. No lo recomiendo.",
    "Cumple su función, nada del otro mundo pero está bien.",
    "Increíble, la mejor compra que he hecho en mi vida.",
    "Pésimo servicio al cliente, nunca más compro aquí."
]


# 1. Tokenización (Dividir el texto en palabras)
print("--- 1. Tokenización ---")
print("Dividimos cada reseña en palabras individuales (tokens):\n")
for i, resena in enumerate(resenas):

    # Convertimos a minúsculas y separamos por espacios
    tokens = resena.lower().split()
    print(f"Reseña {i+1}: {tokens[:5]}...") # Mostramos las primeras 5 palabras


# ==========================================
# 2. TF-IDF (¿Qué palabras son realmente importantes?)
# ==========================================
print("\n--- 2. TF-IDF (Términos más importantes) ---")
print("Ignoramos palabras comunes ('el', 'la', 'de') y destacamos las clave:\n")

# Lista manual de stop words en español
stop_words_es = [
    "el", "la", "los", "las", "un", "una", "unos", "unas", 
    "de", "del", "al", "a", "en", "y", "o", "que", "es", 
    "son", "ser", "estar", "ha", "he", "hemos", "han",
    "me", "te", "se", "nos", "les", "lo", "le", "les",
    "mi", "tu", "su", "sus", "este", "esta", "estos", "estas",
    "muy", "más", "tan", "tanto", "como", "con", "por", "para",
    "sin", "sobre", "entre", "hasta", "desde", "cuando", "donde"
]

# El vectorizador ahora usa nuestra lista personalizada
vectorizador = TfidfVectorizer(stop_words=stop_words_es)
matriz_tfidf = vectorizador.fit_transform(resenas)

# Lo convertimos en una tabla bonita para verlo claro
df_tfidf = pd.DataFrame(matriz_tfidf.toarray(), columns=vectorizador.get_feature_names_out())
print(df_tfidf.round(2)) # Redondeamos a 2 decimales
print("\n* Los números más altos indican palabras más importantes en esa reseña.")

# 3. Análisis de Sentimiento (Básico)
print("\n--- 3. Análisis de Sentimiento ---")

# Diccionarios simples de palabras positivas y negativas
palabras_positivas = ["excelente", "rápido", "encanta", "increíble", "mejor", "bien"]
palabras_negativas = ["terrible", "rompió", "pésimo", "nunca", "no", "recomiendo"]

for i, resena in enumerate(resenas):
    texto = resena.lower()
    
    # Contamos cuántas palabras de cada tipo hay en la reseña
    pos = sum(1 for p in palabras_positivas if p in texto)
    neg = sum(1 for p in palabras_negativas if p in texto)

    # Determinamos el sentimiento
    if pos > neg:
        sentimiento = "POSITIVO 😃"
    elif neg > pos:
        sentimiento = "NEGATIVO 😡"
    else:
        sentimiento = "NEUTRAL 😐"

    print(f"Reseña {i+1}: {sentimiento} (Puntos Pos: {pos} | Puntos Neg: {neg})")