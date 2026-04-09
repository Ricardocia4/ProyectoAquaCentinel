import json
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import RegistroSensor

# Se incluyen los formularios que serán usados como el "validator" de Laravel
from .forms import BoyaForm, RegistroSensorForm
from django.views.decorators.csrf import (
    csrf_exempt,
)  # Solo para pruebas. Eliminar en producción y todas sus invocaciones.


# def inicio(request):
#     return render(request, "index.html")


@csrf_exempt
def boyas(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = BoyaForm(data)
        if form.is_valid():
            try:
                boya = form.save()
                return JsonResponse(
                    {
                        "success": True,
                    },
                    status=200,
                )
            except Exception as e:
                print(f"Error: {e}")
                return JsonResponse(
                    {"success": False, "message": "Algo salió mal"}, status=500
                )
        else:

            return JsonResponse(
                {
                    "success": False,
                    "errors": form.errors,  # form.errors se convierte a dict JSON
                },
                status=400,
            )

    return JsonResponse({"success": False, "message": "Método no válido"}, status=400)


@csrf_exempt
def registroDeSensores(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = RegistroSensorForm(data)
        if form.is_valid():
            try:
                registro = form.save()
                return JsonResponse(
                    {
                        "success": True,
                    },
                    status=200,
                )
            except Exception as e:
                print(f"Error: {e}")
                return JsonResponse(
                    {"success": False, "message": "Algo salió mal"}, status=500
                )
        else:

            return JsonResponse(
                {
                    "success": False,
                    "errors": form.errors,  # form.errors se convierte a dict JSON
                },
                status=400,
            )

    return JsonResponse({"success": False, "message": "Método no válido"}, status=400)


@csrf_exempt
def historico(request, id):
    data = list(
        RegistroSensor.objects.filter(boya=id)
        .values("ph", "turbidez", "temperatura", "conductividad", "fecha_creacion")
        .order_by("-fecha_creacion")
    )
    if not data:
        return JsonResponse(
            {"success": False, "message": "No se encontraron registros para esta boya"},
            status=404,
        )
    ph, temp, turb, conduc, fecha = [], [], [], [], []
    for d in data:
        ph.append(d["ph"])
        temp.append(d["temperatura"])
        turb.append(d["turbidez"])
        conduc.append(d["conductividad"])
        fecha.append(d["fecha_creacion"])

    return JsonResponse(
        {
            "ph": ph,
            "conductividad": conduc,
            "temperatura": temp,
            "turbidez": turb,
            "fecha_creacion": fecha,
        },
        safe=False,
    )


@csrf_exempt
def show(request, id):
    try:
        registro = traerUltimoRegistro(id)
        return JsonResponse(
            {
                "message": "Últimos registros de la boya",
                "data": {
                    "ph": registro.ph,
                    "conductividad": registro.conductividad,
                    "temperatura": registro.temperatura,
                    "turbidez": registro.turbidez,
                },
            },
        )
    except RegistroSensor.DoesNotExist:
        return JsonResponse(
            {"success": False, "message": "No se encontraron registros para esta boya"},
            status=404,
        )
    except Exception as e:
        print(f"error: {e}")
        return JsonResponse({"success": False, "message": "Algo salió mal"}, status=500)


@csrf_exempt
def ultimoRegistro(request, id):
    try:
        registro = traerUltimoRegistro(id)
        return JsonResponse(
            {
                "ph": registro.ph,
                "conductividad": registro.conductividad,
                "temperatura": registro.temperatura,
                "turbidez": registro.turbidez,
            }
        )
    except RegistroSensor.DoesNotExist:
        return JsonResponse(
            {"success": False, "message": "No se encontraron registros para esta boya"},
            status=404,
        )
    except Exception as e:
        print(f"error: {e}")
        return JsonResponse({"success": False, "message": "Algo salió mal"}, status=500)


@csrf_exempt
def diagnostico(request, id):
    try:
        registro = traerUltimoRegistro(id)

        scorep_ph = scorePh(registro.ph)
        score_temp = scoreTemperature(registro.temperatura)
        score_turb = scoreTurbity(registro.turbidez)
        score_conduc = scoreConductivity(registro.conductividad)

        score = scorep_ph + score_temp + score_turb + score_conduc
        estado, recomendacion = diagnostic(score)
        data = {
            "parametros": {
                "ph": {"valor": registro.ph, "score": scorep_ph},
                "temperatura": {"valor": registro.temperatura, "score": score_temp},
                "turbidez": {"valor": registro.turbidez, "score": score_turb},
                "conductividad": {
                    "valor": registro.conductividad,
                    "score": score_conduc,
                },
            },
            "puntaje_total": score,
            "estado": estado,
            "recomendacion": recomendacion,
        }
        return JsonResponse(data)
    except RegistroSensor.DoesNotExist:
        return JsonResponse(
            {"success": False, "message": "No se encontraron registros para esta boya"},
            status=404,
        )
    except Exception as e:
        print(f"error: {e}")
        return JsonResponse({"success": False, "message": "Algo salió mal"}, status=500)


def scorePh(ph):
    if ph >= 6.5 and ph <= 8.5:
        return 0
    if ph >= 6.0 and ph <= 9:
        return 1
    return 2


def scoreConductivity(c):
    if c <= 500:
        return 0
    if c <= 1500:
        return 1
    return 2


def scoreTurbity(t):
    if t <= 1:
        return 0
    if t <= 5:
        return 1
    return 2


def scoreTemperature(t):
    if t >= 15 and t <= 25:
        return 0
    if t >= 10 and t <= 30:
        return 1
    return 2


def diagnostic(score):
    if score <= 2:
        return "Bueno", "No requiere mantenimiento"
    if score <= 5:
        return "Regular", "Requiere mantenimiento"
    if score <= 7:
        return "Malo", "Requiere tratamiento químico"
    return "Malo", "Requiere estudio bacteriológico"


def traerUltimoRegistro(id):
    return RegistroSensor.objects.filter(boya=id).latest("fecha_creacion")
