from behave import *
from app.sequence import GeneradorSecuencias

# Contexto compartido
@given('que inicio un nuevo juego')
def step_iniciar_nuevo_juego(context):
    context.generador = GeneradorSecuencias()
    context.secuencia_actual = context.generador.generar_secuencia(1) 
    
@when('solicito la generación de una nueva secuencia')
def step_generar_secuencia(context):
    context.secuencia_nueva = context.generador.generar_secuencia(1)

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
