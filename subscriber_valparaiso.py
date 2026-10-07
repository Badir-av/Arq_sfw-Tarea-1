import pika
import json
import requests
from math import trunc
from math import radians, cos, sin, asin, sqrt

ciudad = "Valparaiso"
ciudad_lat, ciudad_lon = -33.036, -71.62963

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

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.exchange_declare(exchange="sismos", exchange_type="fanout")

result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange="sismos", queue=queue_name)

def callback(ch, method, properties, body):
    data_sismos = json.loads(body)
    sismo_id = data_sismos["id"]
    sismo_lat = data_sismos["lat"]
    sismo_lon = data_sismos["lon"]

    distancia = trunc(haversine(sismo_lon, sismo_lat, ciudad_lon, ciudad_lat))
    if distancia <= 500:
        detalle = requests.get(f"http://localhost:8000/sismos/{sismo_id}").json()
        print(ciudad + " a " + str(distancia) + "KM solicita el detalle del sismo")
        print(detalle)
        print("--------------------------------")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
print(" [*] Esperando sismos...")
channel.start_consuming()
