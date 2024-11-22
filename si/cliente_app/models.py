from django.db import models

# Create your models here.
class Cliente(Models.Model):
    id_cliente=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50,verbose_name="Nombre")
    telefono=models.CharField(max_length=50,verbose_name="Telefono")
    direccion=models.CharField(max_length=50,verbose_name="direccion")