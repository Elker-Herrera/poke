import requests 
import json

print("digita el nombre del pokemon que quieres elegir")
pokemon = input()
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
respuesta = requests.get(url)
poke = json.loads(respuesta.content)
print("Nombre:",poke["name"])
