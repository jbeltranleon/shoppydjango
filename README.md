# My very first application with Django

## Get started

### Use pip to install python-django and virtualenv 


Here we gonna find some settings that are necessary to start with the project

1. Create a new folder that will store the Django project and the virtual enviroment
 `$ mkdir Django`

2. Create a new virtual enviroment
 `$ virtualenv entornovirtual`

3. Activate the virtual enviroment
 `$ source entornovirtual/bin/activate`
 Use `$ deactivate` to turn off the virtualenv

4. With the virtualenv activate, we gonna install django
 `$ pip install django`

5. Finally we need to create a new django project
 `$ django-admin.py startproject commerce`

6. Starting the server
 `$ python manage.py runserver`

7. Creating a requirements.txt
`$ pip freeze > requirements.txt`

8. Using an existing requirements.txt
`$ pip install -r requirements.txt `
