import requests
import time
import random
import json

url = 'http://127.0.0.1:8000/api/sensores'

for i in range(15):
    try:
        datos = {
            "boya": 1,
            "ph": random.uniform(0, 14),
            "temperatura": random.uniform(0, 50),
            "conductividad": random.uniform(0, 1000),
            "turbidez": random.uniform(0, 20)
        }

        response = requests.post(url, json=datos)
        
        print(f"Intento {i+1}: Status {response.status_code}")
        print(response.json())
        
        time.sleep(90)
        
    except requests.exceptions.RequestException as e:
        print(f"Error en intento {i+1}: {e}")

print("Proceso finalizado.")
