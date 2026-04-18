from django.shortcuts import render
from django.shortcuts import redirect


def inicio(request):
    return render(request, "web/index.html")


def dashboard(request):
    if request.user.is_staff:
        # Si es admin, lo mandamos directo al CRUD de boyas en el panel
        return redirect("/admin/")
    return render(request, "web/dashboard.html")  # O la que quieras de inicio


def mis_boyas(request):
    return render(request, "web/mis_boyas.html")


def detalle_boya(request, id):
    datos = {  # Es un diccionario porque, si hace falta enviar más datos, no afectará la estructura de los demás.
        "id": id
    }
    return render(request, "web/detalle_boya.html", datos)


# Vistas de invitado (Login/Register)
def login_view(request):
    return render(request, "web/login.html")
