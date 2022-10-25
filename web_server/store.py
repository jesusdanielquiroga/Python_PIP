import requests

def get_categories():
    r= requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code) #Devuelve el estado de la petición
    print(r.text) #trae la información a consumir en un string
    categories=r.json() #transforma a json que podemos iterar o transformar
    for category in categories:
        print(category['name'])
