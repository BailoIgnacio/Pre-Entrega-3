# Proyecto_Final

# Sistema de Registro de Seguridad

Este proyecto es una página web de registro de seguridad desarrollada en Django. Permite gestionar información de personas relacionadas con la seguridad, como policías y presos, así como la gestión de prisiones. A través de esta plataforma, es posible registrar:

- Nombres, apellidos y nacimientos de policías.
- Nombres, apellidos, nacimientos y una descripcion de presos.
- Agregar nombres de carceles

Ademas, cuenta con un apartado de registros de usuarios e inicios de sesion con perfiles previamente creados, puediendo tambien editar sus cuentas cambiandoles el nombre, foto de perfil, mail, etc.

Cuenta con una gran seguridad, haciendo que no se pueda acceder a ningun apartado de la pagina web sin antes haber iniciado sesion, y en adicion, cuenta con encriptamiento de contraseñas creado por django.


## Instalación

Sigue los siguientes pasos para configurar el entorno y ejecutar el proyecto localmente:

1. Clona este repositorio en tu máquina local.
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio

2. Crea un entorno virtual con estos comandos en la consola
    python -m venv env
    env\Scripts\activate
    pip install django

3. Abre la pagina con las siguiente linea de codigo.
    python manage.py runserver
    Luego entra al link que se ha dejado en la consola

# Cuenta admin.

    Nombre de usuario = admin
    contraseña = 123



