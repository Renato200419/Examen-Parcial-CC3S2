Feature: Generación de secuencias aleatorias de colores

  Scenario: Generación exitosa de una secuencia de un solo color
    Given que inicio un nuevo juego
    When solicito la generación de una nueva secuencia
    Then el sistema genera una secuencia de un color aleatorio

  Scenario: Aumento de la secuencia con cada nivel
    Given que he superado un nivel del juego
    When solicito una nueva secuencia
    Then la secuencia aumenta en longitud y contiene más colores
