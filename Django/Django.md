To successfully create a Django project - 

You must begin with cerate a virtual environment by doing, once youre in the right folder:

python3 -m venv .  (this creates a virtual environment in the current working directory)

then Activate the virtual environment:

source $.../'project.name'/bin/activate OR bin/activate

Next, you will create a project in that virtual environment, by:

django-admin startproject 'project.name'  (in terminal)

Then move to that project folder and run the server:

python3 manage.py runserver

On a different terminal in the virtual environment folder, run:

python manage.py migrate   (which shows all apps)

Then create the first user for the app:

python manage.py createsuperuser

Then you can log into this user-account on the server url http://.../admin

After, you can start to build an application, by running:

python manage.py startapp 'project.name'

Then start building in models.py of that new project folder. Add the new project app into settings.py - INSTALLED_APPS.

Whenever there are any changes to models.py, you must make sure to run makemigrations and migrate.

Option: to fill database manually with terminal, starting with - python manage.py shell

from products.models import Product

Product.objects.all()

Product.objects.create(title='Project', description='Project description', price=1, summary='Project')

Entering the above will create a new Product 





