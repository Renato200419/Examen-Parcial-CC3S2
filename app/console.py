import requests

class ConsolaSimonSays:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.secuencia_actual = []  # Almacena la secuencia completa generada
        self.nuevo_color = None  # Almacena el nuevo color que se añade

    def mostrar_menu_colores(self):
        """Muestra un menú para que el jugador seleccione colores."""
        print("Selecciona el color correspondiente:")
        print("1. Rojo")
        print("2. Verde")
        print("3. Azul")
        print("4. Amarillo")

    def obtener_secuencia_jugador(self):
        """Permite al jugador seleccionar los colores de la secuencia actual."""
        secuencia_jugador = []
        for i in range(len(self.secuencia_actual)):
            self.mostrar_menu_colores()
            opcion = int(input("Elige un número (1-4): ").strip())
            
            if opcion == 1:
                secuencia_jugador.append('rojo')
            elif opcion == 2:
                secuencia_jugador.append('verde')
            elif opcion == 3:
                secuencia_jugador.append('azul')
            elif opcion == 4:
                secuencia_jugador.append('amarillo')
            else:
                print("Opción no válida, intenta nuevamente.")
                return self.obtener_secuencia_jugador()  # Reinicia si hay un error en la entrada
        return secuencia_jugador

    def iniciar_juego(self):
        """Llama al endpoint para iniciar el juego."""
        response = requests.post(f"{self.base_url}/juego/iniciar")
        if response.status_code == 200:
            self.secuencia_actual = response.json()["secuencia"]
            self.nuevo_color = self.secuencia_actual[-1]
            print(f"Juego iniciado. Secuencia: [{self.nuevo_color}]")  # Muestra solo el nuevo color
        else:
            print("Error al iniciar el juego.")

    def validar_jugada(self, secuencia_jugador):
        """Llama al endpoint para validar la jugada del jugador."""
        response = requests.post(f"{self.base_url}/juego/validar", json=secuencia_jugador)
        if response.status_code == 200:
            print("¡Secuencia correcta! Continúa.")
            return True
        else:
            print(f"Secuencia incorrecta. Juego terminado. {response.json()['detail']}")
            return False

    def continuar_juego(self):
        """Llama al endpoint para continuar el juego, añadiendo un nuevo color."""
        response = requests.post(f"{self.base_url}/juego/continuar")
        if response.status_code == 200:
            self.secuencia_actual = response.json()["secuencia"]
            self.nuevo_color = self.secuencia_actual[-1]
            print(f"Nuevo color añadido: {self.nuevo_color}")  # Solo muestra el nuevo color
        else:
            print("Error al continuar el juego.")

    def jugar(self):
        """Lógica principal del juego."""
        self.iniciar_juego()
        while True:
            # Obtener la secuencia del jugador
            secuencia_jugador = self.obtener_secuencia_jugador()
            
            # Validar la secuencia del jugador
            if not self.validar_jugada(secuencia_jugador):
                break  # Termina el juego si la secuencia es incorrecta
            
            # Continuar el juego si la secuencia es correcta
            self.continuar_juego()

if __name__ == "__main__":
    juego = ConsolaSimonSays()
    juego.jugar()
