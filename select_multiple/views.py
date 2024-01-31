from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Estudiante, Curso

# Create your views here.


def inicio(request):
    return render(request, 'index.html')


def add_student(request):
    if request.method == 'POST':
        # Crear un estudiante
        student_name = request.POST.get('estudiante')
        # estudiante = Estudiante.objects.create(nombre=student_name)
        estudiante = Estudiante(nombre=student_name)
        estudiante.save()

        # Obtener los cursos seleccionados y asociarlos al estudiante
        cursos_seleccionados = request.POST.getlist('cursos[]')
        for curso_nombre in cursos_seleccionados:
            # Obtener o crear el curso
            curso, created = Curso.objects.get_or_create(nombre=curso_nombre)

            # Asociar el curso al estudiante
            estudiante.cursos.add(curso)

        # Redirigir a la página principal o a donde desees
        return redirect('inicio')
    return render(request, 'index.html')


def listar_estudiantes(request):
    # Obtener todos los estudiantes
    estudiantes = Estudiante.objects.all()
    # Renderizar la plantilla con la lista de estudiantes y sus cursos
    return render(request, 'estudiantes.html', {'estudiantes': estudiantes})
