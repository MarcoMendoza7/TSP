import networkx as nx
from .grafo import construir_grafo

def calcular_ruta(origen, destino, medio_transporte, clima, precio_gasolina):
    G = construir_grafo()

    VELOCIDAD_BASE = {
        "auto": 80,
        "bici": 20,
        "caminando": 5
    }

    FACTOR_CLIMA = {
        "soleado": 1.0,
        "nublado": 0.85,
        "lluvioso": 0.7
    }

    try:
        ruta = nx.dijkstra_path(G, origen, destino, weight='weight')
        distancia_total = sum(G[u][v]['weight'] for u, v in zip(ruta[:-1], ruta[1:]))

        velocidad_real = VELOCIDAD_BASE[medio_transporte] * FACTOR_CLIMA[clima]
        tiempo = distancia_total / velocidad_real
        costo = distancia_total * float(precio_gasolina)

        return {
            "ruta": ruta,
            "distancia_km": round(distancia_total, 2),
            "tiempo_horas": round(tiempo, 2),
            "costo_gasolina": round(costo, 2)
        }

    except Exception as e:
        return {"error": str(e)}
