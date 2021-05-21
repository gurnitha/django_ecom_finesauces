## BUILDING ECOMMERCE APPLICATION USING DJANGO

https://github.com/gurnitha/django_ecom_finesauces

### 1. Complete setup: project created and connected with postgres db

	(venv3932) ing| tree -L 2
	.
	├── core
	│   ├── __init__.py
	│   ├── __pycache__
	│   ├── asgi.py
	│   ├── settings.py
	│   ├── urls.py
	│   └── wsgi.py
	├── manage.py
	└── readme.md

### 2. Create Github repository

	https://github.com/gurnitha/django_ecom_finesauces	
	modified:   readme.md

### 3. Create tables

	(venv3932) ing| python3 manage.py check
	System check identified no issues (0 silenced).
	(venv3932) ing| 
	(venv3932) ing| python3 manage.py makemigrations
	No changes detected
	(venv3932) ing| 
	(venv3932) ing| python3 manage.py migrate	

	modified:   readme.md

### 4. Create superuser

	(venv3932) ing| python3 manage.py createsuperuser
	Username (leave blank to use 'inyomangurnitha'): xxx
	Email address: ingafterxx@outlook.com
	Password: xx
	Password (again):xx 
	The password is too similar to the username.
	This password is too short. It must contain at least 8 characters.
	Bypass password validation and create user anyway? [y/N]: y	

	modified:   readme.md	

### 5. Create a new app 'listings'

	new file:   listings/admin.py
	...
	new file:   listings/views.py
	modified:   readme.md


### 6. Install listings to the project

	modified:   core/settings.py
	modified:   readme.md

### 7. Create Category model

	modified:   listings/models.py
	modified:   readme.md


























