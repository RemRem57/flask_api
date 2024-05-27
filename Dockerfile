# Utilisez l'image Python officielle comme base
FROM arm64v8/python:3.8-slim

# Install required packages
RUN apt-get update && apt-get install -y \
    python3-dev \
    python3-rpi.gpio \
    build-essential

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers de votre application dans le conteneur
COPY . .

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposez le port sur lequel votre application Flask écoute
EXPOSE 5000

# Démarrez votre application
CMD ["python", "app.py"]