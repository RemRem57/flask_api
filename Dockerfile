# Utilisez l'image Python officielle comme base
FROM python:3.8-slim

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