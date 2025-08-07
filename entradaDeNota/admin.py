
from django.contrib import admin
from .models import Proyecto, Autor, Asesor

class AutorInline(admin.TabularInline):  # También puedes usar StackedInline
    model = Autor
    extra = 1  # Número de formularios vacíos que se mostrarán

class AsesorInline(admin.TabularInline):
    model = Asesor
    extra = 1

class ProyectoAdmin(admin.ModelAdmin):
    inlines = [AutorInline, AsesorInline]

admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Autor)
admin.site.register(Asesor)
