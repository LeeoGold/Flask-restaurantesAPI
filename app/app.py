from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ping raíz para evitar 404 en "/"
@app.route('/', methods=['GET'])
def root():
    return jsonify({"ok": True, "msg": "API Restaurantes viva"}), 200

# Base de datos simulada
restaurants = [
    {"id": 1, "name": "La Parrilla", "city": "Madrid"},
    {"id": 2, "name": "Sushi House", "city": "Barcelona"},
    {"id": 3, "name": "Pasta Paradise", "city": "Valencia"}
]

menus = {
    1: [
        {"id": 1, "name": "Hamburguesa", "price": 10.50},
        {"id": 2, "name": "Ensalada César", "price": 8.00}
    ],
    2: [
        {"id": 1, "name": "Sushi Roll", "price": 12.00},
        {"id": 2, "name": "Sashimi", "price": 15.50}
    ],
    3: []  # opcional: para que /3/menu no esté vacío
}

# 1) GET /api/restaurants
@app.route('/api/restaurants', methods=['GET'])
def get_restaurants():
    return jsonify(restaurants), 200

# 2) GET /api/restaurants/<id>
@app.route('/api/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = next((r for r in restaurants if r['id'] == id), None)
    if restaurant:
        return jsonify(restaurant), 200
    return jsonify({"error": "Restaurante no encontrado"}), 404

# 3) GET /api/restaurants/<id>/menu
@app.route('/api/restaurants/<int:id>/menu', methods=['GET'])
def get_restaurant_menu(id):
    menu = menus.get(id, [])
    return jsonify(menu), 200

# 4) POST /api/restaurants/<id>/menu/items
@app.route('/api/restaurants/<int:id>/menu/items', methods=['POST'])
def add_menu_item(id):
    if id not in menus:
        return jsonify({"error": "Restaurante no encontrado"}), 404

    new_item = request.get_json()
    if not new_item or 'name' not in new_item or 'price' not in new_item:
        return jsonify({"error": "Datos inválidos. Se requieren 'name' y 'price'"}), 400

    new_id = (max([item['id'] for item in menus[id]], default=0) + 1)
    new_item['id'] = new_id
    menus[id].append(new_item)
    return jsonify(new_item), 201

# Endpoint 5: Crear restaurante esto es nuevo chivcos quye bueno lo intente :p
@app.route('/api/restaurants', methods=['POST'])
def create_restaurant():
    new_rest = request.get_json()

    # Validaciones
    if not new_rest or 'id' not in new_rest or 'name' not in new_rest or 'city' not in new_rest:
        return jsonify({"error": "Datos inválidos. Se requieren 'id', 'name' y 'city'"}), 400
    
    # Validar ID único
    if any(r['id'] == new_rest['id'] for r in restaurants):
        return jsonify({"error": "El ID ya existe. Debe ser único"}), 400

    restaurants.append(new_rest)
    menus[new_rest['id']] = []  # Crear menú vacío para el nuevo restaurante
    return jsonify(new_rest), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)