# Sistema Interactivo con Python, ESP32 y FastAPI
Proyecto final de la Especialización en Desarrollo de Aplicaciones Web con Python en el Instituto de Tecnologías de la información y la Comunicación de Barcelona (2026).

## Descripción
Diseñé y desarrollé completo un sistema(backend y fronted) usando tecnología como placas de ESP32, sensores, matrices, leds, entre otros.
Este sistema monitoriza en tiempo real el nivel de audio percibido por el sensor de sonido, luego la señal la transforma en una escala de 0-100 

## Características Principales
- Captación de niveles de audio con sensor conectado a ESP32 y filtrado de señal(EMA)
- Backend con FastAPI + SQLAlchemy + SQLite
- Dashboard en tiempo real con Streamlit(login, visualización y control)
- Comunicación hardware-software mediante peticiones HTTP
- Control de actuadores (matriz LED MAX7219 y flor servo)
  
## Tecnologías utilizadas
- **Hardware:** ESP32, sensor de sonido MAX9814, matriz LED MAX7219, microservo SG90
- **Backend:** Python, FastAPI, SQLAlchemy, SQLite
- **Fronted:** Streamlit, Plotly, Pandas
- **Comunicación:** HTTP/REST

## Estructura del proyecto
- "esp32_post" -> Lectura del sensor, transformación de lectura y envío de datos
- "esp32_get" -> Recepción de datos y control de actuadores
- "api_app" -> Backend FastAPI
- "streamlit_app" -> Dashboard Interactivo

