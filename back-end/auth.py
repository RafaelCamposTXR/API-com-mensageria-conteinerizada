from flask import Flask, request, jsonify
from flask import Blueprint

auth = Blueprint('auth', __name__)

users = {
    "user1": "password1",
    "user2": "password2"
}

@auth.route('/login', methods=['POST'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Falha na autenticação'}), 401
    
    if auth.username in users and users[auth.username] == auth.password:
        return jsonify({'message': 'Autenticação bem-sucedida'}), 200
    
    return jsonify({'message': 'Credenciais inválidas'}), 401


# Simulação de banco de dados de usuários, descobrir como conectar com o banco de dados
