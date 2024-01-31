from django.urls import path
from . views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('registrar-estudiante/', add_student, name='add_student'),
    path('estudiantes/', listar_estudiantes, name='estudiantes'),

]
