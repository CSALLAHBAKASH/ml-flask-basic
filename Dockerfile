# Dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]

# docker build -t myapp .
# docker run -d --name myapp -p 5000:5000 myapp
# docker logs myapp
# docker login
# docker tag myapp:latest 46076516/myapp:latest