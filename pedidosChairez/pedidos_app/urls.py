from django.urls import path
from pedidos_app import views
urlpatterns = [
    path('', views.inicio_vista, name='inicio_vista'),
    path("registrarPedido/",views.registrarPedido,name="registrarPedido"),
    path("seleccionarPedido/<id_pedido>",views.seleccionarPedido,name="selecionarPedido"),
    path("editarPedido/",views.editarPedido,name="editarPedido"),
    path("borrarPedido/<id_pedido>",views.borrarPedido,name="borrarPedido"),
]
