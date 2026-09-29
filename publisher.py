import pika
import json
import time
from main import sismos

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='sismos', exchange_type='fanout')

def publicar_sismo(id, lat, lon):
    mensaje = {
        "id": id,
        "lat": lat,
        "lon": lon,
    }
    channel.basic_publish(exchange='sismos', routing_key='', body=json.dumps(mensaje))
    print(f" [x] Sent {mensaje}")

#Publica todos los sismos definidos en main.py
for sismo in sismos.values():
    publicar_sismo(sismo["id"], sismo["lat"], sismo["lon"])

connection.close()