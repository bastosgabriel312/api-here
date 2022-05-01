# api-here

## Tecnologias utilizadas (Docs)
  * Python 3 (https://docs.python.org/3.8/)
  * API Here (https://developer.here.com/documentation)
  * Geopy (https://geopy.readthedocs.io/en/stable/)
  * Flask (https://flask.palletsprojects.com/)
  

## Here
### API de mapas utilizados para navegação.

## Geopy
### Foi utilizado para realizar a pesquisa com palavras chaves e retornar a latitude e longitude
``` 
loc = Nominatim(user_agent="GetLoc") 
getLoc = loc.geocode(palavraChave)
getLoc.latitude
getLoc.longitude
```
