# Shot prompting
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

# 2. Inicializar el Cliente
# Este cliente gestiona la conexión
client = genai.Client(api_key=clave_api)

resena = "Este libro empezó bien pero el final fue muy apresurado y decepcionante."

# few shot
prompt = f""" 
        Eres un clasificador de sentimientos para reseñas de libros. Debes responder con solo una palara siguiendo el formato de los ejemplos:

        Reseña: 'Una historia cautivadora y profundamente emocional que explora el poder de la amistad y el sacrificio en medio de tiempos difíciles.'
        Clasificación: Positiva

        Reseña: 'Un relato interesante, pero que a veces se siente predecible y falta de la profundidad que esperaba explorar en sus personajes principales.'
        Clasificación: Neutral

        Reseña: 'A pesar de una premisa intrigante, la trama se pierde en detalles innecesarios y deja una sensación de insatisfacción por su falta de desarrollo y cierre.'
        Clasificación: Negativa

        Reseña: "{resena}"
        """


# 3. Llamada directa al servicio de modelos
try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
except Exception as e:
    print(f"❌ Ocurrió un error en la conexión: {e}")

# 4. Imprimir la respuesta
if response:
    print("✅ Respuesta del modelo:")
    print("-" * 30)
    print(response.text)
    
  