# En esta documentación se subirá todo lo realizado por el alumno: Renato Steven Olivera Calderón

# Índice:
 - [1. Contrucción del Kanban Board](#kanban-board)
 - [2. Implementación Generación de las Secuencias](#implementación-generación-de-las-secuencias)
 - [3. Lógica del Juego](#lógica-de-inicio-de-juego)
 - [4. Pruebas BDD para la generación de secuencias en el Juego](#pruebas-bdd-para-la-generación-de-secuencias-en-el-juego-simon-says)
 - [5. Pruebas unitarias para generar_secuencia con pytest](#pruebas-unitarias-para-generar_secuencia-con-pytest)
 - [6. Métricas con Prometheus y Grafana](#métricas-con-prometheus-y-grafana)
# Kanban Board
Un Kanban Board es una herramienta visual utilizada para gestionar y mejorar el flujo de trabajo en proyectos. Se divide en columnas que representan diferentes etapas del proceso (como "Por hacer", "En progreso" y "Hecho"). Las tareas se mueven entre columnas a medida que avanzan, lo que permite visualizar fácilmente el estado del proyecto y gestionar el trabajo de manera eficiente.

## Pasos para crear el Kanban Board
1. En la sección de `Projects` se crea el Kanban Board la cual se nombró: `Desarrollo del Juego de Memoria - Simon Says`

![Kanban](Imagenes-documentacion-Olivera/Foto1.png)

Luego de crearlo, se divide por columnas:
- **Product Backlog**: Contiene todas las tareas pendientes y no priorizadas del producto, es decir es el repositorio de trabajo por hacer que aún no ha sido planificado en un sprint.
- **Sprint Backlogs**: Lista de tareas seleccionadas para ser completadas en el sprint actua
- **En progreso**: Tareas en las que el equipo está trabajando activamente.
- **En revisión**: Indica que hay pull requests abiertas que están siendo revisadas
- **Hecho**: Significa que las pull requests ya han sido revisadas y mergeadas a la rama (`develop`)

![Kanban](Imagenes-documentacion-Olivera/Foto2.png)

2. Luego creamos el **template para las historias de usuario**.
- Para realizarlo nos dirigimos a `Settings` de nuestro repositorio y seleccionamos `Set up templates`.

![Template](Imagenes-documentacion-Olivera/temp1.png)

- Luegi añadimos el template.

![Template](Imagenes-documentacion-Olivera/temp2.png)

- Seleccionamos como opción `Custom template`.

![Template](Imagenes-documentacion-Olivera/temp3.png)

- Hacemos clic en `Preview and edit`.

![Template](Imagenes-documentacion-Olivera/temp4.png)

- Luego damos clic en el `lapicito`.

![Template](Imagenes-documentacion-Olivera/temp5.png)

- Luego rellenamos los tres campos.

![Template](Imagenes-documentacion-Olivera/temp6.png)

- Una vez rellenado de la siguiente manera:

![Template](Imagenes-documentacion-Olivera/temp7.png)

- Damos clic en `Propose changes`

![Template](Imagenes-documentacion-Olivera/temp8.png)

- Realizamos el commit 

![Template](Imagenes-documentacion-Olivera/temp9.png)

- En nuestra carpeta `.github` vemos que se ha creado una carpeta llamada `ISSUE_TEMPLATE` en la cual se guardan todos los templates.

![Template](Imagenes-documentacion-Olivera/temp10.png)

- Al entrar a la carpeta tenemos nuestro template para las historias de usuario.

![Template](Imagenes-documentacion-Olivera/temp11.png)

3. Una vez hecho el **template de las historias de usuario**, realizamos las historias de usuario.

- Las historias de usuario describen funcionalidades desde el punto de vista del usuario y expresan lo que el sistema debe hacer de manera sencilla y clara.

- Tenemos como ejemplo a la historia de usuario `Crear la estructura básica del proyecto`.

```md
**Como** desarrollador,  
**Quiero** crear la estructura básica del proyecto,  
**Para** organizar correctamente los archivos y directorios para un desarrollo escalable.

### Descripción:
El proyecto debe tener una estructura inicial que incluya carpetas para la aplicación principal (`app/`) y para las pruebas (`tests/`). Esta estructura debe permitir que el proyecto crezca sin complicaciones.

### Criterios de aceptación:
**Funcionalidad**: Estructura básica del proyecto

**Escenario**: Estructura creada exitosamente

- **Dado** que inicio el proyecto,
- **Cuando** creo la estructura de carpetas,
- **Entonces** las carpetas `app/` y `tests/` deben existir y estar correctamente organizadas.

**Escenario**: Organización del código

- **Dado** que quiero que el código esté bien estructurado,
- **Cuando** creo los archivos principales (`main.py` y `test_routes.py`),
- **Entonces** deben estar en las ubicaciones correctas dentro de `app/` y `tests/`.

### Tareas:
- [X] Crear la carpeta `app/` para la lógica de la aplicación.
- [X] Crear la carpeta `tests/` para las pruebas unitarias.
- [X] Crear el archivo `main.py` en `app/` para inicializar la aplicación.
- [X] Crear el archivo `test_routes.py` en `tests/` para pruebas unitarias.
- [X] Confirmar que la estructura permita la escalabilidad del proyecto.
```
![Historia de usuario](Imagenes-documentacion-Olivera/h1.png)

Vista de la historia de usuario:
- **Asignaciones**: Se observa que los desarrolladores asignados a esta historia de usuario son Renato200419 (Olivera) y al-2100 (Barriga).





- **Label (Etiqueta)**: Se ha etiquetado como enhancement, lo que indica que esta PR corresponde a una mejora o incremento en las funcionalidades del proyecto, en este caso, la organización de la estructura.

- **Prioridad**: La prioridad está marcada como Alta, lo que sugiere que esta tarea es crítica para el desarrollo del proyecto, probablemente porque una buena estructura es esencial para el progreso posterior.

- **Estimación**: La estimación es de 3, lo que usualmente se refiere a una escala de esfuerzo, como story points. Esto indica una complejidad moderada en la tarea.

- **Sprint**: Está asignado al Sprint 1, que comenzó el 14 de octubre. Esto significa que se esperaba que la tarea se completara en el primer sprint, cumpliendo un objetivo clave en las primeras fases del desarrollo.

- **Pull Request**: La historia está ligada directamente a la PR, lo que facilita el seguimiento del progreso. En este caso, la historia de usuario describe la necesidad de crear la estructura básica del proyecto, y la PR #1 implementa esos cambios.

![Historia de usuario](Imagenes-documentacion-Olivera/h2.png)

4. **Planificación de los Sprints**
Para la planificación se dividió en 3 sprints por día.

- ***Sprint 1***: Creación de la estructura básica del proyecto (el cascarón).
   - **Crear la estructura básica del proyecto**: Se estableció la estructura inicial del proyecto con las carpetas principales (`app/`, `tests/`), permitiendo un desarrollo escalable.
   - **Configurar Docker Compose**: Se añadió la configuración para facilitar el manejo de contenedores.
   - **Configurar Prometheus para monitoreo básico**: Se integró Prometheus para monitorear métricas básicas del proyecto.
   - **Configurar pipeline de CI/CD**: Se implementó un pipeline automatizado para la integración y entrega continua del proyecto.
   - **Crear Dockerfile para el proyecto**: Se creó el Dockerfile para contenedorización, lo cual permite ejecutar la aplicación en un entorno controlado.

- ***Sprint 2***: Implementación de las tareas del miembro 1 y 2, junto con pruebas BDD y TDD.
    - **Generar secuencia aleatoria de colores**: Se implementó la funcionalidad para generar secuencias aleatorias en el juego junto con su prueba BDD.
   - **Validar secuencia ingresada por el jugador**: Se añadió la lógica que valida si la secuencia ingresada por el jugador es correcta. Además, se agregó su prueba BDD.
   - **Implementar y probar la generación y validación de secuencias**: Se realizaron las pruebas unitarias para asegurar que la generación y validación de secuencias funcionan correctamente.
   - **Implementar la consola del juego Simon Says**: Se creó la consola donde el jugador interactúa con el juego.

- ***Sprint 3***: Refactorización del código, documentación del proyecto, test adicionales, dashboards de Grafana, métricas de Prometheus y tarea del miembro 3, con pruebas BDD y TDD.


5. **Progreso del proyecto**
- Inicio del Sprint 1
![Kanban](Imagenes-documentacion-Olivera/Foto3.png)
![Kanban](Imagenes-documentacion-Olivera/Foto4.png)
![Kanban](Imagenes-documentacion-Olivera/Foto5.png)

6. Creación del `Burndown Chart`

    **Burndown Chart** es una representación gráfica utilizada en metodologías ágiles para mostrar
    la cantidad de trabajo pendiente a lo largo del tiempo en un sprint o proyecto. Mide el progreso
    del equipo visualizando el trabajo completado y el trabajo restante
    - El eje x representa la línea de tiempo (días, sprints, etc.),
    - El eje y muestra la cantidad de trabajo restante (a menudo medido en story points, tareas u
    horas)

    **Para el Sprint 1**
![Kanban](Imagenes-documentacion-Olivera/Foto6.png)
![Kanban](Imagenes-documentacion-Olivera/Foto7.png)

- **Inicio del Sprint 2**
![Kanban](Imagenes-documentacion-Olivera/Foto8.png)
![Kanban](Imagenes-documentacion-Olivera/Foto9.png)
![Kanban](Imagenes-documentacion-Olivera/Foto10.png)

- **Finalización del Sprint 2**

    ![Kanban](Imagenes-documentacion-Olivera/Foto11.png)


    ![Kanban](Imagenes-documentacion-Olivera/Foto12.png)

- 










# Implementación Generación de las Secuencias
Para poder realizarlo creamos un archivo `sequence.py` en `app` en el que 

```python
import random

class GeneradorSecuencias:
    def __init__(self, colores=None):
        if colores is None:
            self.colores = ['rojo', 'verde', 'azul', 'amarillo']  # Colores por defecto
        else:
            self.colores = colores
        self.secuencia = []

    def generar_secuencia(self, longitud=1):
        """Genera una secuencia aleatoria de colores."""
        self.secuencia = random.choices(self.colores, k=longitud)
        return self.secuencia
```
# Lógica de inicio de juego
En `routes.py` agregamos el endpoint para iniciar el juego:

```python
from fastapi import APIRouter
from app.sequence import GeneradorSecuencias

# Crear el enrutador de FastAPI
router = APIRouter()

# Inicializar el generador de secuencias
generador_secuencias = GeneradorSecuencias()
secuencia_actual = []

# Rutas de la API

# Ruta principal
@router.get("/")
def root():
    return {"message": "Aplicación para Simon Says"}

# Ruta de verificación de salud
@router.get("/health")
def health_check():
    return {"status": "healthy"}

@router.post("/juego/iniciar")
def iniciar_juego():
    """Inicia un nuevo juego generando una secuencia de un solo color."""
    global secuencia_actual
    secuencia_actual = generador_secuencias.generar_secuencia()
    return {"mensaje": "Nuevo juego iniciado", "secuencia": secuencia_actual}
```

# Pruebas BDD para la generación de secuencias en el Juego: Simon Says

Para poder realizarlo se crea la carpeta `features` en el tendremos los archivos `.feature` y una carpeta `steps` para guardar los archivos `.py` en el cual se implementarán los pasos para los escenarios de prueba en Gherkin.

- Escenarios de prueba:

    ```gherkin
    Feature: Generación de secuencias aleatorias de colores

    Scenario: Generación exitosa de una secuencia de un solo color
        Given que inicio un nuevo juego
        When solicito la generación de una nueva secuencia
        Then el sistema genera una secuencia de un color aleatorio

    Scenario: Aumento de la secuencia con cada nivel
        Given que he superado un nivel del juego
        When solicito una nueva secuencia
        Then la secuencia aumenta en longitud y contiene más colores
    ```
- `generar_secuencia_steps.py` 
    ```python
    from behave import *
    from app.sequence import GeneradorSecuencias

    # Contexto compartido
    @given('que inicio un nuevo juego')
    def step_iniciar_nuevo_juego(context):
        context.generador = GeneradorSecuencias()
        context.secuencia_actual = context.generador.generar_secuencia()
        
    @when('solicito la generación de una nueva secuencia')
    def step_generar_secuencia(context):
        context.secuencia_nueva = context.generador.generar_secuencia()

    @then('el sistema genera una secuencia de un color aleatorio')
    def step_verificar_secuencia(context):
        assert len(context.secuencia_nueva) == 1, "La secuencia generada debe tener una longitud de 1"
        assert context.secuencia_nueva[0] in context.generador.colores, "El color debe ser uno de los permitidos"

    # Para el segundo escenario
    @given('que he superado un nivel del juego')
    def step_superar_nivel(context):
        context.generador = GeneradorSecuencias()
        context.secuencia_actual = context.generador.generar_secuencia(longitud=1)  # Inicialmente de longitud 1
        context.nivel = 2  # El nivel actual es mayor a 1

    @when('solicito una nueva secuencia')
    def step_generar_secuencia_larga(context):
        context.secuencia_nueva = context.generador.generar_secuencia(longitud=context.nivel)

    @then('la secuencia aumenta en longitud y contiene más colores')
    def step_verificar_secuencia_larga(context):
        assert len(context.secuencia_nueva) == context.nivel, f"La secuencia generada debe tener una longitud de {context.nivel}"
        for color in context.secuencia_nueva:
            assert color in context.generador.colores, "Todos los colores de la secuencia deben ser válidos"
    ```
- **Resultado ejecutando behave**

![Resultado-Behave](Imagenes-documentacion-Olivera/behave.png)


# Pruebas unitarias para generar_secuencia con pytest 
Creamos la carpeta `tests` para guardar todas las pruebas unitarias.

En este caso realizamos la prueba unitaria para `generar_secuencia`. 
```python
import pytest
from app.sequence import GeneradorSecuencias


# Prueba para verificar que se genera una secuencia de un solo color
def test_generar_secuencia_un_color():
    generador = GeneradorSecuencias()
    secuencia = generador.generar_secuencia(longitud=1)

    assert len(secuencia) == 1, "La secuencia debería tener una longitud de 1"
    assert secuencia[0] in generador.colores, "El color generado debería ser uno de los colores permitidos"


# Prueba para verificar que se genera una secuencia con múltiples colores
def test_generar_secuencia_multiple_colores():
    generador = GeneradorSecuencias()
    secuencia = generador.generar_secuencia(longitud=3)

    assert len(secuencia) == 3, "La secuencia debería tener una longitud de 3"
    for color in secuencia:
        assert color in generador.colores, "Cada color generado debería ser uno de los colores permitidos"


# Prueba para verificar que se genera una secuencia usando un conjunto de colores personalizado
def test_generar_secuencia_colores_personalizados():
    colores_personalizados = ['morado', 'naranja', 'rosado']
    generador = GeneradorSecuencias(colores=colores_personalizados)
    secuencia = generador.generar_secuencia(longitud=2)

    assert len(secuencia) == 2, "La secuencia debería tener una longitud de 2"
    for color in secuencia:
        assert color in colores_personalizados, "El color generado debería ser uno de los colores personalizados"
```

- **Resultado de la prueba unitaria**

![Resultado-test](Imagenes-documentacion-Olivera/test.png)

# **Métricas con Prometheus y Grafana**

Se implementaron dos métricas:
- `latencia_histogram` 
- `juegos_iniciados`

Se realizaron cambios en `main.py`

```python
from fastapi import FastAPI
from app.routes import router as app_router
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn
app = FastAPI()

# Instrumentar la aplicación y exponer las métricas
instrumentator=Instrumentator()
instrumentator.instrument(app).expose(app)

# Incluir las rutas
app.include_router(app_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
De igual manera realizamos cambios en `routes.py` 

```python
from fastapi import APIRouter, HTTPException
from app.sequence import GeneradorSecuencias
from app.validation import ValidadorSecuencias
from prometheus_client import Counter, Histogram
# Crear el enrutador de FastAPI
router = APIRouter()

# Inicializar el generador de secuencias
generador_secuencias = GeneradorSecuencias()
secuencia_actual = []
puntuacion = 0
modo_dificultad= "facil" # Por defecto, el modo es fácil

# Métricas de Prometheus
latencia_histogram = Histogram("latencia_api", "Latencia de la API en segundos")
juegos_iniciados = Counter("juegos_iniciados", "Número de juegos iniciados")

# Rutas de la API

# Ruta principal
@router.get("/")
def root():
    return {"message": "Aplicación para Simon Says"}

# Ruta de verificación de salud
@router.get("/health")
def health_check():
    return {"status": "healthy"}

@router.post("/juego/iniciar")
def iniciar_juego(dificultad: str = "facil"):
    """Inicia un nuevo juego generando una secuencia de un solo color."""
    global secuencia_actual, puntuacion, modo_dificultad
    secuencia_actual = generador_secuencias.generar_secuencia(1 if dificultad == "facil" else 2)
    juegos_iniciados.inc()  # Incrementar el contador de juegos iniciados
    puntuacion = 0 # Esto reinicia la aplicacion 
    modo_dificultad = dificultad # Establece el modo de dificultad
    return {"mensaje": "Nuevo juego iniciado", "secuencia": secuencia_actual, "puntuacion": puntuacion,"dificultad": modo_dificultad}

@router.post("/juego/validar")
@latencia_histogram.time()
def validar_secuencia(secuencia_jugador: list[str]):
    """Válida la secuencia del jugador"""
    global secuencia_actual, puntuacion
    validador = ValidadorSecuencias(secuencia_actual)
    es_valida = validador.validar_secuencia(secuencia_jugador)
    if not es_valida:
        raise HTTPException(status_code=400, detail="Secuencia incorrecta. Juego terminado.")
    # Actualizar puntuación si la secuencia es correcta
    puntuacion += len(secuencia_actual)
    return {"mensaje": "Secuencia correcta, continúa", "puntuacion": puntuacion, "secuencia": secuencia_actual}

@router.post("/juego/continuar")
def continuar_juego():
    """Añade un nuevo color a la secuencia si el jugador ha acertado"""
    global secuencia_actual, modo_dificultad
    cantidad_colores = 1 if modo_dificultad == "facil" else 2
    nuevos_colores = generador_secuencias.generar_secuencia(cantidad_colores)
    secuencia_actual.extend(nuevos_colores)  # Añadir uno o dos colores a la secuencia
    return {"mensaje": f"{cantidad_colores} color(es) añadido(s)", "secuencia": secuencia_actual}

```
Ingresamos a Grafana, pero antes de eso no olvidar levantar `docker-compose`
- Comando: `docker-compose --build -d`
Una vez dentro de Grafana
![Grafana](Imagenes-documentacion-Olivera/graf1.png)
- Nos dirigimos a `Data sources` para configurarlo.
![DataSource](Imagenes-documentacion-Olivera/graf2.png)

- Configuración de la primera métrica `latencia_histogram`. 
![1° metrica](Imagenes-documentacion-Olivera/graf4.png)

- Configuración de la segunda métrica `juegos_iniciados`.
![2° metrica](Imagenes-documentacion-Olivera/graf3.png)
- **Previa del Resultado**
![Previa](Imagenes-documentacion-Olivera/graf5.png)

- **Resultado**

![Resultado](Imagenes-documentacion-Olivera/metrics.png)