# Generated by Django 5.0.1 on 2024-01-31 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tbl_cursos',
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id_estudiante', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('cursos', models.ManyToManyField(related_name='estudiantes', to='select_multiple.curso')),
            ],
            options={
                'db_table': 'tbl_estudiantes',
            },
        ),
    ]
