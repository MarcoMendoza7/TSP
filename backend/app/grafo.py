import networkx as nx
from geopy.distance import geodesic

CIUDADES = {
    "CDMX": (19.4326, -99.1332),
    "Toluca": (19.2826, -99.6557),
    "Puebla": (19.0413, -98.2062),
    "Querétaro": (20.5888, -100.3899),
    "Cuernavaca": (18.9186, -99.2345),
}

CONECTADAS = [
    ("CDMX", "Toluca"),
    ("CDMX", "Puebla"),
    ("CDMX", "Querétaro"),
    ("CDMX", "Cuernavaca"),
    ("Puebla", "Querétaro"),
    ("Toluca", "Cuernavaca"),
]

def construir_grafo():
    G = nx.Graph()
    for ciudad in CIUDADES:
        G.add_node(ciudad, pos=CIUDADES[ciudad])
    for origen, destino in CONECTADAS:
        coord_origen = CIUDADES[origen]
        coord_destino = CIUDADES[destino]
        distancia = geodesic(coord_origen, coord_destino).km
        G.add_edge(origen, destino, weight=distancia)
    return G
