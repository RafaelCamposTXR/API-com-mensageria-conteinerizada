from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de banco de dados de usuários, descobrir como conectar com o banco de dados
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Falha na autenticação'}), 401
    
    if auth.username in users and users[auth.username] == auth.password:
        return jsonify({'message': 'Autenticação bem-sucedida'}), 200
    
    return jsonify({'message': 'Credenciais inválidas'}), 401

if __name__ == '__main__':
    app.run(debug=True)