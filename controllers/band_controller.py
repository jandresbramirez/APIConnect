from flask import Blueprint

band_bp = Blueprint('band_bp',__name__)

@band_bp.route('/bands', methods=['GET'])
def saludo():
    print("Hola")

@band_bp.route('/bands/<int:band_id>', methods=['GET'])
def saludo():
    print("Hola")

@band_bp.route('/bands', methods=['POST'])
def saludo():
    print("Hola")

@band_bp.route('/bands/<int:band_id>', methods=['PUT'])
def saludo():
    print("Hola")
    
@band_bp.route('/bands/<int:band_id>', methods=['DELETE'])
def saludo():
    print("Hola")