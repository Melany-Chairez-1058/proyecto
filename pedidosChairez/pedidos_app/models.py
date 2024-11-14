from django.db import models

# Create your models here.

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.PositiveSmallIntegerField()
    fecha_pedido=models.DateField(verbose_name="Fecha de Realizado",null=False,blank=False)
    fecha_entrega=models.DateField(verbose_name="Fecha de Entrega",null=False,blank=False)
    total_pedido=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Total del pedido")
    estado_pedido=models.CharField(max_length=50,verbose_name="Estado del pedido",null=False,blank=False)
    metodo_pago=models.CharField(max_length=50,verbose_name="Metodo de pago",null=False,blank=False)



    def __str__(self) :
        return self.id_cliente
    
