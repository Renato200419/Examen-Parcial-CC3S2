Feature: Implementar sistema de puntuación y niveles de dificultad en Simon Says

    Scenario: Selección de dificultad

        Given que inicio un nuevo juego,
        When selecciono el nivel de dificultad,
        Then el juego debe generar secuencias de colores acorde al nivel seleccionado (fácil o difícil).
    
    Scenario: Incremento de puntuación por secuencia correcta
        Given que he ingresado una secuencia correcta,
        When el sistema valida la secuencia,
        Then mi puntuación debe incrementarse con base en la longitud de la secuencia.

    Scenario: Continuar el juego con secuencias adicionales
        Given que he ingresado una secuencia correcta,
        When solicito continuar el juego,
        Then el juego debe añadir uno o dos colores adicionales a la secuencia dependiendo de la dificultad seleccionada.
