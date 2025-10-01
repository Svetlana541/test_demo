# импортируем класс Flask
from flask import Flask

# импортируем Redis
import redis
 
# создаем экземпляр приложения Flask
app = Flask(__name__)
 
# подключимся к серверу Redis
r = redis.Redis(host='redis', port=6379)
 
# ДОзаписываем ключ и значение в Redis
r.append('msg', 'Hello Docker Compose ')
 
@app.route('/')
def hello():
    return r.get('msg').decode()
 
#запускаем локальный сервер разработки Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)