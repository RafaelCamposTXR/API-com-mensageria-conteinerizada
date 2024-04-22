from flask import Flask, jsonify, request

app = Flask(__name__)

# Dicionário simulando a associação entre aeroportos de origem e destino, conectar com o banco de dados 
flight_destinations = {
    "JFK": ["LAX", "ORD", "DFW"],
    "LAX": ["JFK", "ORD", "DFW"],
    "ORD": ["JFK", "LAX", "DFW"],
    "DFW": ["JFK", "LAX", "ORD"]
}

@app.route('/flight-destinations', methods=['GET'])
def get_flight_destinations():
    origin = request.args.get('origin')
    if not origin:
        return jsonify({'error': 'Por favor, forneça o aeroporto de origem'}), 400
    
    destinations = flight_destinations.get(origin.upper())
    if destinations:
        return jsonify({'origin': origin, 'destinations': destinations}), 200
    else:
        return jsonify({'error': 'Aeroporto de origem não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
