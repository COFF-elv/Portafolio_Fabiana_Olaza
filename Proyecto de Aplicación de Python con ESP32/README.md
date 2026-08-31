# Sistema Interactivo con Python, ESP32 y FastAPI
Proyecto final de la Especialización en Desarrollo de Aplicaciones Web con Python en el Instituto de Tecnologías de la información y la Comunicación de Barcelona (2026).

## Descripción
Desarrollé un sistema completo(backend y frontend) usando tecnología como placas de ESP32, sensores, matrices, leds, entre otros. 

La idea principal en términos simples es crear un sistema capaz de reconocer el tipo de ambiente en el que se encuentra un evento, tener dos cargos importantes(control y común) que en equipo funcionen como uno solo y se consiga el objetivo, se acumulan valores para llegar a un valor impuesto como meta por la persona en control y con ello la flor servo simule el florecimiento y las luces led reaccionen acompañando este proceso. 

## Funcionamiento
Este sistema monitoriza en tiempo real el nivel de audio percibido por el sensor de sonido, hace la calibración de sonido siendo 0 la mínima y la máxima 100, luego hace POST de la misma a la API y esta la almacena en un DB que registra la entrada y el valor recibido. 

Después la API clasifica este valor en un estado siendo cuatro [chill(25), flow(50), rush(75), euphoria(100)], dependiendo en que estado se perciba en el ambiente los leds y matriz tendrán presentaciones y juegos de luces diferentes, cada estado cambia de color y la matriz que simula los latidos de un corazón aumentan.  

Asimismo se hace uso de Streamlit que funcionará como web con login para la parte de control y la de acceso común, dónde gracias a la API se podrán obtener los valores en tiempo real siendo medidos y mostrados en gráficas y al mismo tiempo la persona en control se encarga de poner el límite para llegar a la meta.

## Características Principales
- Captación de niveles de audio con sensor conectado a ESP32 y filtrado de señal(EMA)
- Backend con FastAPI + SQLAlchemy + SQLite
- Dashboard en tiempo real con Streamlit(login, visualización y control)
- Comunicación hardware-software mediante peticiones HTTP
- Control de actuadores (matriz LED MAX7219 y flor servo)
  
## Tecnologías utilizadas
- **Hardware:** ESP32, sensor de sonido MAX9814, matriz LED MAX7219, microservo SG90
- **Backend:** Python, FastAPI, SQLAlchemy, SQLite
- **Frontend:** Streamlit, Plotly, Pandas
- **Comunicación:** HTTP/REST

## Estructura del proyecto
- "esp32_post" -> Lectura del sensor, transformación de lectura y envío de datos
- "esp32_get" -> Recepción de datos y control de actuadores
- "api_app" -> Backend FastAPI
- "streamlit_app" -> Dashboard Interactivo

