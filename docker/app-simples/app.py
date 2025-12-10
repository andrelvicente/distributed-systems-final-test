#!/usr/bin/env python3
"""
Aplicação web MUITO SIMPLES para aprender Docker
Esta aplicação apenas mostra uma mensagem quando você acessa no navegador
"""
from flask import Flask, jsonify
import socket

# Criar a aplicação Flask
app = Flask(__name__)

# Rota principal - quando você acessa http://localhost:5000
@app.route('/')
def home():
    # Pegar o nome do container (hostname)
    hostname = socket.gethostname()
    
    # Retornar uma mensagem em formato JSON
    return jsonify({
        'mensagem': 'Olá! Esta aplicação está rodando dentro de um container Docker! 🐳',
        'hostname': hostname,
        'status': 'online',
        'explicacao': 'Se você está vendo isso, o Docker funcionou!'
    })

# Rota de saúde - para verificar se a aplicação está funcionando
@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

# Iniciar o servidor
# host='0.0.0.0' significa que aceita conexões de qualquer lugar
# port=5000 é a porta que vamos usar
if __name__ == '__main__':
    print("🚀 Servidor iniciando na porta 5000...")
    print("📝 Acesse: http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)

