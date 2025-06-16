from flask import Blueprint, request, jsonify
from .dijkstra import calcular_ruta

rutas_bp = Blueprint('rutas', __name__)

@rutas_bp.route('/api/ruta', methods=['POST'])
def ruta():
    data = request.get_json()
    origen = data.get('origen')
    destino = data.get('destino')
    medio = data.get('medio')
    clima = data.get('clima')
    gasolina = data.get('gasolina')

    resultado = calcular_ruta(origen, destino, medio, clima, gasolina)
    return jsonify(resultado)
