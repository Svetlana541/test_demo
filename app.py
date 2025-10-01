from flask import Flask
import psycopg2

app = Flask(__name__)


def get_students():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="db"
    )
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students (id SERIAL PRIMARY KEY, name VARCHAR(50));")
    cur.execute("INSERT INTO students (name) VALUES ('Alice'), ('Bob'), ('Charlie') ON CONFLICT DO NOTHING;")
    conn.commit()
    cur.execute("SELECT name FROM students;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [row[0] for row in rows]

@app.route("/")
def index():
    students = get_students()
    return "<h1>Список студентов:</h1>" + "<br>".join(students)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
