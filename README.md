# suba_d

## Project Description
suba_d is a Django-based project that provides a web interface for managing student details and their subject marks. The project includes the following features:
- Student model with fields: Name, Age, Email, and City.
- Subject Marks model with fields: Student (ForeignKey), Language 1, Language 2, Acting, and Dance.
- Django Admin interface for data entry.
- A detailed view displaying student information and their subject marks.

## Folder Structure
project_d/<br>
manage.py<br>
suba_d/<br>
init.py<br>
settings.py<br>
urls.py<br>
wsgi.py<br>
suba_a/<br>
init.py<br>
admin.py<br>
apps.py<br>
models.py<br>
views.py<br>
urls.py<br>
templates/<br>
student_detail.html<br>
migrations/<br>
init.py<br>


## Getting Started

### Prerequisites
- Python 
- Django 

### Installation

1.Create and activate a virtual environment:

```
python -m venv venv
venv\Scripts\activate
```
Install the required packages:

```
pip install -r requirements.txt
```
Run migrations:

```
python manage.py makemigrations
python manage.py migrate
```
Create a superuser:

```
python manage.py createsuperuser
Start the development server:
```
usename:suba
password:djangosuba

```
python manage.py runserver
```
# Usage
Access the Django Admin interface at http://127.0.0.1:8000/admin/ and log in with the superuser credentials.
Add student and subject marks entries via the admin interface.
View student details and their subject marks at http://127.0.0.1:8000/student/<id>/.
# Project Structure
project_d/: Project folder containing settings and configuration files.
suba_d/: Main Django project folder.
suba_a/: Django app folder containing models, views, templates, and admin configuration.

# output:
![Screenshot (427)](https://github.com/subasree22/subacreoproject/assets/154589464/ed69efd7-9698-421a-91fe-1823cd2184ed)
![Screenshot (428)](https://github.com/subasree22/subacreoproject/assets/154589464/259a5305-434f-4588-a187-a59ffed17364)
![Screenshot (429)](https://github.com/subasree22/subacreoproject/assets/154589464/00ba75b0-0d9a-4c69-83a0-231d21d18f81)
![Screenshot (430)](https://github.com/subasree22/subacreoproject/assets/154589464/e59bc7a2-2ea5-4182-a84a-80e9704ccab2)
![Screenshot (431)](https://github.com/subasree22/subacreoproject/assets/154589464/b058b6ba-8c8d-48ef-a59d-2ca7b6927327)
![Screenshot (431)](https://github.com/subasree22/subacreoproject/assets/154589464/3e1b1d79-696a-44d3-974f-c4e1e8f44c7d)
![Screenshot (432)](https://github.com/subasree22/subacreoproject/assets/154589464/246ce84f-c0fc-4e0f-89c4-a523d37cee2c)
