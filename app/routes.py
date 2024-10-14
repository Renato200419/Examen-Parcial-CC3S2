from fastapi import APIRouter
from app.sequence import GeneradorSecuencias

# Crear el enrutador de FastAPI
router = APIRouter()


# Inicializar el generador de secuencias
# Inicializar el generador de secuencias
generador_secuencias = GeneradorSecuencias()
secuencia_actual = []

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
def iniciar_juego():
    """Inicia un nuevo juego generando una secuencia de un solo color."""
    global secuencia_actual
    secuencia_actual = generador_secuencias.generar_secuencia()
    return {"mensaje": "Nuevo juego iniciado", "secuencia": secuencia_actual}