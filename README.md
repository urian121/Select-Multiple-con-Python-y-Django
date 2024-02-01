### Select Múltiple Dinámico con Python y Django

##### El proyecto "Select Múltiple Dinámico con Python y Django" permite a los usuarios seleccionar múltiples opciones de manera dinámica dentro de un formulario web, facilitando la selección y asociación de datos en aplicaciones Django. Utiliza tecnologías web como Python, Django y JavaScript para lograr una experiencia de usuario interactiva y eficiente.

1.  Crear un entorno virtual, hay muchas formas

        Opción 1: Crear entorno virtual con el paquete virtualenv
        Si no tienes instalado virtualenv puedes instalarlo de forma global en el sistema atraves de https://pypi.org/project/virtualenv/
        pip install virtualenv ->Instalar de forma global
        virtualenv env ->Crear entorno
        virtualenv --version ->Ver la versión de virtualenv

        Opción 2: Crear un entorno virtual con el paquete que ya viene por defecto en las ultimas versiones de Python
        python -m venv env

2.  Activar entorno virtual

        . env/Script/activate ->para Windows
        . env/bin/activate -> Para Mac
        deactivate -->Para desactivar mi entorno virtual

3.  Instalar django desde el manejador de paquete de Python Pip, ya dentro del entorno virtual.

        pip install Django
        Nota: para instalar Django en una version especifica
        pip install Django==4.2.4

4.  Instalar Driver para conectar Gestor de BD MySQL con Django, con el fin de crear una tabla para almacenar los idiomas disponibles

        pip install mysqlclient

5.  Crear el proyecto con django

        `django-admin startproject project_core .`
        El punto . es crucial le dice al script que instale Django en el directorio actual

        Ya en este punto se puede correr el proyecto que a creado Django,
        python manage.py runserver

6.  Crear mi primera aplicación en Django

        python manage.py startapp select_multiple

7.  Instalar nuestra aplicación (select_multiple) ya creada en el proyecto, en el archivo settings.py

        archivo settings.py
        INSTALLED_APPS = [
        ----,
        'select_multiple',
        ]

8.  Crear las migraciones y correrlas

        python manage.py makemigrations -> Creando migraciones
        python manage.py migrate         -> Correr migraciones

9.  Correr el proyecto

        python manage.py runserver
        Revisar la consola y visitar la URL http://127.0.0.1:8000

10. Crear el archivo urls.py en la aplicación (select_multiple)

        from django.urls import path
        from . import views

                urlpatterns = [
                        path('', inicio, name='inicio'),
                        path('registrar-estudiante/', add_student, name='add_student'),
                        path('estudiantes/', listar_estudiantes, name='estudiantes'),
                ]

11. Conectar las URLS de mi aplicación con el projecto, para esto vamos al archivo uls.py del projecto
    from django.urls import path, include

        urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include('select_multiple.urls')),
        ]

12. Crear la carpeta 'templates' dentro de la aplicación donde estarán mis index.html

13. Crear la carpeta 'static' dentro de mi aplicacion, aqui estaran archivos
    estaticos (css, js, imagenes, etc..)

14. Correr archivo requirement.txt para instalar todas las dependencias del proyecto

        pip install -r requirements.txt

15. Correr aplicación en un puerto en especifico

        python manage.py runserver 0:8500

#### Referencia

        https://harvesthq.github.io/chosen/

#### Nota

        La tabla tbl_estudiantes_cursos es creada automáticamente por Django debido a la relación many-to-many que se ha definido entre los modelos Estudiante y Curso. Esta tabla intermedia se utiliza para almacenar las asociaciones entre los estudiantes y los cursos que han sido seleccionados.

        Cuando se define una relación ManyToManyField en un modelo de Django, Django crea automáticamente una tabla intermedia para representar la relación many-to-many entre los dos modelos. Esta tabla intermedia contiene generalmente dos campos de clave externa que apuntan a las claves primarias de los modelos relacionados.

        La relación "many-to-many" (muchos a muchos) es un tipo de relación en bases de datos relacionales y también en el contexto de los modelos en el marco de Django.

####

        El uso de get_or_create() es una forma conveniente y común en Django para obtener un objeto de modelo de la base de datos si existe, o crearlo si no existe. Sin embargo, dependiendo de tus necesidades y del contexto específico de tu aplicación, podrías optimizar o ajustar esta lógica.

        Una forma de mejorar la expresión get_or_create() es usar update_or_create(), especialmente si necesitas actualizar algún campo del modelo en caso de que el objeto ya exista. Este método te permite actualizar los campos del objeto si ya existe, en lugar de simplemente recuperarlo.

        curso, created = Curso.objects.update_or_create(
        nombre=curso_nombre,
        defaults={'otro_campo': valor_otro_campo}

)

#### Resultado final

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/select-multiple-con-python.png)

### Expresiones de Gratitud 🎁

    Comenta a otros sobre este proyecto 📢
    Invita una cerveza 🍺 o un café ☕
    Paypal iamdeveloper86@gmail.com
    Da las gracias públicamente 🤓.

## No olvides SUSCRIBIRTE 👍
