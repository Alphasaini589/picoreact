from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="db",
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )

@app.route("/")
def home():
    return "Backend connected"

@app.route("/health")
def health():
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT 1")
        return {"status": "up", "db": "connected"}
    except Exception as e:
        return {"status": "down", "error": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)