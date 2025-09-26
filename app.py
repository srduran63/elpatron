import os
from flask import Flask, render_template, abort, url_for, request, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix
from waitress import serve

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Configuración para las IPs de Render
ALLOWED_HOSTS = [
    '35.160.120.126',
    '44.233.151.27',
    '34.211.200.85',
    '74.220.48.0/24',
    '74.220.56.0/24'
]

app.config['ALLOWED_HOSTS'] = ALLOWED_HOSTS
app.config['PREFERRED_URL_SCHEME'] = 'https'

# Catálogo de vehículos
vehicles = [
    {
        'id': '1',
        'marca': 'Toyota',
        'modelo': 'Corolla',
        'año': 2020,
        'precio': 15000,
        'kilometraje': 45000,
        'imagen': 'images/corolla.jpg',
        'detalles': {
            'motor': '1.8L',
            'transmision': 'Automática',
            'combustible': 'Gasolina'
        }
    },
    {
        'id': '2',
        'marca': 'Honda',
        'modelo': 'Civic',
        'año': 2019,
        'precio': 14500,
        'kilometraje': 52000,
        'imagen': 'images/civic.jpg',
        'detalles': {
            'motor': '2.0L',
            'transmision': 'Manual',
            'combustible': 'Gasolina'
        }
    },
    # ...existing code... (aquí irían más vehículos)
]

@app.route('/')
def index():
    return render_template('index.html', vehicles=vehicles)

@app.route('/vehicle/<string:vehicle_id>')
def vehicle_detail(vehicle_id):
    vehicle = next((v for v in vehicles if v['id'] == vehicle_id), None)
    if vehicle is None:
        abort(404)
    return render_template('vehicle_detail.html', vehicle=vehicle)

@app.route('/api/vehicles')
def get_vehicles():
    return jsonify(vehicles)

@app.route('/api/vehicles/<string:vehicle_id>')
def get_vehicle(vehicle_id):
    vehicle = next((v for v in vehicles if v['id'] == vehicle_id), None)
    if vehicle is None:
        abort(404)
    return jsonify(vehicle)

@app.route('/contact', methods=['POST'])
def contact():
    try:
        data = request.form
        # Aquí iría la lógica para procesar el formulario de contacto
        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    if os.environ.get('FLASK_ENV') == 'development':
        app.run(host='0.0.0.0', port=port, debug=True)
    else:
        serve(app, host='0.0.0.0', port=port)