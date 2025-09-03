import requests

BASE_URL = "http://127.0.0.1:5000"

# 1) Probar endpoint raíz
r = requests.get(f"{BASE_URL}/")
print("Root:", r.json())

# 2) Listar restaurantes
r = requests.get(f"{BASE_URL}/api/restaurants")
print("Restaurantes:", r.json())

# 3) Obtener restaurante por ID
r = requests.get(f"{BASE_URL}/api/restaurants/1")
print("Restaurante 1:", r.json())

# 4) Obtener menú de un restaurante
r = requests.get(f"{BASE_URL}/api/restaurants/1/menu")
print("Menú Restaurante 1:", r.json())

# 5) Agregar un nuevo ítem al menú
nuevo_item = {"name": "Pizza Margarita", "price": 9.99}
r = requests.post(f"{BASE_URL}/api/restaurants/1/menu/items", json=nuevo_item)
print("Nuevo item creado:", r.json())
