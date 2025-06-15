from flask import Flask, jsonify, render_template_string, send_from_directory
import os
import time
import random
from datetime import datetime
import psycopg2
from psycopg2 import OperationalError

app = Flask(__name__)

# Feature flags
USE_POSTGRES = os.getenv("USE_POSTGRES", "false").lower() == "true"
FAIL_AFTER_START = os.getenv("FAIL_AFTER_START", "false").lower() == "true"

# Background color
BACKGROUND_COLOR = os.getenv('BACKGROUND_COLOR', '#ffffff')

# Port configuration
PORT = int(os.getenv('PORT', '5000'))

# --- DB config (з дефолтами) ---
if USE_POSTGRES:
    DB_CONFIG = {
        "host": os.getenv("POSTGRES_HOST", "localhost"),
        "database": os.getenv("POSTGRES_DB", "demo"),
        "user": os.getenv("POSTGRES_USER", "postgres"),
        "password": os.getenv("POSTGRES_PASSWORD", "postgres"),
    }
else:
    DB_CONFIG = None

# HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Demo Updated App Ostap</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: {{ BACKGROUND_COLOR }};
        }
        .image-container {
            margin: 20px 0;
            text-align: center;
        }
        .image-container img {
            max-width: 300px;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <h1>Demo Updated App Ostap</h1>
    <p>Current time: {{ current_time }}</p>
    <p>Database status: {{ db_status }}</p>
    <p>Feature flags:</p>
    <ul>
        <li>USE_POSTGRES: {{ use_postgres }}</li>
        <li>FAIL_AFTER_START: {{ fail_after_start }}</li>
    </ul>
    {% if quote %}
    <div class="quote-block">
        <blockquote>"{{ quote['quote'] }}"</blockquote>
        <p><strong>{{ quote['author'] }}</strong>, <em>{{ quote['work_title'] }}</em></p>
    </div>
    {% endif %}
    <div class="image-container">
        <img src="/static/photo.jpg" alt="Demo Image">
    </div>
</body>
</html>
"""

def connect_to_db():
    if not USE_POSTGRES or not DB_CONFIG:
        return None
    try:
        return psycopg2.connect(**DB_CONFIG)
    except psycopg2.OperationalError as e:
        print(f"[DB ERROR] Failed to connect to PostgreSQL: {e}")
        return None


# --- Get random quote ---
def fetch_random_quote():
    conn = connect_to_db()
    if not conn:
        return None
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT quote, work_title, author
                FROM quotes
                ORDER BY RANDOM()
                LIMIT 1;
            """)
            row = cur.fetchone()
            if row:
                return {'quote': row[0], 'work_title': row[1], 'author': row[2]}
    finally:
        conn.close()
    return None

# --- Routes ---
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/')
def home():
    db_connected = bool(connect_to_db())
    quote = fetch_random_quote() if db_connected else None
    return render_template_string(
        HTML_TEMPLATE,
        current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        db_status="Connected" if db_connected else "Not connected",
        use_postgres=USE_POSTGRES,
        fail_after_start=FAIL_AFTER_START,
        BACKGROUND_COLOR=BACKGROUND_COLOR,
        bg_color=BACKGROUND_COLOR,
        quote=quote
    )

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/health/ready')
def health_ready():
    if USE_POSTGRES and not connect_to_db():
        return jsonify({"status": "not ready"}), 503
    return jsonify({"status": "ready"})

@app.route('/health/live')
def health_live():
    return jsonify({"status": "alive"})

@app.route('/info')
def info():
    return jsonify({
        "app": "demo",
        "version": "1.0.0",
        "features": {
            "USE_POSTGRES": USE_POSTGRES,
            "FAIL_AFTER_START": FAIL_AFTER_START
        }
    })

if __name__ == '__main__':
    if FAIL_AFTER_START:
        time.sleep(random.randint(5, 15))
        raise Exception("Simulated failure after startup")
    app.run(host='0.0.0.0', port=PORT)