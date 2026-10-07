# Tarea 1 INF-326

*Simulación de notificación y solicitud de información de sismos usando el patrón arquitectonico publish-subscribe implementado con RabbitMQ y FastAPI*

Por: Badir Villegas 202273020-K

## Instalación y ejecución

- Instalar dependencias de requirements.txt

### Ejecutar los scripts en distintas consolas siguiendo este orden:

1. `uvicorn main:app --reload` → Correr el servicio HTTP y la información completa de los sismos
2. En consolas distintas, un subscriber por ciudad:
   - `python subscriber_arica.py`
   - `python subscriber_coquimbo.py`
   - `python subscriber_valparaiso.py`
   - `python subscriber_concepcion.py`
   - `python subscriber_punta_arenas.py`
3. `python publisher.py` → Enviar los sismos pre-configurados con Exchange tipo *fanout*

## Fuentes

- [https://www.rabbitmq.com/tutorials](https://www.rabbitmq.com/tutorials)
- [https://sismologia.cl/](https://sismologia.cl/)

