from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    precio=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Precio Producto")
    stock=models.IntegerField(default=0,verbose_name="Cantidad Stock")
    descripcion=models.CharField(max_length=100,verbose_name="Descripcion")
    tipo=models.CharField(max_length=50,verbose_name="Tipo")
    categoria=models.CharField(max_length=50,verbose_name="Categoria")
    nombre = models.CharField(max_length=50,verbose_name="Nombre")
    id_proveedor=models.PositiveSmallIntegerField(default=0)
    id_sucursal=models.PositiveSmallIntegerField(default=0)
