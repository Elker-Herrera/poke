#
#API ---> Interfaz de programacion de aplicacion
# Reglas, punto partida, endpoints
# Metodos HTTP, crud
# Get ---> Obtener
# SOAP --> XML
# Reset --> JSON
# Response --> Respuesta 
# Requests --> Solicitar

import requests 
import json

url = "https://dog.ceo/api/breeds/image/random"

response = requests.get(url)

data = json.loads(response.content)

print(data)