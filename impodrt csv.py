import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # Abre el archivo CSV
    with open(csv_file_path, 'r') as csv_file:
        # Lee el archivo CSV como un diccionario
        csv_reader = csv.DictReader(csv_file)
        
        # Convierte los datos del CSV a una lista de diccionarios
        data = [row for row in csv_reader]
        
        # Abre el archivo JSON y escribe los datos
        with open(json_file_path, 'w') as json_file:
            # Utiliza json.dump para escribir los datos en formato JSON
            json.dump(data, json_file, indent=2)

# Especifica las rutas de los archivos CSV y JSON
csv_path = 'ruta/del/archivo.csv'
json_path = 'ruta/del/archivo.json'

# Llama a la función para convertir el archivo CSV a JSON
csv_to_json(csv_path, json_path)

print(f'La conversión de {csv_path} a {json_path} ha sido completada.')
