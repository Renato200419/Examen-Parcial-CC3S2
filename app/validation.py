class ValidadorSecuencias:
    def __init__(self, secuencia_generada):
        self.secuencia_generada = secuencia_generada

    def validar_secuencia(self, secuencia_jugador):
        """Compara la secuencia del jugador con la generada"""
        return self.secuencia_generada == secuencia_jugador
