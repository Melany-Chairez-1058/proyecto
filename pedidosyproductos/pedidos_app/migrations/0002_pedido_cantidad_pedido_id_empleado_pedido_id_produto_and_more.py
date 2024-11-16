# Generated by Django 5.1.2 on 2024-11-15 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pedido',
            name='id_empleado',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pedido',
            name='id_producto',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='id_cliente',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]