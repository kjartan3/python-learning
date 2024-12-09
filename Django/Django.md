To successfully create a Django project - 

You must begin with cerate a virtual environment by doing, once youre in the right folder:

python3 -m venv .  (this creates a virtual environment in the current working directory)

then Activate the virtual environment:

source $.../'project.name'/bin/activate OR bin/activate

Next, you will create a project in that virtual environment, by:

django-admin startproject 'project.name'  (in terminal)

Then move to that project folder and run the server:

python3 manage.py runserver

