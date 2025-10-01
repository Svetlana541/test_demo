# Базовый образ с Python
FROM python:3.9

# Указываем рабочую директорию
WORKDIR /app

# RUN — установка flask и redis на этапе сборки образа
RUN pip install flask redis pytest

# Указываем, какой порт будет открыт для доступа (не обязательно)
EXPOSE 8000

# Копируем наш код внутрь контейнера
COPY app.py .

# CMD — запускается при старте контейнера
CMD ["python", "app.py"]