from flask import Blueprint, jsonify, request

payments_bp = Blueprint("payments", __name__)

# Iniciar pago
@payments_bp.route('/payments/checkout', methods=['POST'])
def checkout():
    data = request.json
    return jsonify({
        "paymentId": "p789",
        "courseId": data.get("courseId"),
        "status": "pending"
    }), 200

# Confirmar pago
@payments_bp.route('/payments/confirm', methods=['POST'])
def confirm():
    data = request.json
    return jsonify({
        "paymentId": data.get("paymentId"),
        "status": "success",
        "message": "Pago confirmado correctamente"
    }), 200
