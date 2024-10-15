from behave import *
import requests

base_url = "http://localhost:8000"

@given('que he iniciado un nuevo juego')
def step_iniciar_nuevo_juego(context):
    response = requests.post(f"{base_url}/juego/iniciar", params={"dificultad": "facil"})
    assert response.status_code == 200
    context.secuencia = response.json()["secuencia"]
    
@given('he validado correctamente la secuencia')
def step_validar_secuencia_correcta(context):
    response = requests.post(f"{base_url}/juego/iniciar", params={"dificultad": "facil"})
    assert response.status_code == 200
    context.secuencia_anterior = response.json()["secuencia"]

    # Validar la secuencia
    response = requests.post(f"{base_url}/juego/validar", json=context.secuencia_anterior)
    assert response.status_code == 200

@when('reinicio el juego')
def step_reiniciar_juego(context):
    response = requests.post(f"{base_url}/juego/iniciar", params={"dificultad": "facil"})
    assert response.status_code == 200
    context.secuencia_nueva = response.json()["secuencia"]
    context.puntuacion_nueva = response.json()["puntuacion"]

@then('el sistema debe generar una nueva secuencia')
def step_verificar_nueva_secuencia(context):
    assert context.secuencia_nueva != context.secuencia_anterior, "La secuencia debería haber cambiado"

@then('la puntuación debe reiniciarse a cero')
def step_verificar_puntuacion_reiniciada(context):
    assert context.puntuacion_nueva == 0, "La puntuación debería reiniciarse a 0"
