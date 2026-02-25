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

    #Ensayo de 145 palabras
    #texto= """En un mundo cada vez más interconectado, la empatía se ha convertido en una herramienta esencial para el entendimiento y la convivencia entre personas de diferentes culturas, creencias y orígenes. La empatía nos permite ponernos en el lugar del otro, comprender sus emociones y puntos de vista, y responder de manera más humana y respetuosa. A nivel interpersonal, fomenta relaciones más profundas y saludables, ya que permite una comunicación más abierta y menos conflictiva. En el ámbito global, la empatía es crucial para resolver problemas colectivos, como los conflictos bélicos o las crisis migratorias, donde la indiferencia solo perpetúa la división. Si bien no es una habilidad innata, la empatía puede cultivarse mediante la reflexión y el contacto directo con personas de diferentes contextos. De esta forma, la empatía no solo enriquece la vida individual, sino que también puede transformar positivamente a toda la sociedad. """

    #Ensayo de 87 palabras
    #texto= """El arte desempeña un papel crucial en el desarrollo integral de los estudiantes, pues fomenta la creatividad, la expresión personal y la resolución de problemas. A través de la pintura, la música o la danza, los estudiantes aprenden a pensar de manera crítica y a experimentar el mundo desde diferentes perspectivas. Además, el arte les ayuda a comprender mejor su entorno emocional y cultural, mientras les ofrece una salida para explorar su identidad. Integrar el arte en la educación es esencial para formar individuos completos y empáticos."""
    
    #Ensayo de 100 palabras
    texto= """La tecnología ha transformado profundamente nuestras relaciones personales, estp facilitando la comunicación instantánea a través de redes sociales y aplicaciones de mensajería. Sin embargo, este avance también ha traído consigo el distanciamiento emocional y la superficialidad en muchas interacciones. Si bien las plataformas digitales permiten mantener el contacto a larga distancia, han reducido la calidad de las conversaciones cara a cara, esenciales y muy importantes para el desarrollo de vínculos genuinos teniendo en cuenta su nivel de acercamiento. Es fundamental encontrar un equilibrio, utilizando la tecnología para acercarnos, pero sin olvidar la importancia de las conexiones humanas profundas y auténticas."""

    
    prompt= f"""Eres un evaluador académico de ensayos. Se te proporcionará un ensayo corto, este texto estará delimitado por '"'
                SI el ensayo tiene menos de 100 palabras: Debes responder "El texto proporcionado es muy corto para considerarse como un ensayo, por favor ingresa un nuevo ensayo con minimo 100 palabras.
                SI el ensayo tiene 100 o más de 100 palabras: Debes evaluarlo en una escala de 0 a 50, bajo los criterios de: Ortografía, Coherencia y Argumentación.
                La respuesta debe ser un objeto JSON que contenga cantidad de palabras, nota_final y comentarios.
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