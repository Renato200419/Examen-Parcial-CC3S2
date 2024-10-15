# Juego de memoria "Simon Says"

## Descripción del Proyecto

El juego de memoria "Simon Says" es un proyecto desarrollado en Python que simula el juego de memoria clásico en el que los jugadores deben recordar y repetir una secuencia de colores.

## Características Principales

- **API REST**: Implementada con FastAPI.
- **Cliente de Consola (`app/console.py`)**: Interfaz de consola para interactuar con el juego.
- **Monitoreo en Tiempo Real**: Configuración de Prometheus y Grafana para visualizar métricas y estadísticas del juego.
- **DevSecOps Integrado**: Automatización de pruebas, auditoría de seguridad y análisis CI/CD.

## Guía de Instalación y Uso

### Requisitos Previos

- Docker y Docker Compose instalados en el sistema.
- Python 3.9 o superior instalado en el sistema para ejecutar la consola del juego.

### Instalación

1. Clona el repositorio del proyecto:
    ```bash
    git clone https://github.com/Renato200419/Examen-Parcial-CC3S2.git
    cd Examen-Parcial-CC3S2
    ```

2. Construye y levanta los servicios utilizando Docker Compose:
    ```bash
    docker-compose up --build -d
    ```
### Como iniciar el juego

1. Crea el entorno virtual

   ```bash
   python3 -m venv venv
   ```
2. Activa el entorno virtual

   ```bash
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```
3. Instala las dependencias necesarias

   ```
   pip install -r requirements.txt
   ```

4. Accede a la consola del juego
   ```bash
   python app/console.py
   ```
### Cómo Iniciar el Juego

Una vez que accedes a la consola (`app/console.py`), sigue las instrucciones en pantalla para interactuar con el juego. A continuación se detalla el flujo de juego:
1. Selecciona el nivel de dificultad (fácil o difícil).
```bash
Selecciona el nivel de dificultad:
1. Fácil
2. Difícil
Elige un número (1-2): 1
Juego iniciado. Dificultad: facil. Puntuación: 0.
```
2. El juego generará colores aleatorios.
```bash
Secuencia: ['rojo']
Selecciona el color correspondiente:
1. Rojo
2. Verde
3. Azul
4. Amarillo
```

3. Repite la secuencia ingresando los colores en el orden correcto.
```bash
Elige un número (1-4): 1
¡Secuencia correcta! Puntuación: 1.
Nuevo color añadido: amarillo
```

4. Continúa repitiendo la secuencia hasta que cometas un error.
```bash
Selecciona el color correspondiente:
1. Rojo
2. Verde
3. Azul
4. Amarillo
Elige un número (1-4): 1
Selecciona el color correspondiente:
1. Rojo
2. Verde
3. Azul
4. Amarillo
Elige un número (1-4): 4
¡Secuencia correcta! Puntuación: 3.
Nuevo color añadido: azul
```

### Monitorización del Juego

Para monitorear las métricas del juego:

1. Accede a la interfaz de Grafana en `http://localhost:3000`.
2. Configura el Data Source en Grafana:
   - En la barra lateral, selecciona Configuration y luego Data Sources.
   - Crea un nuevo Data Source para Prometheus y establece la URL en http://prometheus:9090. 
   - Guarda la configuración.
3. Importa el dashboard desde la carpeta dashboards/ del proyecto:
   - En Grafana, selecciona la opción Import en la barra lateral.
   - Carga el archivo JSON de la carpeta dashboards/ que contiene la configuración del dashboard.
4. Una vez importado y configurado el Data Source, podrás ver las métricas.

## Estructura del Proyecto

- **`app/`**: Implementación de la API REST y lógica del juego.
- **`app/console.py`**: Cliente de consola para interactuar con el juego.
- **`Dockerfile`**: Define la imagen Docker para la aplicación.
- **`docker-compose.yml`**: Archivo de configuración para Docker Compose.
- **`prometheus.yml`**: Configuración de Prometheus para la recolección de métricas.
- **`Dashboard/`**: Carpeta que contiene el archivo JSON del dashboard de Grafana.
- **`features/`**: Carpeta que contiene las historias de usuario y escenarios de prueba.
- **`features/steps/`**: Implementación de los pasos de los escenarios de prueba.
- **`tests/`**: Pruebas unitarias y de integración para asegurar el correcto funcionamiento de la aplicación.
- **`requirements.txt`**: Lista de dependencias de Python para el proyecto.


## Integrantes del Proyecto
- Jorge Alonso Barriga Morales
- Renato Steven Olivera Calderón
- José Ismael Llanos Rosadio

## Contribuciones

Si deseas contribuir a este proyecto:

1. Realiza un fork del repositorio.
2. Crea una nueva rama con las mejoras o correcciones (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza un Pull Request explicando tus cambios.
