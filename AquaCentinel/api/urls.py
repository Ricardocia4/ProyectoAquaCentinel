from django.urls import path
from . import views

app_name = "sensores"
urlpatterns = [
    path("boyas", views.boyas),
    path("sensores", views.registroDeSensores, name="sensores"),
    path("boya/diagnostico/<str:id>", views.diagnostico, name="diagnostico"),
    path("boya/info/<str:id>", views.show, name="show"),
    path("boya/<str:id>/historico", views.historico, name="historico"),
    path("boya/<str:id>/ultimo-registro", views.ultimoRegistro, name="ultimoRegistro"),
]
