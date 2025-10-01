# Базовый образ с Python
FROM python:3.9

# Указываем рабочую директорию
WORKDIR /app

# Копируем наш код внутрь контейнера
COPY app.py .

# CMD — запускается при старте контейнера
CMD ["python", "app.py"]