from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import LibroForm


#CRUD 

#CREATE
def crear_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("libros:listar")
    else:
        form = LibroForm()
    return render(request, "formulario_libro.html", {"form": form, "titulo": "Crear Libro"})

#READ
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, "listar_libros.html", {"libros": libros})

#UPDATE
def editar_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)
    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect("libros:listar")
    else:
        form = LibroForm(instance=libro)
    return render(request, "formulario_libro.html", {"form": form, "titulo": "Editar Libro"})

#DELETE
def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)
    if request.method == "POST":
        libro.delete()
        return redirect("libros:listar")
    return render(request, "confirmar_eliminacion.html", {"libro": libro})
