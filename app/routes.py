from fastapi import APIRouter

# Crear el enrutador de FastAPI
router = APIRouter()

# Rutas de la API

# Ruta principal
@router.get("/")
def root():
    return {"message": "Bienvenido a la app!"}

# Ruta de verificación de salud
@router.get("/health")
def health_check():
    return {"status": "healthy"}
