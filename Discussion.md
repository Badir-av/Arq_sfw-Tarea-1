# Trade-offs

- ### Exchange fanout: 
Se usó este ya que en terminos de esta tarea, no hay tantos subscribers por lo tanto basta con enviarles a todos tipo broadcast el aviso, **pero** todos deben gestionar si el sismo les es de importancia o no

- ### Filtro Haversine en el subscriber:
La lógica y complejidad es simple **pero** cada subscriber procesa todos los sismos aun que ignore la mayoría

- ### Cola exclusive temporal:
Fácil para probar y ejecutar repetidas veces **pero** si un susbscriber se cae no se guardará ningún mensaje y se perderá

# Back of the envelope

En esta tarea se usó un espacio muy acotado (5 ciudades y 3 sismos a la vez) pero en la realidad existen muchas más ciudades y, en promedio se perciben aproximadamente  20 sismos al día.

- Para N ciudades se tendría que hacer un calculo de distancia `N * sismo` al mismo tiempo

- Calcular un Haversine es barato pero ¿cuantos por segundo podría soportar?

- Si se configuró una distancia de 500 km para considerarse sismo de interes, para cada ciudad ¿qué porcentaje del total de sismos le importan?

- ¿Cúal sería la latencia en un sistema real dada la serie publicar → cola → callback → GET /sismos/{id}?