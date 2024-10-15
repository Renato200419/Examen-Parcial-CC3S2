Feature: Implementar sistema de puntuación y niveles de dificultad en Simon Says

    Scenario: Selección de dificultad
        Given que inicio una nueva partida
        When selecciono el nivel de dificultad "dificil"
        Then el juego debe generar secuencias de colores acorde al nivel seleccionado "dificil"

    Scenario: Incremento de puntuación por secuencia correcta
        Given que he ingresado una secuencia correcta
        When el sistema va a validar la secuencia
        Then mi puntuación debe incrementarse con base en la longitud de la secuencia

    Scenario: Continuar el juego con secuencias adicionales
        Given que he ingresado una nueva secuencia correcta en el nivel "dificil"
        When solicito continuar el juego
        Then la secuencia debe aumentar en longitud y contener más colores