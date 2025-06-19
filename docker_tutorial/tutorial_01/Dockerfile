# Dockerfile 새롭게 만들기

# Docker-Compose.yml 

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501 

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]