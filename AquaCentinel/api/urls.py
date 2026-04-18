from django.urls import path
from . import views

app_name = "api"
urlpatterns = [
    path("boyas", views.boyas),
    path("mis-boyas", views.misBoyas, name="misBoyas"),
    path("mis-boyas/descripcion", views.boyaDescripcion, name="boyaDescripcion"),
    path("mis-boyas/<str:id>", views.misBoyas, name="miBoya"),
    path("sensores", views.registroDeSensores, name="sensores"),
    # path("boya/diagnostico/<str:id>", views.diagnostico, name="diagnostico"),
    path("boya/info/<str:id>", views.show, name="show"),
    path("boya/<int:id>/detalles", views.detalles, name="detalles"),
    # path("boya/<str:id>/info", views.info, name="info"),
    path("boya/<str:id>/historico", views.historico, name="historico"),
    # path("boya/<str:id>/registros-recientes", views.infoReciente, name="registrosRecientes"),
    path("boya/<str:id>/ultimo-registro", views.ultimoRegistro, name="ultimoRegistro"),
    path("dashboard/", views.dashboard_data, name="dashboard_data"),
]
