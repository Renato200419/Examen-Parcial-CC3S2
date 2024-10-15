from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Aplicación para Simon Says"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_validar_secuencia_correcta():
    # Iniciar el juego para obtener la secuencia
    response = client.post("/juego/iniciar", params={"dificultad": "facil"})
    assert response.status_code == 200
    secuencia = response.json()["secuencia"]

    # Validar la secuencia correcta
    response = client.post("/juego/validar", json=secuencia)
    assert response.status_code == 200
    data = response.json()
    assert data["mensaje"] == "Secuencia correcta, continúa"
    assert "puntuacion" in data
    assert data["puntuacion"] > 0  # La puntuación debe incrementarse

def test_validar_secuencia_incorrecta():
    # Iniciar el juego para obtener la secuencia
    response = client.post("/juego/iniciar", params={"dificultad": "facil"})
    assert response.status_code == 200

    # Probar con una secuencia incorrecta
    secuencia_incorrecta = ["azul", "verde"]  # Asumimos que no es la secuencia correcta
    response = client.post("/juego/validar", json=secuencia_incorrecta)
    assert response.status_code == 400
    assert response.json()["detail"] == "Secuencia incorrecta. Juego terminado."

def test_validar_secuencia_vacia():
    # Iniciar el juego para obtener la secuencia
    response = client.post("/juego/iniciar", params={"dificultad": "facil"})
    assert response.status_code == 200

    # Probar con una secuencia vacía
    secuencia_vacia = []
    response = client.post("/juego/validar", json=secuencia_vacia)
    assert response.status_code == 400  # Esperamos un error de validación
    assert response.json()["detail"] == "Secuencia incorrecta. Juego terminado."

def test_continuar_juego():
    # Iniciar el juego
    response = client.post("/juego/iniciar", params={"dificultad": "facil"})
    assert response.status_code == 200
    secuencia = response.json()["secuencia"]

    # Validar la secuencia correcta
    response = client.post("/juego/validar", json=secuencia)
    assert response.status_code == 200

    # Continuar el juego y verificar que se añaden nuevos colores
    response = client.post("/juego/continuar")
    assert response.status_code == 200
    data = response.json()
    assert "secuencia" in data
    assert len(data["secuencia"]) > len(secuencia)  # La secuencia debe haber crecido

def test_reiniciar_juego():
    # Iniciar el juego
    response = client.post("/juego/iniciar", params={"dificultad": "facil"})
    assert response.status_code == 200
    secuencia_anterior = response.json()["secuencia"]

    # Validar la secuencia
    response = client.post("/juego/validar", json=secuencia_anterior)
    assert response.status_code == 200
    puntuacion_anterior = response.json()["puntuacion"]

    # Reiniciar el juego
    response = client.post("/juego/iniciar", params={"dificultad": "facil"})
    assert response.status_code == 200
    secuencia_nueva = response.json()["secuencia"]
    puntuacion_nueva = response.json()["puntuacion"]

    # Verificar que la secuencia y puntuación se reinician
    assert secuencia_nueva != secuencia_anterior  # La secuencia debería haber cambiado
    assert puntuacion_nueva == 0  # La puntuación debería reiniciarse a 0        

def test_iniciar_juego_facil():
    response = client.post("/juego/iniciar", params={"dificultad": "facil"})
    assert response.status_code == 200
    data = response.json()
    assert data["mensaje"] == "Nuevo juego iniciado"
    assert data["dificultad"] == "facil"
    assert len(data["secuencia"]) == 1  # El nivel fácil genera una secuencia de 1 color

def test_iniciar_juego_dificil():
    response = client.post("/juego/iniciar", params={"dificultad": "dificil"})
    assert response.status_code == 200
    data = response.json()
    assert data["mensaje"] == "Nuevo juego iniciado"
    assert data["dificultad"] == "dificil"
    assert len(data["secuencia"]) == 2  # El nivel difícil genera una secuencia de 2 colores

def test_puntuacion_dificil():
    # Iniciar el juego en modo difícil
    response = client.post("/juego/iniciar", params={"dificultad": "dificil"})
    assert response.status_code == 200
    secuencia = response.json()["secuencia"]

    # Validar la secuencia correcta
    response = client.post("/juego/validar", json=secuencia)
    assert response.status_code == 200
    puntuacion = response.json()["puntuacion"]

    # Verificar que la puntuación sea mayor que cero
    assert puntuacion > 0