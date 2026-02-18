#Ejercicio:
#Desarrolle una función llamada procesar_articulo(texto, tarea) que reciba un texto largo y una tarea.
#   -Si la tarea es "resumir", debe devolver un resumen ejecutivo.
#   -Si la tarea es "profesionalizar", debe editar el texto para que suene formal y técnico.
# Restricción: Debe usar una system_instruction que defina a la IA como un "Editor Editorial de prestigio".

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()  # Cargar las variables de entorno desde el archivo .env
API_KEY = os.getenv("GENAI_API_KEY")

# Inicializar el cliente de GenAI
client = genai.Client(api_key=API_KEY)

# Configuración de la tarea y el sistema
configuration = types.GenerateContentConfig(
    max_output_tokens=2048,
    system_instruction="""Eres un editor de texto de una Editorial de prestigio especializado en resumir y profesionalizar textos. 
    Recibirás una instrucción del siguiente tipo: "Tarea = (resumir o profesionalizar), Texto = ..." debes editar el texto entregado en base a la tarea asignada.
    Si te piden una tarea que no esté relacionada con la edición de texto, responde 'Lo siento, solo soy un editor de texto profesional, no puedo realizar la tarea que solicitas'."""
)

def procesar_articulo(texto, tarea):
    prompt = "Tarea = " + tarea + ", Texto = " + texto
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents= prompt,
            config = configuration
        )
        print("\n--- Respuesta Recibida ---")
        print(response.text)
        print("--------------------------")
        
    except Exception as e:
        print(f"❌ Ocurrió un error en la conexión: {e}")


print("--- Chat con Editor de textos profesional ---")
print("Asistente: ¡Hola! Soy un editor de texto profesional de una prestigiosa editorial. Te ayudaré a resumir y profesionalizar tus escritos.")


print("Asistente: Digita el número de opción de la tarea que deseas que realice por ti:.\n1. Resumir\n2. Profesionalizar")
user_input = input("Usuario: ")
tarea = ""
if user_input == "1":
    tarea = "resumir (hacer resumen ejecutivo)"
elif user_input == "2":
    tarea = "profesionalizar"
else:
    print("Opción no válida, ejecute e inténtalo de nuevo.")
    

    
# Procesar el artículo con la tarea elegida
if tarea:
    print("Asistente: Ahora copia y pega el texto aquí.")
    texto = input("Usuario: ")
    print("Editando texto...✍️")
    procesar_articulo(texto, tarea)
