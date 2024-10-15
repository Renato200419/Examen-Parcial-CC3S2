Feature: Reiniciar juego
  
  Scenario: Reiniciar el juego
    Given que he iniciado un nuevo juego
    And he validado correctamente la secuencia
    When reinicio el juego
    Then el sistema debe generar una nueva secuencia
    And la puntuación debe reiniciarse a cero
