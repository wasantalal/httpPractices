# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

EXPOSE 8000


# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser


CMD ["uvicorn", "http_mongo_docker.main:app","--host", "0.0.0.0","--port","8000"]

# docker images
# docker build -t http_mongo_docker:v1 .
# docker run -d -p 8000:8000 http_mongo_docker:v1 
# http://127.0.0.1:8000/user/Wasan