from fastapi import FastAPI

"""
- Sismos reales de sismologia.cl
- Fecha en hora local
"""
sismos = {
    #sismo en Pichidangui, le interesa a valpo
    1: {
        "id": 1,
        "ref": "6 KM al NE de Pichidangui",
        "lat": -32.09,
        "lon": -71.50,
        "profundidad": 34,
        "magnitud": 3.2,
        "fecha": "2026-09-28 00:55:33",
    },
    #sismo en Tocopilla, le interesa a arica
    2: {
        "id": 2,
        "ref": "17 KM al O de Tocopilla",
        "lat": -22.14,
        "lon": -70.36,
        "profundidad": 34,
        "magnitud": 2.7,
        "fecha": "2026-09-28 01:38:11",
    },
    #sismo en Chaiten, no le interesa a nadie +500KM de P.Arenas y Concepción
    3: {
        "id": 3,
        "ref": "17 KM al S de Chaiten",
        "lat": -43.07,
        "lon": -72.69,
        "profundidad": 8,
        "magnitud": 4.6,
        "fecha": "2026-09-27 15:55:43",
    },
}


app = FastAPI()

@app.get("/sismos/{id}")
def get_sismo(id: int):
    try:
        return sismos[id]
    except KeyError:
        return {"error": "Sismo no encontrado"}