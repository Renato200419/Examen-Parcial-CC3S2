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

