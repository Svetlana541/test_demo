FROM python:3.9

WORKDIR /app

RUN pip install flask psycopg2-binary

COPY app.py .

CMD ["python", "app.py"]