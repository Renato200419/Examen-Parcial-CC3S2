from behave import *
from app.validation import ValidadorSecuencias

@given('que el sistema ha generado una secuencia')
def step_generar_secuencia(context):
    context.secuencia_generada = ['rojo', 'verde', 'azul']  # Ejemplo de secuencia generada
    context.validador = ValidadorSecuencias(context.secuencia_generada)

@when('el jugador ingresa la secuencia correcta')
def step_ingresar_secuencia_correcta(context):
    context.secuencia_jugador = ['rojo', 'verde', 'azul']  # El jugador repite correctamente la secuencia
    context.resultado = context.validador.validar_secuencia(context.secuencia_jugador)

@then('el sistema confirma que la secuencia es correcta y el jugador continúa')
def step_verificar_secuencia_correcta(context):
    assert context.resultado is True, "La secuencia debería ser correcta"

@when('el jugador ingresa una secuencia incorrecta')
def step_ingresar_secuencia_incorrecta(context):
    context.secuencia_jugador = ['rojo', 'amarillo', 'azul']  # El jugador ingresa una secuencia incorrecta
    context.resultado = context.validador.validar_secuencia(context.secuencia_jugador)

@then('el sistema notifica que la secuencia es incorrecta y el juego termina')
def step_verificar_secuencia_incorrecta(context):
    assert context.resultado is False, "La secuencia debería ser incorrecta"
