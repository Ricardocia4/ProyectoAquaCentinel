from django.urls import path
from . import views


# El "apodo" de la app para usar {% url 'web:nombre' %}
app_name = "web"

urlpatterns = [
    # 1. El INDEX (La raíz)
    path("", views.inicio, name="index"),
    # 2. El DASHBOARD
    path("dashboard/", views.dashboard, name="dashboard"),
    # 3. LAS BOYAS
    path("mis-boyas/", views.mis_boyas, name="mis_boyas"),
    # 4. EL DETALLE
    path("boya-detalle/", views.detalle_boya, name="detalle_boya"),
]
