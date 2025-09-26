from flask import Flask, render_template, abort

app = Flask(__name__)

# Base de datos de vehículos (en memoria)
vehicles = [
    {
        "id": 1,
        "marca": "Toyota",
        "modelo": "Corolla",
        "año": 2020,
        "precio": 18900,
        "kilometraje": 45000,
        "descripcion": "Toyota Corolla 2020 en excelente estado. Color rojo con interior negro. Transmisión automática, un solo dueño, título limpio.",
        "imagen": "images/toyota/corolla_2020_rojo_1.jpg",
        "imagenes": [
            "images/toyota/corolla_2020_rojo_1.jpg",
            "images/toyota/corolla_2020_rojo_2.jpg",
            "images/toyota/corolla_2020_rojo_3.jpg"
        ]
    },
    {
        "id": 2,
        "marca": "Toyota",
        "modelo": "RAV4",
        "año": 2021,
        "precio": 25900,
        "kilometraje": 35000,
        "descripcion": "Toyota RAV4 2021 en perfectas condiciones. Color blanco perla con interior en tela negra. Toyota Safety Sense 2.0, cámara de reversa.",
        "imagen": "images/toyota/rav4_2021_blanco_1.jpg",
        "imagenes": [
            "images/toyota/rav4_2021_blanco_1.jpg",
            "images/toyota/rav4_2021_blanco_2.jpg",
            "images/toyota/rav4_2021_blanco_3.jpg"
        ]
    },
    {
        "id": 3,
        "marca": "Ford",
        "modelo": "Mustang",
        "año": 2022,
        "precio": 38000,
        "kilometraje": 15000,
        "descripcion": "Ford Mustang GT 2022. V8. Color azul metalizado. Asientos de cuero, paquete deportivo, como nuevo.",
        "imagen": "images/ford/mustang_2022_azul_1.jpg",
        "imagenes": [
            "images/ford/mustang_2022_azul_1.jpg",
            "images/ford/mustang_2022_azul_2.jpg",
            "images/ford/mustang_2022_azul_3.jpg"
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html', vehicles=vehicles)

@app.route('/vehicle/<int:vehicle_id>')
def vehicle_detail(vehicle_id):
    vehicle = next((v for v in vehicles if v['id'] == vehicle_id), None)
    if vehicle is None:
        abort(404)
    return render_template('vehicle_detail.html', vehicle=vehicle)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)