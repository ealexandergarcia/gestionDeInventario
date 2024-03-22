import requests

# URL del servidor json-server
url = 'http://localhost:3000/activos/1'

# Enviar solicitud GET al servidor
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()

    # Verificar si existe la clave 'historialActivos' en los datos
    if 'historialActivos' in data:
        # Obtener los datos del historialActivos
        historial_activos = data['historialActivos']

        # Imprimir los datos del historialActivos
        print(historial_activos)
    else:
        print("No se encontraron datos en historialActivos")
else:
    # Si la solicitud no fue exitosa, imprimir el código de estado
    print("Error:", response.status_code)


#que lo que mmguevo 