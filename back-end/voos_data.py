from flask import Flask, jsonify, request

app = Flask(__name__)

# Dicionário simulando uma base de dados de voos
flights_data = {
    "2024-04-21": [
        {"flight_number": "FL123", "origin": "JFK", "destination": "LAX", "departure_time": "08:00"},
        {"flight_number": "FL456", "origin": "LAX", "destination": "ORD", "departure_time": "10:00"},
        {"flight_number": "FL789", "origin": "ORD", "destination": "DFW", "departure_time": "12:00"}
    ]
}

@app.route('/flights', methods=['GET'])
def get_flights():
    date = request.args.get('date')
    if not date:
        return jsonify({'error': 'Por favor, forneça a data dos voos'}), 400
    
    flights = flights_data.get(date)
    if flights:
        return jsonify({'date': date, 'flights': flights}), 200
    else:
        return jsonify({'error': 'Não há voos disponíveis para a data especificada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
