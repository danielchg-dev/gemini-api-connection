import os
from urllib import response
from google import genai
from google.genai import types
from dotenv import load_dotenv
# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")
# 2. Inicializar el Cliente
# Este cliente gestiona la conexión
client = genai.Client(api_key=clave_api)
def ejecutar_consulta():
    print("🚀 Conectando con el motor de Gemini ...")


    #--------->>> ELEMENTOS CLAVE DE LA ANATOMIA DE UN PROMPT <<<-----------------#

    #Tarea
    prompt = f"""Escribe una publicación de blog detallada sobre las ventajas de usar microservicios."""

    #Formato
    #prompt = f"""Genera una lista de 3 lenguajes de programación. FORMATO: Devuelve el resultado exclusivamente en formato JSON con las llaves 'nombre' y 'uso_principal'."""

    #Tema
    #prompt = """Explica el concepto de 'Entropía' aplicado a la teoría de la información."""

    #Tono
    #prompt = """Explica qué es una base de datos.TONO: Escribe como si fueras un pirata del siglo XVIII utilizando jerga náutica."""

    #Contexto
    #prompt = """Explica cómo funciona el protocolo HTTP. CONTEXTO: Tu audiencia son niños de 8 años en una clase de introducción a la tecnología."""

    #Restricción
    #prompt = """Resume el impacto de la revolución industrial. RESTRICCIONES: No uses más de 50 palabras. No menciones a ningún personaje histórico específico."""

    #Condicional
    # texto_entrada = "In recent years, Internet has transformed how we communicate."
    # prompt = f"""Se te proporcionará un texto delimitado por tildes invertidas.
    # SI el texto está escrito en inglés, verifica si contiene la palabra clave 'tec
    # hnology'.
    # SI la contiene, sugiere un título.
    # DE LO CONTRARIO, escribe 'Palabra clave no encontrada'.
    # ```
    # {texto_entrada}
    # ```
    # """

    configuracion = types.GenerateContentConfig(
        temperature=0.7, #Nivel de creatividad en la respuesta
        max_output_tokens=2000 #Limite de tokens en la respuesta
    )

    try:
        # 3. Llamada directa al servicio de modelos
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents= prompt,
            config = configuracion
        )
        print("\n--- Respuesta Recibida ---")
        print(response.text)
        print("--------------------------")
        
    except Exception as e:
        print(f"❌ Ocurrió un error en la conexión: {e}")
    
if __name__ == "__main__":
    ejecutar_consulta()