import pika
import json
import time
from math import radians, cos, sin, asin, sqrt

subscribers = {
    #Ciudad: (latitud, longitud)
    "Arica": (-18.4746, -70.2979),
    "Coquimbo": (-29.95332, -71.33947),
    "Valparaiso": (-33.036, -71.62963),
    "Concepcion": (-36.82699, -73.04977),
    "Punta Arenas": (-53.16282, -70.90922),
}

# Formula de Haversine para calcular distancia entre sismos y ciudades
def haversine(lon1, lat1, lon2, lat2):
    # Convertir grados decimales a radianes
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Fórmula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    
    # Radio de la Tierra en kilómetros
    r = 6371 
    
    return c * r
