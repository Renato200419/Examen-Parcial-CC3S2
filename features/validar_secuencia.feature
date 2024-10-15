Feature: Validación de secuencias ingresadas por el jugador

  Scenario: Validación exitosa de la secuencia
    Given que el sistema ha generado una secuencia
    When el jugador ingresa la secuencia correcta
    Then el sistema confirma que la secuencia es correcta y el jugador continúa

  Scenario: Validación fallida de la secuencia
    Given que el sistema ha generado una secuencia
    When el jugador ingresa una secuencia incorrecta
    Then el sistema notifica que la secuencia es incorrecta y el juego termina
