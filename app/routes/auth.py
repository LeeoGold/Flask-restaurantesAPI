from flask import Blueprint, jsonify, request

auth_bp = Blueprint("auth", __name__)

# Endpoint de registro
@auth_bp.route('/auth/register', methods=['POST'])
def register():
    data = request.json
    return jsonify({
        "userId": "u123",
        "email": data.get("email"),
        "message": "Usuario registrado con éxito"
    }), 201

# Endpoint de login
@auth_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    return jsonify({
        "token": "fake-jwt",
        "email": data.get("email")
    }), 200
