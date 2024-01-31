from django.db import models


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_cursos'

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    cursos = models.ManyToManyField(Curso, related_name='estudiantes')

    class Meta:
        db_table = 'tbl_estudiantes'

    def __str__(self):
        return f'Estudiante: {self.estudiante.nombre} - Curso: {self.curso.nombre}'
