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