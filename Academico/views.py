from django.shortcuts import render, redirect
from .models import Curso

# Create your views here.
def home(request):
    curso = Curso.objects.all() #Este es el listado de todos los cursos, se traen desde la base de datos
    return render(request, 'gestionCurso.html', {'curso': curso})

def registrarCurso(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']   
    credito = request.POST['numCredito']

    curso = Curso.objects.create(cogido=codigo, nombre=nombre, credito=credito)#Primero va como esta en el modelo y luego como lo recibe
    return redirect('/')

def eliminarCurso(request, codigo):
    curso = Curso.objects.get(cogido=codigo)
    curso.delete()
    return redirect('/')

def edicioncurso(request, codigo):
    curso = Curso.objects.get(cogido=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']   
    credito = request.POST['numCredito']

    curso = Curso.objects.get(cogido=codigo)
    curso.nombre = nombre
    curso.credito = credito
    curso.save()

    return redirect('/')

