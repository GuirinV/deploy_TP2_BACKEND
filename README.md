### INTEGRANTES DEL PROYECTO
-Verónica Guirin
-Mateo Saavedra
-Angelina Zarantonello

### LINK A LA PRESENTACIÓN DEL PROYECTO
https://1drv.ms/v/s!AvBvlmf7wmfUqBVXl9aaw1ckdcWw

### README - Pasos del Trabajo_2
Este README proporciona una guía detallada de los pasos necesarios para la creación de una API y su posterior implementación (deploy) en PythonAnywhere. El proceso abarca desde la configuración del entorno de desarrollo hasta la puesta en funcionamiento de la aplicación web.

1. Creación de API
   1.1 Repositorio en GitHub
   Clonar el repositorio del proyecto desde GitHub.
   Abrir el proyecto en Visual Studio Code (VSCODE).
   1.1.1 Limpieza del Repositorio
   Eliminar archivos y carpetas no necesarios, como por ejemplo, la base de datos SQLite.
   1.1.2 Instalación de Dependencias
   Instalar las dependencias de mysqlclient.
   Verificar el funcionamiento de la API localmente: python manage.py runserver.
   Realizar migraciones para configurar las tablas en la base de datos: python manage.py makemigrations y python manage.py migrate.
   1.1.3 Requirements.txt
   Congelar las dependencias en un entorno virtual y guardarlas en requirements.txt: pip freeze > requirements.txt.
   Eliminar carpetas y elementos no esenciales (por ejemplo, pycache, carpetas venv).
   1.2 Deploy en PythonAnywhere
   1.2.1 Creación de Cuenta en PythonAnywhere
   Crear una cuenta en PythonAnywhere.
   1.2.2 Consola en PythonAnywhere
   Acceder a la consola desde el dashboard de PythonAnywhere.
   Instalar las dependencias necesarias para el proyecto: pip install --user pythonanywhere.
   Posicionarse en la carpeta del proyecto y crear un entorno virtual: mkvirtualenv --python=python3 venv.
   Instalar las dependencias desde requirements.txt: pip install -r requirements.txt.
   1.2.3 Configuración en PythonAnywhere
   1.2.3.1 Web Apps
   Ir a la sección "WEB" en PythonAnywhere y seleccionar "ADD A NEW WEB APP".
   Elegir "Manual Configurations" para personalizar la configuración.
   Configurar la ruta del código, entorno virtual, archivos estáticos y archivo de configuración WSGI.
   1.2.3.2 WSGI Configuration File
   Modificar el archivo de configuración WSGI con la ruta del proyecto y el nombre de los settings.
   1.2.3.3 Settings.py
   Modificar ALLOWED_HOSTS en settings.py con el dominio de PythonAnywhere.
   Realizar commit, pull y recargar en PythonAnywhere.
   1.2.4 Migración de la Base de Datos en PythonAnywhere
   Realizar migraciones: python manage.py makemigrations y python manage.py migrate.
   Recargar en PythonAnywhere.
   1.2.5 Configuración de Archivos Estáticos
   Configurar STATIC_ROOT, STATIC_URL, y STATICFILES_DIRS en settings.py.
   Realizar commit, pull, recoger archivos estáticos y recargar en PythonAnywhere.
   1.2.6 Agregar una Base de Datos en PythonAnywhere
   Crear una base de datos en la sección "Databases" de PythonAnywhere.
   Configurar los datos de la base de datos en settings.py.
   1.2.7 Verificar la API
   Acceder a la consola MySQL en PythonAnywhere.
   Mostrar las tablas y verificar la correcta configuración de la base de datos.
   Realizar consultas para verificar el correcto funcionamiento de la API.
   Este README proporciona una guía detallada para configurar y desplegar la API en PythonAnywhere, asegurando un proceso paso a paso para garantizar el correcto funcionamiento de la aplicación web.
