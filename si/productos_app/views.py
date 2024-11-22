from django.shortcuts import render, redirect
from .models import Producto
# Create your views here.

def inicio_vista(request):
    losproductos=Producto.objects.all()
    return render(request,'gestionarProducto.html',{'misproductos':losproductos})
    
def registrarProducto(request):
    id_producto=request.POST["idpro"]
    precio=request.POST["precio"]
    stock=request.POST["stock"]
    descripcion=request.POST["desc"]
    tipo=request.POST["tipo"]
    categoria=request.POST["cate"]
    nombre=request.POST["nombrepr"]
    id_proveedor =request.POST["idv"]
    id_sucursal= request.POST["ids"]
    guardarProducto=Producto.objects.create(id_producto=id_producto,precio=precio,stock=stock,descripcion=descripcion,tipo=tipo,categoria=categoria,nombre=nombre,id_proveedor=id_proveedor,id_sucursal=id_sucursal)
    return redirect('/')                                 


def seleccionarProducto(request,id_producto):
    Productos=Producto.objects.get(id_producto=id_producto)
    return render(request,'editarProducto.html',{'misproductos':Productos})


def editarProducto(request):
    id_producto=request.POST["idpro"]
    precio=request.POST["precio"]
    stock=request.POST["stock"]
    descripcion=request.POST["desc"]
    tipo=request.POST["tipo"]
    categoria=request.POST["cate"]
    nombre=request.POST["nombrepr"]
    id_proveedor =request.POST["idv"]
    id_sucursal= request.POST["ids"]
    Productos=Producto.objects.get(id_producto=id_producto)
    Productos.id_producto=id_producto 
    Productos.precio=precio
    Productos.stock=stock
    Productos.descripcion=descripcion
    Productos.tipo=tipo
    Productos.categoria=categoria
    Productos.nombre=nombre
    Productos.id_proveedor=id_proveedor
    Productos.id_sucursal=id_sucursal
    
    Productos.save()
    return redirect('/')
    

def borrarProducto(request,id_producto):
    Productos=Producto.objects.get(id_producto=id_producto)
    Productos.delete()
    return redirect('/')