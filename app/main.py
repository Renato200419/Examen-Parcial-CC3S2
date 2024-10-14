from fastapi import FastAPI
from app.routes import router as app_router
from prometheus_fastapi_instrumentator import Instrumentator
import uvicorn
app = FastAPI()

# Instrumentar la aplicación y exponer las métricas
instrumentator=Instrumentator()
instrumentator.instrument(app).expose(app)

# Incluir las rutas
app.include_router(app_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)