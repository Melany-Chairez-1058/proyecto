from django.shortcuts import render, redirect
from .models import Producto
# Create your views here.

def inicio_vista(request):
    lospedidos=Producto.objects.all()
    return render(request,'gestionarPedido.html',{'mispedidos':lospedidos})
    