Feature: Validación de secuencia vacía

  Scenario: Validar secuencia vacía
    Given que he iniciado un nuevo juego
    When envío una secuencia vacía
    Then el sistema devuelve un error indicando que la secuencia es incorrecta
