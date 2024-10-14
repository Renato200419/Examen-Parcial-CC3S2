from fastapi import APIRouter, HTTPException
from app.sequence import GeneradorSecuencias
from app.validation import ValidadorSecuencias

# Crear el enrutador de FastAPI
router = APIRouter()

# Inicializar el generador de secuencias
generador_secuencias = GeneradorSecuencias()
secuencia_actual = []
puntuacion = 0
modo_dificultad= "facil" # Por defecto, el modo es fácil

# Rutas de la API
# Rutas de la API

# Ruta principal
@router.get("/")
def root():
    return {"message": "Aplicación para Simon Says"}

# Ruta de verificación de salud
@router.get("/health")
def health_check():
    return {"status": "healthy"}

@router.post("/juego/iniciar")
def iniciar_juego(dificultad: str = "facil"):
    """Inicia un nuevo juego generando una secuencia de un solo color."""
    global secuencia_actual, puntuacion, modo_dificultad
    secuencia_actual = generador_secuencias.generar_secuencia(1 if dificultad == "facil" else 2)
    puntuacion = 0 # Esto reinicia la aplicacion 
    modo_dificultad = dificultad # Establece el modo de dificultad
    return {"mensaje": "Nuevo juego iniciado", "secuencia": secuencia_actual, "puntuacion": puntuacion,"dificultad": modo_dificultad}

@router.post("/juego/validar")
def validar_secuencia(secuencia_jugador: list[str]):
    """Válida la secuencia del jugador"""
    global secuencia_actual, puntuacion
    validador = ValidadorSecuencias(secuencia_actual)
    es_valida = validador.validar_secuencia(secuencia_jugador)
    if not es_valida:
        raise HTTPException(status_code=400, detail="Secuencia incorrecta. Juego terminado.")
    # Actualizar puntuación si la secuencia es correcta
    puntuacion += len(secuencia_actual)
    return {"mensaje": "Secuencia correcta, continúa", "puntuacion": puntuacion, "secuencia": secuencia_actual}

@router.post("/juego/continuar")
def continuar_juego():
    """Añade un nuevo color a la secuencia si el jugador ha acertado"""
    global secuencia_actual, modo_dificultad
    cantidad_colores = 1 if modo_dificultad == "facil" else 2
    nuevos_colores = generador_secuencias.generar_secuencia(cantidad_colores)
    secuencia_actual.extend(nuevos_colores)  # Añadir uno o dos colores a la secuencia
    return {"mensaje": f"{cantidad_colores} color(es) añadido(s)", "secuencia": secuencia_actual}
