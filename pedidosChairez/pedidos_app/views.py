from django.shortcuts import render,redirect
from .models import Pedido
# Create your views here.
1
def inicio_vista(request):
    lospedidos=Pedido.objects.all()
    return render(request,'gestionarPedido.html',{'mispedidos':lospedidos})
    

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
    Pedidos=Pedido.objects.get(id_pedido=id_pedido)
    return render(request,'editarPedido.html',{'mispedidos':Pedidos})

def editarPedido(request):
    id_pedido=request.POST["txtidped"]
    id_cliente =request.POST["txtidcli"]
    fecha_pedido=request.POST["txtfechped"]
    fecha_entrega=request.POST["txtfechent"]
    total_pedido=request.POST["txttotal"]
    estado_pedido=request.POST["txtesta"]
    metodo_pago=request.POST["txtmetodop"]
    Pedidos=Pedido.objects.get(id_pedido=id_pedido)
    Pedidos.id_pedido=id_pedido 
    Pedidos.id_cliente=id_cliente
    Pedidos.fecha_pedido=fecha_pedido
    Pedidos.fecha_entrega=fecha_entrega
    Pedidos.total_pedido=total_pedido
    Pedidos.estado_pedido=estado_pedido
    Pedidos.metodo_pago=metodo_pago
    
    Pedidos.save()
    return redirect('/')
    

def borrarPedido(request,id_pedido):
    Pedidos=Pedido.objects.get(id_pedido=id_pedido)
    Pedidos.delete()
    return redirect('/')