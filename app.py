import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, email TEXT)")
    conn.execute("INSERT INTO users (username, email) VALUES ('admin', 'admin@example.com')")
    return conn

@app.route("/user")
def find_user():
    conn = get_db()
    username = request.args.get("username", "")
    query = "SELECT id, email FROM users WHERE username = ?"
    row = conn.execute(query, (username,)).fetchone()
    return {"found": bool(row), "email": row[1] if row else None}

if __name__ == "__main__":
    app.run(port=5000)