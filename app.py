from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    try:
        db_url = os.environ['DATABASE_URL']
        conn = psycopg2.connect(db_url, sslmode='require')
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f"✅ Connected to DB: {db_version}"
    except Exception as e:
        return f"❌ DB Connection Failed: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
