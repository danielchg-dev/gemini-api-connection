# gemini-api-connection
Este proyecto contiene una implementación base para interactuar con los modelos de Inteligencia Artificial de Google utilizando el nuevo SDK de segunda generación (`google-genai`).

## 🛠️ Requisitos Previos

Antes de comenzar, asegúrate de tener:
* Instalado **Python 3.10 o superior**
* Una **API Key** de Google AI Studio. Puedes obtenerla en [aistudio.google.com](https://aistudio.google.com/).

## 🚀 Configuración del Entorno

Sigue estos pasos para ejecutar el código en tu máquina local:

### 1. Clonar el repositorio
### 2. Abrir una terminal (en VS Code: ctrl + ñ)
### 3. Crear y activar un entorno virtual
En Windows:

```bash
python -m venv venv
```
```bash
.\venv\Scripts\activate
```
En macOS/Linux:
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 5. Configurar variables de entorno
Crea un archivo llamado .env en la raíz del proyecto y añade tu API Key Google AI Studio de la siguiente manera:
```bash
GEMINI_API_KEY=tu_clave_secreta_aqui
```
## 💻 Uso
Para ejecutar el script principal de conexión:

```bash
python .\app_gemini.py
```
## 🗒️ Anotaciones EXTRA
*  **Para crear o actualizar el `requirements.txt`:** Ejecuta este comando en tu terminal (con el entorno activado) para que el archivo de texto se genere automáticamente:
    ```bash
    pip freeze > requirements.txt
    ```
## ✅ Ejemplo de ejecución
<img width="1920" height="1140" alt="Captura de pantalla 2026-02-03 214652" src="https://github.com/user-attachments/assets/4af36106-bb8d-4949-b97d-e9f33ab1492e" />
