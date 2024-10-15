from behave import *
import requests

base_url = "http://localhost:8000"

@when('envío una secuencia vacía')
def step_enviar_secuencia_vacia(context):
    context.response = requests.post(f"{base_url}/juego/validar", json=[])
    assert context.response.status_code == 400

@then('el sistema devuelve un error indicando que la secuencia es incorrecta')
def step_verificar_error_secuencia_vacia(context):
    assert context.response.json()["detail"] == "Secuencia incorrecta. Juego terminado."
