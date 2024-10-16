# **Documentación de José Ismael Llanos Rosadio**

## **1. Distribución de tareas**

Conforme a las indicaciones del examen parcial, la distribución de tareas fue realizada de forma equitativa. Mi rol fue el de **Miembro 3: Sistema de puntuación y gestión de niveles de dificultad**, y también participé en la implementación de pruebas para validar estas características, tanto en **BDD** como en **TDD**. Los detalles de mis contribuciones se explican en los siguientes puntos.

## **2. Mi rol en el equipo**

Mi principal tarea fue la implementación del **sistema de puntuación** y la **gestión de niveles de dificultad** dentro del juego **Simon Says** durante el **Sprint 3**, que tuvo lugar de manera presencial a partir de la **1 p.m. en la Sala 3 de la UNI**. Además, fui responsable de añadir pruebas unitarias en **pytest** y pruebas basadas en **BDD** con **Behave** para validar estas funcionalidades.

## **3. Aportes realizados**

### **3.1. Sistema de puntuación y niveles de dificultad**

Se implementó un sistema de puntuación que verifica la cantidad de puntos que un jugador puede obtener, desplegándose en dos niveles de dificultad: **fácil** y **difícil**. 

- **Rama:** `feature/Llanos_sistema_puntuacion_dificultad`
- **PR:** [Sistema de puntuación y gestión de niveles de dificultad #26](https://github.com/Renato200419/Examen-Parcial-CC3S2/pull/26)
#### **Cambios en (`routes.py`):**

1. **Inicialización de la puntuación**:
   Agregué la variable `puntuacion` para gestionar los puntos acumulados por el jugador. Esta variable se inicializa en cero cada vez que comienza una nueva partida.

   ```python
   puntuacion = 0
   ```

2. **Validación de secuencias y actualización de puntuación**:
   En la función `validar_secuencia`, añadí la lógica para incrementar la puntuación del jugador si la secuencia ingresada es correcta. La puntuación se actualiza en base a la longitud de la secuencia.

   ```python
   puntuacion += len(secuencia_actual)
   return {"mensaje": "Secuencia correcta, continúa", "puntuacion": puntuacion, "secuencia": secuencia_actual}
   ```

3. **Continuidad del juego**:
   También implementé la función `continuar_juego`, que añade nuevos colores a la secuencia dependiendo de si el jugador acierta y del nivel de dificultad seleccionado. Esto permite que el jugador siga jugando con una secuencia más difícil.

   ```python
   cantidad_colores = 1 if modo_dificultad == "facil" else 2
   nuevos_colores = generador_secuencias.generar_secuencia(cantidad_colores)
   secuencia_actual.extend(nuevos_colores) # Añadir uno o dos colores a la secuencia
   return {"mensaje": f"{cantidad_colores} color(es) añadido(s)", "secuencia": secuencia_actual}
   ```

#### **Cambios en (`console.py`):**
- Modifiqué el constructor de la clase `ConsolaSimonSays` para incluir puntuación y dificultad
   ```python
   def __init__(self, base_url="http://localhost:8000"):
       self.base_url = base_url
       self.secuencia_actual = []  # Almacena la secuencia completa generada
       self.puntuacion = 0
       self.dificultad = "facil"
   ```

- Permití que el jugador pudiera elegir el nivel de dificultad a través de un menú interactivo, donde puede seleccionar entre el nivel "fácil" o "difícil".
   ```python
	def seleccionar_dificultad(self):  
	    """Permite al jugador seleccionar el nivel de dificultad."""  
	    print("Selecciona el nivel de dificultad:")  
	    print("1. Fácil")  
	    print("2. Difícil")  
	    opcion = int(input("Elige un número (1-2): ").strip())  
	    if opcion == 1:  
	        self.dificultad = "facil"  
	    elif opcion == 2:  
	        self.dificultad = "dificil"  
	    else:  
	        print("Opción no válida, elige nuevamente.")  
	        self.seleccionar_dificultad()
   ```

- Modifiqué la función `iniciar_juego` para que inicie el juego con la dificultad seleccionada.
   ```python
		def iniciar_juego(self):  
		    self.seleccionar_dificultad()  
		    response = requests.post(f"{self.base_url}/juego/iniciar", params={"dificultad": self.dificultad})  
		    if response.status_code == 200:  
		        data = response.json()  
		        self.secuencia_actual = data["secuencia"]  
		        self.puntuacion = data["puntuacion"]  
		        print(f"Juego iniciado. Dificultad: {self.dificultad}. Puntuación: {self.puntuacion}.")  
		        print(f"Secuencia: {self.secuencia_actual}")  
		    else:  
		        print("Error al iniciar el juego.")
   ```

- Modifiqué `validar_jugada`para que muestre la puntuación del jugador.
   ```python
       if response.status_code == 200:
           data = response.json()
           self.puntuacion = data["puntuacion"]
           print(f"Secuencia correcta! Puntuación: {self.puntuacion}")
   ```
5. También hice que se imprima la cantidad correcta de colores en `continuar_juego` dependiendo de la dificultad
	```python
	if self.dificultad == "facil" :   
	    print(f"Nuevo color añadido: {self.secuencia_actual[-1]}")  
	else:  
	    print(f"Nuevo color añadido: {self.secuencia_actual[-2:]}")
	```
### **3.3. Pruebas en Behave para validar el sistema de puntuación**

Desarrollé pruebas en **Behave** que validan el comportamiento del sistema desde la perspectiva del usuario.

- **Rama:** `feature/Llanos-bdd-sistema_puntuacion`
- **PR:** [Feature/llanos bdd sistema puntuacion #37](https://github.com/Renato200419/Examen-Parcial-CC3S2/pull/37)
#### **Código en `sistema_validacion.feature`:**
```gherkin
Feature: Validación de puntuación y niveles de dificultad
  Scenario: Validar selección de dificultad fácil
    Given que inicio un nuevo juego
    When selecciono la dificultad "facil"
    Then el sistema genera una secuencia de 1 color y la puntuación inicial es 0

  Scenario: Validar selección de dificultad difícil
    Given que inicio un nuevo juego
    When selecciono la dificultad "dificil"
    Then el sistema genera una secuencia de 2 colores y la puntuación inicial es 0
```
#### **Código en `sistema_validacion_steps.py` **
```python
from behave import *  
import requests  
  
base_url = "http://localhost:8000"  
  
@given('que inicio una nueva partida')  
def step_impl(context):  
    # No se hace nada en este paso  
    pass  
  
@when('selecciono el nivel de dificultad "{dificultad}"')  
def step_impl(context, dificultad):  
    response = requests.post(f"{base_url}/juego/iniciar", params={"dificultad": dificultad})  
    context.response = response  
    assert response.status_code == 200  
  
  
@then('el juego debe generar secuencias de colores acorde al nivel seleccionado "{dificultad}"')  
def step_impl(context, dificultad):  
    response_json = context.response.json()  
    secuencia = response_json["secuencia"]  
  
    if dificultad == "facil":  
        assert len(secuencia) == 1  
    elif dificultad == "dificil":  
        assert len(secuencia) == 2  
    assert "mensaje" in response_json  
  
  
# Segundo escenario  
@given('que he ingresado una secuencia correcta')  
def step_impl(context):  
    # Hacemos la solicitud para iniciar el juego  
    response = requests.post(f"{base_url}/juego/iniciar")  
  
    # Guardamos la secuencia correcta en el contexto  
    context.secuencia_correcta = response.json().get("secuencia")  
  
    # Guardamos la puntuación inicial en el contexto  
    context.puntuacion_inicial = response.json().get("puntuacion")  
  
    print(f"Secuencia correcta: {context.secuencia_correcta}")  
    print(f"Puntuación inicial: {context.puntuacion_inicial}")  
  
    assert response.status_code == 200  
  
  
@when('el sistema va a validar la secuencia')  
def step_impl(context):  
    # Hacemos la solicitud para validar la secuencia correcta  
    context.response = requests.post(f"{base_url}/juego/validar", json=context.secuencia_correcta)  
  
    # Verificamos que la respuesta tenga un status 200  
    assert context.response.status_code == 200  
  
  
@then('mi puntuación debe incrementarse con base en la longitud de la secuencia')  
def step_impl(context):  
    # Obtenemos la nueva puntuación después de la validación  
    puntuacion_nueva = context.response.json().get("puntuacion")  
  
    print(f"Puntuación nueva: {puntuacion_nueva}")  
  
    # Comprobamos que la puntuación nueva sea mayor que la inicial  
    assert puntuacion_nueva > context.puntuacion_inicial  
  
# Tercer escenario  
@given('que he ingresado una nueva secuencia correcta en el nivel {dificultad}')  
def step_impl(context, dificultad):  
    # Iniciamos el juego con dificultad fácil  
    response = requests.post(f"{base_url}/juego/iniciar", params={"dificultad": dificultad})  
  
    # Guardamos la secuencia correcta generada por el juego  
    context.secuencia_correcta = response.json().get("secuencia")  
  
    # Validamos la secuencia correcta que acabamos de obtener  
    context.response = requests.post(f"{base_url}/juego/validar", json=context.secuencia_correcta)  
  
    # Verificamos que la validación fue exitosa  
    assert context.response.status_code == 200  
  
  
@when('solicito continuar el juego')  
def step_impl(context):  
    # Continuamos el juego, añadiendo más colores a la secuencia  
    context.response = requests.post(f"{base_url}/juego/continuar")  
    # Verificamos que la respuesta sea correcta  
    assert context.response.status_code == 200  
  
@then('la secuencia debe aumentar en longitud y contener más colores')  
def step_impl(context):  
    # Obtenemos la secuencia actual después de continuar el juego  
    secuencia_actual = context.response.json().get("secuencia")  
  
    # Verificamos que la longitud de la secuencia actual sea mayor que la secuencia correcta  
    assert len(secuencia_actual) > len(context.secuencia_correcta)
```
### **3.3. Pruebas para validar la dificultad y puntuación**

Implementé pruebas unitarias para validar que el sistema maneje correctamente los niveles de dificultad y la puntuación acumulada por el jugador.

- **Rama:** `feature/Llanos-implementacion_del_test_routes`
- **PR:** [Agregar pruebas para validar el sistema de puntuación y el modo de dificultad en pytest #38](https://github.com/Renato200419/Examen-Parcial-CC3S2/pull/38)

#### **Cambios en (`test_routes.py`):**
He implementado tres pruebas clave para asegurar el correcto funcionamiento del sistema de dificultad y puntuación en el juego:

1. **`test_iniciar_juego_facil`**: Verifica que al iniciar el juego en el nivel "fácil", se genera una secuencia de 1 color. Además, se asegura que el mensaje y la dificultad sean los correctos.
	```python
	def test_iniciar_juego_facil():  
	    response = client.post("/juego/iniciar", params={"dificultad": "facil"})  
	    assert response.status_code == 200  
	    data = response.json()  
	    assert data["mensaje"] == "Nuevo juego iniciado"  
	    assert data["dificultad"] == "facil"  
	    assert len(data["secuencia"]) == 1  # El nivel fácil genera una secuencia de 1 color  
	```
2. **`test_iniciar_juego_dificil`**: Comprueba que al iniciar el juego en el nivel "difícil", la secuencia generada es de 2 colores, y que la respuesta incluya la información correcta sobre la dificultad.
	```python
	def test_iniciar_juego_dificil():  
	    response = client.post("/juego/iniciar", params={"dificultad": "dificil"})  
	    assert response.status_code == 200  
	    data = response.json()  
	    assert data["mensaje"] == "Nuevo juego iniciado"  
	    assert data["dificultad"] == "dificil"  
	    assert len(data["secuencia"]) == 2  # El nivel difícil genera una secuencia de 2 colores  
	```
3. **`test_puntuacion_dificil`**: Inicia el juego en modo difícil, valida una secuencia correcta y verifica que la puntuación obtenida sea mayor que cero. Esto asegura que el sistema de puntuación funciona adecuadamente.
	```python
	def test_puntuacion_dificil():  
	    # Iniciar el juego en modo difícil  
	    response = client.post("/juego/iniciar", params={"dificultad": "dificil"})  
	    assert response.status_code == 200  
	    secuencia = response.json()["secuencia"]  
	  
	    # Validar la secuencia correcta  
	    response = client.post("/juego/validar", json=secuencia)  
	    assert response.status_code == 200  
	    puntuacion = response.json()["puntuacion"]  
	  
	    # Verificar que la puntuación sea mayor que cero  
	    assert puntuacion > 0
	```


## **4. Retos y desafíos enfrentados**
Uno de los principales retos a los que me enfrenté fue la correcta integración del sistema de puntuación con los diferentes niveles de dificultad. Asegurar que la puntuación se incrementara adecuadamente según la longitud de las secuencias en el modo fácil y difícil requirió realizar múltiples intentos probando los endpoints con la consola, lo que implicó modificar varias partes del código.

Otro desafío fue la implementación de **BDD (Behavior Driven Development)**. Aunque comprendía los conceptos, me resultó complicado escribir correctamente los escenarios de prueba en **Behave** para validar el sistema de puntuación y los niveles de dificultad. La interacción entre las pruebas y las funcionalidades del juego requirió varios intentos para que los tests reflejaran correctamente el comportamiento esperado.

## **5. Conclusiones**

Durante el horario del examen parcial (de 1 a 4 p.m.), logré realizar todas las modificaciones necesarias en `routes.py` y `console.py`, asegurando que nuestro grupo tuviera el juego completamente funcional y cumpliendo con todos los requisitos del examen dentro de ese plazo. Sin embargo, fue necesario emplear tiempo adicional después para completar las pruebas **BDD** y **TDD**, así como la documentación final.