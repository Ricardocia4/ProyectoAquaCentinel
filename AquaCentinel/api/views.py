import json
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import RegistroSensor, Boya
from django.forms.models import model_to_dict

# Estos imports son para los sockets
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Se incluyen los formularios que serán usados como el "validator" de Laravel
from .forms import BoyaForm, RegistroSensorForm
from django.views.decorators.csrf import (
    csrf_exempt,
)  # Solo para pruebas. Eliminar en producción y todas sus invocaciones.


@csrf_exempt
def misBoyas(request):
    # Este endpoint retorna todas las boyas vinculadas del usuario 
    if request.method == "GET":
        print(f"usuario: {request.user.id}")
        try:
            boyas = list(Boya.objects.filter(usuario=request.user.id).values("id", "codigo_boya", "descripcion"))
            print(boyas)
            
            for i in range(len(boyas)):
                try:
                    registro = traerUltimoRegistro(boyas[i]["id"])
                    boyas[i]["registro"] = model_to_dict(registro)
                except Exception:
                    boyas[i]["registro"] = []

            return JsonResponse(boyas, safe=False)

        except Boya.DoesNotExist:
            return JsonResponse({"success": False, "message": "No existen boyas vinculadas a este usuario."})
        
        except Exception as e:
            print(f"error: {e}")
            return JsonResponse({"success": False, "message": "Algo salió mal"}, status=500)
            
    if request.method == "POST":
        boya = None
        codigo_boya = request.POST.get('codigo_boya')

        try:
            boya = Boya.objects.get(codigo_boya=codigo_boya)

        except Boya.DoesNotExist:
            return JsonResponse(
                {"success": False, "message": "El código no corresponde a ninguna boya"},
                status=404,
            )
        except Exception as e:
            print(f"error: {e}")
            return JsonResponse({"success": False, "message": "Algo salió mal"}, status=500)
        
    print(f"Usuario : {boya.usuario}")

    if boya.usuario is not None:
        return JsonResponse({"success": False, "message": "Esta boya ya está vinculada a un usuario."}, status=409)
    

    try:
        boya.usuario = request.user
        boya.save()
        return JsonResponse({"success": True, "message": "Boya vinculada con éxito"})
    except Exception as e:
        print(f"error: {e}")
        return JsonResponse({"success": False, "message": "Algo salió mal"}, status=500)

@csrf_exempt
def info(request, id):
    try:
        boya = model_to_dict(Boya.objects.get(id=id))
        print(boya)
        return JsonResponse(boya, safe=False)

    except Boya.DoesNotExist:
        return JsonResponse({"success": False, "message": "No existe una boya con este ID."})
    
    except Exception as e:
        print(f"error: {e}")
        return JsonResponse({"success": False, "message": "Algo salió mal"}, status=500)

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
                # Aquí se hace un "emit"
                data["fecha_creacion"] = f"{registro.fecha_creacion}"
                channel_layer = get_channel_layer()

                async_to_sync(channel_layer.group_send)(
                    f'{data["boya"]}',  # Nombre del grupo (ID de boya)
                    {
                        'type': 'send_new_data', # Nombre del método en el consumidor
                        'data': data,
                    }
                )


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
    
    return JsonResponse(data, safe=False)
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
def infoReciente(request, id):
    data = list(
        RegistroSensor.objects.filter(boya=id)
        .values("ph", "turbidez", "temperatura", "conductividad", "fecha_creacion")
        .order_by("-fecha_creacion")
        [:15]
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
    print(ph)
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
            "fecha_creacion": registro.fecha_creacion,
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
