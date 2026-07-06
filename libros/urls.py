from django.urls import path
from . import views

app_name = "libros"

urlpatterns = [
    path("", views.listar_libros, name="listar"),
    path("crear/", views.crear_libro, name="crear"),
    path("editar/<int:id>/", views.editar_libro, name="editar"),
    path("eliminar/<int:id>/", views.eliminar_libro, name="eliminar"),
]
