from django.urls import path
from pedido_app import views
urlpatterns = [
    path('', views.inicio_vista, name='inicio_vista'),
    path("registrarPedido/",views.registrarPedido,name="registrarPedido"),
    path("seleccionarPedido/<codigo>",views.seleccionarPedido,name="selecionarPedido"),
    path("editarPedido/",views.editarPedido,name="editarPedido"),
    path("borrarPedido/<codigo>",views.borrarPedido,name="borrarPedido"),
]
