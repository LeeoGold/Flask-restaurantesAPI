from flask import Blueprint, jsonify, request

courses_bp = Blueprint("courses", __name__)

# Listar cursos
@courses_bp.route('/courses', methods=['GET'])
def list_courses():
    return jsonify({
        "items": [
            {"id": "c1", "title": "Introducción a Flask"},
            {"id": "c2", "title": "APIs REST con Python"}
        ],
        "total": 2
    })

# Obtener curso por ID
@courses_bp.route('/courses/<course_id>', methods=['GET'])
def get_course(course_id):
    return jsonify({
        "id": course_id,
        "title": "Curso de ejemplo",
        "description": "Contenido del curso aquí"
    })
