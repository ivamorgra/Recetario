from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    ingredientes = models.TextField(max_length=5000)
    preparacion = models.TextField(max_length=5000)
    imagen = models.ImageField(upload_to='recetas', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    
    contenido = models.TextField()
    
    def __str__(self):
        return self.contenido

