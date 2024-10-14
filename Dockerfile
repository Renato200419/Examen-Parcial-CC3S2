FROM python:3.8

# Crear directorio de la app y copiar todo el contenido
WORKDIR /app

# Copiar el contenido del directorio actual a /app en el contenedor
COPY . /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto
EXPOSE 8000

# Ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
