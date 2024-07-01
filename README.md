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
