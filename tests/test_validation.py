import pytest
from app.validation import ValidadorSecuencias


# Prueba para validar que la secuencia es correcta
def test_validar_secuencia_correcta():
    secuencia_generada = ['rojo', 'verde', 'azul']  # Secuencia generada por el sistema
    validador = ValidadorSecuencias(secuencia_generada)

    secuencia_jugador = ['rojo', 'verde', 'azul']  # Secuencia ingresada por el jugador
    assert validador.validar_secuencia(secuencia_jugador) is True, "La secuencia debería ser correcta"


# Prueba para validar que la secuencia es incorrecta
def test_validar_secuencia_incorrecta():
    secuencia_generada = ['rojo', 'verde', 'azul']  # Secuencia generada por el sistema
    validador = ValidadorSecuencias(secuencia_generada)

    secuencia_jugador = ['rojo', 'amarillo', 'azul']  # Secuencia ingresada por el jugador que es incorrecta
    assert validador.validar_secuencia(secuencia_jugador) is False, "La secuencia debería ser incorrecta"


# Prueba para validar que una secuencia vacía falla
def test_validar_secuencia_vacia():
    secuencia_generada = ['rojo', 'verde', 'azul']  # Secuencia generada por el sistema
    validador = ValidadorSecuencias(secuencia_generada)

    secuencia_jugador = []  # Secuencia vacía
    assert validador.validar_secuencia(secuencia_jugador) is False, "Una secuencia vacía no debería ser correcta"
