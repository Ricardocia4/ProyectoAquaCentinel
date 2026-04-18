import requests
import time
import random

url = "http://127.0.0.1:8000/api/sensores"


def generar_datos_prueba():
    # Definimos casos posibles para estresar la lógica de diagnóstico
    caso = random.choices(
        ["ideal", "regular", "malo_turbidez", "critico_total"],
        weights=[30, 30, 30, 10],  # Probabilidades de cada caso
    )[0]

    if caso == "ideal":
        # Todo en rangos perfectos (Score 0)
        ph = random.uniform(6.8, 7.5)
        temp = random.uniform(18, 24)
        cond = random.uniform(100, 400)
        turb = random.uniform(0, 0.8)

    elif caso == "regular":
        # Algunos valores fuera de rango pero no críticos (Score 3-5)
        ph = random.uniform(6.0, 6.4)
        temp = random.uniform(26, 29)
        cond = random.uniform(600, 1200)
        turb = random.uniform(2, 4.5)

    elif caso == "malo_turbidez":
        # El caso que mencionaste: todo bien excepto turbidez alta
        ph = random.uniform(7.0, 7.4)
        temp = random.uniform(20, 22)
        cond = random.uniform(200, 400)
        turb = random.uniform(10, 25)  # Crítico (> 5 NTU)

    else:  # critico_total
        # Desastre total en todos los sensores
        ph = random.choice([2.0, 12.0])  # Muy ácido o muy alcalino
        temp = random.uniform(35, 45)
        cond = random.uniform(1600, 2500)
        turb = random.uniform(30, 50)

    return {
        "boya": 2,  # Asegúrate de que este ID exista en tu DB
        "ph": round(ph, 2),
        "temperatura": round(temp, 2),
        "conductividad": round(cond, 2),
        "turbidez": round(turb, 2),
    }


print("--- Iniciando simulación de AquaSentinel ---")

for i in range(15):
    try:
        datos = generar_datos_prueba()

        response = requests.post(url, json=datos)

        print(f"[{i+1}] Enviando datos: {datos}")

        if response.status_code == 200:
            print(f"✅ Éxito: {response.json()}")
        else:
            print(f"⚠️ Error {response.status_code}: {response.text}")

        # Reduje el tiempo a 5 segundos para que pruebes rápido,
        # pero cámbialo a 30 o 90 si prefieres.
        time.sleep(5)

    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")

print("--- Simulación finalizada ---")
