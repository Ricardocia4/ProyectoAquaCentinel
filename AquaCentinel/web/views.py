from django.shortcuts import render


def inicio(request):
    # Nota que ahora incluimos "web/" en la ruta del template
    return render(request, "web/index.html")


# esta es la funcion de las boyas para la api activa pero no se usa odavia y no se va usar por ahora


def dashboard(request):
    return render(request, "web/dashboard.html")  # O la que quieras de inicio


def mis_boyas(request):
    return render(request, "web/mis_boyas.html")


def detalle_boya(request):
    return render(request, "web/detalle_boya.html")


# Vistas de invitado (Login/Register)
def login_view(request):
    return render(request, "web/login.html")  # Asegúrate de que el nombre coincida
