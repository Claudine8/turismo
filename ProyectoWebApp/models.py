from django.db import models
from django.contrib.auth.models import AbstractUser, User





class Categorias(models.Model):
    categoria = models. CharField(max_length=64, null=False)

    def __str__(self):
        return f"{self.categoria}"

class Productos(models.Model):
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE,
related_name="clasificacion_seccion")
    fecha_creacion = models.DateTimeField(auto_now_add= True)
    titulo = models.CharField(max_length=2000, null=False)
    descripcion = models.CharField(max_length=2000, null=False)
    imagen = models.ImageField(upload_to="productos", blank=True, null=True)
    precio = models.IntegerField()
    precio_oferta = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario")
    subtotal = models.IntegerField(default=0)

    

