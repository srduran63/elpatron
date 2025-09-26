from flask import Flask, render_template, abortfrom flask import Flask, render_template_string, request, redirect, url_for



app = Flask(__name__)app = Flask(__name__)



# Base de datos de vehículos (en memoria)# Base de datos MAZDA y TOYOTA COROLLA (2015-2025)

vehicles = [autos_db = [

    {    # TOYOTA COROLLA 2025

        "id": 1,    {

        "marca": "Toyota",        'id': 1,

        "modelo": "Corolla",        'marca': 'Toyota',

        "año": 2020,        'modelo': 'Corolla LE 2025',

        "precio": 18900,        'año': 2025,

        "kilometraje": 45000,        'precio': 24300,

        "descripcion": "Toyota Corolla 2020 en excelente estado. Color rojo con interior negro. Transmisión automática, un solo dueño, título limpio.",        'kilometraje': 0,

        "imagen": "images/toyota/corolla_2020_rojo_1.jpg",        'descripcion': 'Toyota Corolla LE 2025 completamente nuevo con Toyota Safety Sense 2.0, diseño renovado y máxima eficiencia. El futuro de los compactos está aquí.',

        "imagenes": [        'imagen': 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23dc2626"/><text x="400" y="240" font-family="Arial" font-size="24" font-weight="bold" text-anchor="middle" fill="white">COROLLA LE 2025</text></svg>',

            "images/toyota/corolla_2020_rojo_1.jpg",        'imagenes': [

            "images/toyota/corolla_2020_rojo_2.jpg",            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23dc2626"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Vista Frontal</text></svg>',

            "images/toyota/corolla_2020_rojo_3.jpg"            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23000"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Interior Premium</text></svg>',

        ]            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23333"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Panel Digital</text></svg>',

    },            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%236366f1"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Vista Trasera</text></svg>'

    {        ],

        "id": 2,        'caracteristicas': [

        "marca": "Toyota",            'Toyota Safety Sense 2.0',

        "modelo": "RAV4",            'Pantalla táctil de 8 pulgadas',

        "año": 2021,            'Apple CarPlay y Android Auto',

        "precio": 25900,            'Cámara de reversa HD',

        "kilometraje": 35000,            'Control crucero adaptativo',

        "descripcion": "Toyota RAV4 2021 en perfectas condiciones. Color blanco perla con interior en tela negra. Toyota Safety Sense 2.0, cámara de reversa.",            'Asientos calefaccionados'

        "imagen": "images/toyota/rav4_2021_blanco_1.jpg",        ]

        "imagenes": [    },

            "images/toyota/rav4_2021_blanco_1.jpg",    # MAZDA 3 2025

            "images/toyota/rav4_2021_blanco_2.jpg",    {

            "images/toyota/rav4_2021_blanco_3.jpg"        'id': 2,

        ]        'marca': 'Mazda',

    },        'modelo': 'Mazda 3 Hatchback 2025',

    {        'año': 2025,

        "id": 3,        'precio': 26500,

        "marca": "Ford",        'kilometraje': 0,

        "modelo": "Mustang",        'descripcion': 'Mazda 3 Hatchback 2025 con diseño KODO refinado, tecnología SKYACTIV-G avanzada y experiencia de conducción premium. Elegancia japonesa redefinida.',

        "año": 2022,        'imagen': 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23000"/><text x="400" y="240" font-family="Arial" font-size="22" font-weight="bold" text-anchor="middle" fill="white">MAZDA 3 HATCHBACK 2025</text></svg>',

        "precio": 38000,        'imagenes': [

        "kilometraje": 15000,            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23dc2626"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Diseño KODO</text></svg>',

        "descripcion": "Ford Mustang GT 2022. V8. Color azul metalizado. Asientos de cuero, paquete deportivo, como nuevo.",            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23000"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Motor SKYACTIV-G</text></svg>',

        "imagen": "images/ford/mustang_2022_azul_1.jpg",            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23333"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Cabina Premium</text></svg>',

        "imagenes": [            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%236366f1"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Tecnología Conectada</text></svg>'

            "images/ford/mustang_2022_azul_1.jpg",        ],

            "images/ford/mustang_2022_azul_2.jpg",        'caracteristicas': [

            "images/ford/mustang_2022_azul_3.jpg"            'Motor SKYACTIV-G 2.5L',

        ]            'Diseño KODO premium',

    }            'Pantalla MAZDA CONNECT',

]            'Sistema i-ACTIVSENSE',

            'Tracción AWD disponible',

@app.route('/')            'Asientos de cuero disponibles'

def index():        ]

    return render_template('index.html', vehicles=vehicles)    },

    # TOYOTA COROLLA 2024

@app.route('/vehicle/<int:vehicle_id>')    {

def vehicle_detail(vehicle_id):        'id': 3,

    vehicle = next((v for v in vehicles if v['id'] == vehicle_id), None)        'marca': 'Toyota',

    if vehicle is None:        'modelo': 'Corolla XLE 2024',

        abort(404)        'año': 2024,

    return render_template('vehicle_detail.html', vehicle=vehicle)        'precio': 26950,

        'kilometraje': 1200,

@app.errorhandler(404)        'descripcion': 'Toyota Corolla XLE 2024 versión premium con acabados de lujo, tecnología avanzada y máximo confort. La experiencia Corolla más refinada.',

def page_not_found(e):        'imagen': 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23059669"/><text x="400" y="240" font-family="Arial" font-size="22" font-weight="bold" text-anchor="middle" fill="white">COROLLA XLE 2024</text></svg>',

    return render_template('404.html'), 404        'imagenes': [

            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23059669"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Exterior Premium</text></svg>',

if __name__ == '__main__':            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23000"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Interior de Lujo</text></svg>',

    app.run(debug=True)            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23333"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Tecnología Avanzada</text></svg>',
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%236366f1"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Sistema Audio JBL</text></svg>'
        ],
        'caracteristicas': [
            'Acabados premium XLE',
            'Sistema de audio JBL',
            'Asientos de cuero SofTex',
            'Techo corredizo eléctrico',
            'Llantas de aleación 17"',
            'Cargador inalámbrico Qi'
        ]
    },
    # MAZDA CX-5 2024
    {
        'id': 4,
        'marca': 'Mazda',
        'modelo': 'Mazda CX-5 Turbo 2024',
        'año': 2024,
        'precio': 36800,
        'kilometraje': 800,
        'descripcion': 'Mazda CX-5 Turbo 2024 - SUV premium con motor turboalimentado, tracción AWD i-ACTIV y tecnología de vanguardia. Versatilidad y elegancia unificadas.',
        'imagen': 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23000"/><text x="400" y="240" font-family="Arial" font-size="20" font-weight="bold" text-anchor="middle" fill="white">MAZDA CX-5 TURBO 2024</text></svg>',
        'imagenes': [
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23dc2626"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Motor Turbo</text></svg>',
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23000"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">AWD i-ACTIV</text></svg>',
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23333"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Cabina Espaciosa</text></svg>',
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%236366f1"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Carga Premium</text></svg>'
        ],
        'caracteristicas': [
            'Motor turbo SKYACTIV-G 2.5T',
            'Tracción AWD i-ACTIV',
            'Sistema de sonido BOSE',
            'Pantalla de 10.25 pulgadas',
            'Asientos ventilados y calefaccionados',
            'Portón trasero eléctrico'
        ]
    },
    # TOYOTA COROLLA 2023
    {
        'id': 5,
        'marca': 'Toyota',
        'modelo': 'Corolla SE 2023',
        'año': 2023,
        'precio': 25200,
        'kilometraje': 3500,
        'descripcion': 'Toyota Corolla SE 2023 versión deportiva con suspensión sport-tuned, diseño agresivo y tecnología de conectividad avanzada.',
        'imagen': 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23ef4444"/><text x="400" y="240" font-family="Arial" font-size="22" font-weight="bold" text-anchor="middle" fill="white">COROLLA SE 2023</text></svg>',
        'imagenes': [
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23ef4444"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Diseño Deportivo</text></svg>',
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23000"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Suspensión Sport</text></svg>',
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23333"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Cockpit Deportivo</text></svg>',
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%236366f1"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Llantas 18 Sport</text></svg>'
        ],
        'caracteristicas': [
            'Suspensión sport-tuned',
            'Kit aerodinámico SE',
            'Llantas deportivas de 18"',
            'Asientos deportivos',
            'Paddle shifters CVT',
            'Escape deportivo'
        ]
    },
    # MAZDA MX-5 MIATA 2023
    {
        'id': 6,
        'marca': 'Mazda',
        'modelo': 'MX-5 Miata RF 2023',
        'año': 2023,
        'precio': 34500,
        'kilometraje': 2100,
        'descripcion': 'Mazda MX-5 Miata RF 2023 - El roadster perfecto con techo retráctil rígido, motor SKYACTIV-G y pura esencia deportiva japonesa.',
        'imagen': 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23991b1b"/><text x="400" y="240" font-family="Arial" font-size="20" font-weight="bold" text-anchor="middle" fill="white">MX-5 MIATA RF 2023</text></svg>',
        'imagenes': [
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23991b1b"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Techo Retráctil</text></svg>',
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23000"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Motor SKYACTIV</text></svg>',
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23333"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Cockpit Deportivo</text></svg>',
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%236366f1"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Transmisión Manual</text></svg>'
        ],
        'caracteristicas': [
            'Techo retráctil rígido RF',
            'Motor SKYACTIV-G 2.0L',
            'Transmisión manual 6 vel.',
            'Suspensión deportiva',
            'Sistema BOSE premium',
            'Control de estabilidad'
        ]
    },
    # TOYOTA COROLLA HYBRID 2022
    {
        'id': 7,
        'marca': 'Toyota',
        'modelo': 'Corolla Hybrid LE 2022',
        'año': 2022,
        'precio': 28100,
        'kilometraje': 5800,
        'descripcion': 'Toyota Corolla Hybrid LE 2022 - Eficiencia máxima con más de 50 MPG, tecnología híbrida avanzada y emisiones ultra bajas.',
        'imagen': 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%2306b6d4"/><text x="400" y="240" font-family="Arial" font-size="20" font-weight="bold" text-anchor="middle" fill="white">COROLLA HYBRID 2022</text></svg>',
        'imagenes': [
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%2306b6d4"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Sistema Híbrido</text></svg>',
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23000"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Eficiencia 50+ MPG</text></svg>',
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23333"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Display Eco</text></svg>',
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%236366f1"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Carga Regenerativa</text></svg>'
        ],
        'caracteristicas': [
            'Sistema híbrido Toyota',
            '50+ MPG combinado',
            'Emisiones ultra bajas',
            'Display de eficiencia',
            'Carga regenerativa',
            'Modo EV disponible'
        ]
    },
    # MAZDA 6 SIGNATURE 2022
    {
        'id': 8,
        'marca': 'Mazda',
        'modelo': 'Mazda 6 Signature 2022',
        'año': 2022,
        'precio': 38900,
        'kilometraje': 4200,
        'descripcion': 'Mazda 6 Signature 2022 - Sedán premium con motor turbo, acabados Signature de lujo y tecnología de vanguardia. Elegancia máxima.',
        'imagen': 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23374151"/><text x="400" y="240" font-family="Arial" font-size="20" font-weight="bold" text-anchor="middle" fill="white">MAZDA 6 SIGNATURE 2022</text></svg>',
        'imagenes': [
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23374151"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Acabados Signature</text></svg>',
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23000"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Motor Turbo</text></svg>',
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%23333"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">Cuero Nappa</text></svg>',
            'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="800" height="480" viewBox="0 0 800 480"><rect width="800" height="480" fill="%236366f1"/><text x="400" y="240" font-family="Arial" font-size="20" text-anchor="middle" fill="white">BOSE Premium</text></svg>'
        ],
        'caracteristicas': [
            'Motor turbo SKYACTIV-G 2.5T',
            'Asientos de cuero Nappa',
            'Sistema BOSE premium',
            'Pantalla de 11.6 pulgadas',
            'Acabados de madera real',
            'AWD disponible'
        ]
    }
]