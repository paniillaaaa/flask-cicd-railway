from flask import Flask, render_template
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def index():
    db_url = os.environ.get("DATABASE_URL")
    if db_url:
        try:
            conn = psycopg2.connect(db_url)
            cur = conn.cursor()
            cur.execute("SELECT version();")
            db_version = cur.fetchone()
            return f"Connected to PostgreSQL: {db_version[0]}"
        except Exception as e:
            return f"Database connection error: {e}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
