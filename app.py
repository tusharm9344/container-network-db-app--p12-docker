from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = psycopg2.connect(
            host="postgres-db",
            database="myapp",
            user="postgres", 
            password="mypassword"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        conn.close()
        return f"Connected to database! PostgreSQL version: {db_version[0]}"
    except Exception as e:
        return f"Database connection failed: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
