from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class vendedor(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    numero_empleado= models.IntegerField()
    
class venta(models.Model):
    fecha= models.DateField() 
    monto= models.FloatField()
    numero_vendedor= models.IntegerField()

class cliente(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    numero_cliente= models.IntegerField()

class avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"

