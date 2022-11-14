from django.contrib import admin
from recetario.models import Receta, Comentario
# Register your models here.
@admin.register(Receta)
class ConferenciaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'ingredientes', 'preparacion', 'imagen', 'fecha_creacion', 'usuario']
    
@admin.register(Comentario)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['receta', 'contenido']
 