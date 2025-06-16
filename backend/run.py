from flask import Flask, send_from_directory
from app.routes import rutas_bp
import os

app = Flask(__name__, static_folder="../frontend")

app.register_blueprint(rutas_bp)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
