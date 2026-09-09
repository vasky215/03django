# 03django
CTRL + SHIFT + P (CREATE INSTANCE .venv) - Crear instancia venv es una herramienta oficial de Python que crea espacios de trabajo aislados. Permite instalar paquetes y librerías para un proyecto sin afectar a otros programas ni al sistema principal de tu computadora.

-Dentro del entorno virtual instalar django usando pip // pip install django

-Para crear proyecto: django-admin startproject ejemplo01 .

-Para correr server: python manage.py runserver

-Para crear APP: python manage.py startapp app1

-Para agregar APP en settings: Agregar en la lista del installed apps

-Para agregar libreria http response: views -> from django.http import HttpResponse

-Agregar cosas a views y a urls (en el proyecto, y las views en app1)

-Guardar requerimientos (para que el proyecto se levante con las librerias hechas!): pip freeze > requirements.txt

-IGNORAR ARCHIVOS: .gitignore - Así se omiten el pycache, los terminados en .sqlite3 y el .venv !!!

-CTRL + C para salir de la instancia

git config --global user.name "FranciscoDev"
git config --global user.email "francisco.jbrionescontreras2005@gmail.com"

pip freeze > requirements.txt

crear una nueva rama git branch ramainicio

cambiar de rama  git checkout main
