import json
import os

def obtener_datos_mapa():
    ruta = os.path.join(os.path.dirname(__file__), '../../data/mapa.json')
    with open(ruta, 'r') as archivo:
        return json.load(archivo)
