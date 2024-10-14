import random

class GeneradorSecuencias:
    def __init__(self, colores=None):
        if colores is None:
            self.colores = ['rojo', 'verde', 'azul', 'amarillo']  # Colores por defecto
        else:
            self.colores = colores
        self.secuencia = []

    def generar_secuencia(self, longitud):
        """Genera una secuencia aleatoria de colores."""
        self.secuencia = random.choices(self.colores, k=longitud)
        return self.secuencia
