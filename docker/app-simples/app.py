#!/usr/bin/env python3
"""
Aplicação web simples para demonstrar Docker
"""
from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    return jsonify({
        'mensagem': 'Olá! Esta é uma aplicação rodando em Docker!',
        'hostname': hostname,
        'status': 'online',
        'versao': '1.0.0'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

@app.route('/info')
def info():
    return jsonify({
        'python_version': os.sys.version,
        'container_id': socket.gethostname()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

