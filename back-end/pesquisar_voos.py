from flask import Flask, jsonify, request

app = Flask(__name__)

# Dicionário simulando uma base de dados de voos com tarifas
flights_data = {
    "FL123": {"origin": "JFK", "destination": "LAX", "price": 200},
    "FL456": {"origin": "LAX", "destination": "ORD", "price": 250},
    "FL789": {"origin": "ORD", "destination": "DFW", "price": 300},
    "FL101": {"origin": "JFK", "destination": "DFW", "price": 220},
    "FL202": {"origin": "DFW", "destination": "ORD", "price": 280},
    "FL303": {"origin": "ORD", "destination": "JFK", "price": 240}
}

@app.route('/flights/cheapest', methods=['GET'])
def get_cheapest_flights():
    passengers = request.args.get('passengers')
    if not passengers:
        return jsonify({'error': 'Por favor, forneça o número de passageiros'}), 400
    
    try:
        passengers = int(passengers)
    except ValueError:
        return jsonify({'error': 'O número de passageiros deve ser um número inteiro'}), 400

    if passengers <= 0:
        return jsonify({'error': 'O número de passageiros deve ser maior que zero'}), 400

    sorted_flights = sorted(flights_data.items(), key=lambda x: x[1]['price'])
    cheapest_flights = sorted_flights[:passengers]

    return jsonify({'passengers': passengers, 'flights': cheapest_flights}), 200

if __name__ == '__main__':
    app.run(debug=True)
