import requests
# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Definir la consulta GraphQL simple
query_lista = """
{
        plantas{
            id
            nombre
            especie
            edad
            altura
            frutos
        }
    }
"""
# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query_lista})
print(response.text)
