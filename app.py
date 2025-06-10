from flask import Flask, jsonify, render_template_string, send_from_directory
import os
import time
import random
from datetime import datetime
import psycopg2
from psycopg2 import OperationalError

app = Flask(__name__)

# Feature flags
FEATURE_FLAGS = {
    'USE_POSTGRES': os.getenv('USE_POSTGRES', 'false').lower() == 'true',
    'FAIL_AFTER_START': os.getenv('FAIL_AFTER_START', 'false').lower() == 'true'
}

# Background color
BACKGROUND_COLOR = os.getenv('BACKGROUND_COLOR', '#ffffff')

# Port configuration
PORT = int(os.getenv('PORT', '5000'))

# Database connection
def get_db_connection():
    if not FEATURE_FLAGS['USE_POSTGRES']:
        return None
    try:
        return psycopg2.connect(
            host=os.getenv('POSTGRES_HOST', 'localhost'),
            database=os.getenv('POSTGRES_DB', 'demo'),
            user=os.getenv('POSTGRES_USER', 'postgres'),
            password=os.getenv('POSTGRES_PASSWORD', 'postgres')
        )
    except OperationalError:
        return None

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
        {% for flag, value in FEATURE_FLAGS.items() %}
        <li>{{ flag }}: {{ value }}</li>
        {% endfor %}
    </ul>
    <div class="image-container">
        <img src="/static/photo.jpg" alt="Demo Image">
    </div>
</body>
</html>
"""

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/')
def home():
    db_status = "Connected" if get_db_connection() else "Not connected"
    return render_template_string(
        HTML_TEMPLATE,
        current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        db_status=db_status,
        FEATURE_FLAGS=FEATURE_FLAGS,
        BACKGROUND_COLOR=BACKGROUND_COLOR
    )

@app.route('/health/ready')
def readiness():
    if FEATURE_FLAGS['USE_POSTGRES'] and not get_db_connection():
        return jsonify({"status": "not ready"}), 503
    return jsonify({"status": "ready"})

@app.route('/health/live')
def liveness():
    return jsonify({"status": "alive"})

@app.route('/info')
def info():
    return jsonify({
        "app": "demo",
        "version": "1.0.0",
        "features": FEATURE_FLAGS
    })

if __name__ == '__main__':
    if FEATURE_FLAGS['FAIL_AFTER_START']:
        time.sleep(random.randint(5, 15))
        raise Exception("Simulated failure after startup")
    app.run(host='0.0.0.0', port=PORT)