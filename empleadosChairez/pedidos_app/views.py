from django.shortcuts import render,redirect
from .models import Pedido
# Create your views here.

def inicio_vista(request):
    lospedidos=Pedido.objects.all()
    return render(request,'gestionarPedidos.html',{'mispedidos':lospedidos})
    

def registrarPedido(request):
    
    id_pedido=request.POST["txtidped"]
    id_cliente =request.POST["txtidcli"]
    fecha_pedido=request.POST["txtfechped"]
    fecha_entrega=request.POST["txtfechent"]
    total_pedido=request.POST["txttotal"]
    estado_pedido=request.POST["txtesta"]
    metodo_pago=request.POST["txtmetodop"]


    guardarPedido=Pedido.objects.create( id_pedido=id_pedido, id_cliente= id_cliente,fecha_pedido= fecha_pedido,fecha_entrega=fecha_entrega,total_pedido=total_pedido,estado_pedido=estado_pedido,metodo_pago=metodo_pago)
    return redirect('/')

def seleccionarPedido(request,id_pedido):
    Pedido=Pedido.objects.get(id_pedido=id_pedido)
    return render(request,'editarPedido.html',{'mispedidoss':Pedido})

def editarMateria(request):
    id_pedido=request.POST["txtidped"]
    id_cliente =request.POST["txtidcli"]
    fecha_pedido=request.POST["txtfechped"]
    fecha_entrega=request.POST["txtfechent"]
    total_pedido=request.POST["txttotal"]
    estado_pedido=request.POST["txtesta"]
    metodo_pago=request.POST["txtmetodop"]
    Pedido=Pedido.objects.get(id_pedido=id_pedido)
    Pedido.id_pedido=id_pedido 
    Pedido.id_cliente=id_cliente
    Pedido.fecha_pedido=fecha_pedido
    
    Pedido.save()
    return redirect('/')
    

def borrarMateria(request,codigo):
    materia=Materia.objects.get(codigo=codigo)
    materia.delete()
    return redirect('/')