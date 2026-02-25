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


    texto= """ Hola, mi factura #4502 tiene un cargo doble que no reconozco. Ayuda. """

    prompt= f"""Eres un asistente de triaje de correos electrónicos de soporte. Se te proporcionará un texto delimitado por '"'
                SI el texto contiene una queja sobre un pago o factura: Clasifícalo como "URGENTE-FINANZAS". Extrae el número de factura si existe.
                SI NO, si el texto es una duda técnica general: Clasifícalo como "SOPORTE-ESTÁNDAR". Responde: "Gracias, un técnico lo revisará".
                SI NO es ninguna de las anteriores: Responde simplemente: "Categoría no identificada".
                Texto: "{texto}" """
    
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