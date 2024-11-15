from django.urls import path
from productos_app import views
urlpatterns = [
    path('', views.inicio_vista, name='inicio_vista'),
    path("registrarProducto/",views.registrarProducto,name="registrarProducto"),
    path("seleccionarProducto/<id_flor>",views.seleccionarProducto,name="selecionarProducto"),
    path("editarProducto/",views.editarProducto,name="editarProducto"),
    path("borrarProducto/<id_flor>",views.borrarProducto,name="borrarProducto"),
]
