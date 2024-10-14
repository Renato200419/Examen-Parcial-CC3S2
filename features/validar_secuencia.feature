Feature: Validación de secuencias ingresadas por el jugador
  Como desarrollador,
  Quiero implementar la validación de secuencias,
  Para verificar que el jugador repita correctamente la secuencia generada y avanzar o finalizar el juego.

  Scenario: Validación exitosa de la secuencia
    Given que el sistema ha generado una secuencia
    When el jugador ingresa la secuencia correcta
    Then el sistema confirma que la secuencia es correcta y el jugador continúa

  Scenario: Validación fallida de la secuencia
    Given que el sistema ha generado una secuencia
    When el jugador ingresa una secuencia incorrecta
    Then el sistema notifica que la secuencia es incorrecta y el juego termina
