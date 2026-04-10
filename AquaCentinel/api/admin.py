from django.contrib import admin
from .models import Boya


@admin.register(Boya)
class BoyaAdmin(admin.ModelAdmin):
    # 1. Definimos qué columnas ver en la tabla principal
    list_display = ("codigo_boya", "usuario")

    # 2. Excluimos 'usuario' del formulario para que no aparezca
    exclude = ("usuario",)

    # 3. Hacemos que el código sea visible pero no editable en el detalle
    readonly_fields = ("codigo_boya",)
