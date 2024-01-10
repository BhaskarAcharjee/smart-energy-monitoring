# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simulated data for energy monitoring
energy_data = {
    'solar': 300,
    'wind': 150,
    'consumption': 450,
}

@app.route('/')
def home():
    return render_template('index.html', energy_data=energy_data)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(energy_data)

@app.route('/api/update', methods=['POST'])
def update_data():
    global energy_data

    # Simulated update from sensors
    data = request.get_json()
    energy_data['solar'] = data.get('solar', energy_data['solar'])
    energy_data['wind'] = data.get('wind', energy_data['wind'])
    energy_data['consumption'] = data.get('consumption', energy_data['consumption'])

    return jsonify({'message': 'Data updated successfully'})

if __name__ == '__main__':
    app.run(debug=True)
