from django.shortcuts import render, redirect
from .models import Curso

# Create your views here.
def Home(request):
    cursos = Curso.objects.all()
    return render(request, "gestion.html", {"cursos": cursos})

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(codigo = codigo, nombre = nombre, creditos = creditos)

    return redirect('/')

def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    return redirect('/')

def editarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "editarCurso.html", {"curso": curso})

def edicionCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    return redirect('/')
