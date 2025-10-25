import requests

url = "https://jsonplaceholder.typicode.com/users"

respuesta = requests.get(url)

if respuesta.status_code == 200:
    users = respuesta.json()
    for user in users:
        print(user["name"])
else:
    print("El servidor no respondio", respuesta.status_code)
    