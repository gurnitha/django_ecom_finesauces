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