#!/usr/bin/env python3
"""
Aplicação web que demonstra comunicação entre containers
"""
from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'mensagem': 'Aplicação rodando com Docker Compose!',
        'servicos': {
            'web': 'http://localhost:5000',
            'database': 'postgresql://db:5432',
            'redis': 'redis://redis:6379'
        },
        'hostname': socket.gethostname()
    })

@app.route('/status')
def status():
    return jsonify({
        'status': 'online',
        'database_url': os.getenv('DATABASE_URL', 'not configured')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

