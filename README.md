# Social Food Posting

# Backend

## Table of Contents

1. [Project Goals](#project-goals)
2. [User Stories](#user-stories)
3. [Design](#design)
4. [Technologies](#technologies)
5. [Dependencies](#dependencies)
6. [Setup and Installation](#setup-and-installation)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Acknowledgements](#Acknowledgements)

## Project Goals

Social Food Posting simple platform for users to share their culinary creations, interact with like-minded individuals, and manage user profiles, posts, likes, and comments. 

## User Stories

- As a user, I want to register an account and log in to access the platform's features.
- As a user, I want to post photos of my dishes and share them with the community.
- As a user, I want to like and comment on posts from other users.
- As a user, I want to update my profile information and manage my posts.

## Diagram

https://www.lucidchart.com

![Class Diagram](<testingmd/images/Screenshot 2024-05-01 130937.png>)


## Technologies

Django: 
- Version: 5.0.4
- The primary web framework used for building your application.
- Handles web requests, routing, sessions, and forms among other backend functions.


Django REST Framework (DRF):
- Version: 3.15.1
- Building RESTful APIs with Django.


Simple JWT: Adds JWT (JSON Web Token) 
- Version: 5.3.1
- authentication for Django REST Framework.
- Manages token creation and verification for secure API access.


Cloudinary: 
Version: 1.39.1
- Media management allows you to store and retrieve images and video files.
- Integrated via django-cloudinary-storage for managing file uploads and static/media storage.


django-cors-headers: 
Version: 4.3.1
- Middleware handling Cross-Origin Resource Sharing (CORS), allowing or restricting cross-domain requests.


Python Decouple: 
- Version: 3.8
- Manages environment variables and configurations securely.


Django Filters: 
Version: 24.2
Library for filtering querysets based on request parameters.

Gunicorn: 
- Version: 21.2.0
- WSGI HTTP server for UNIX, serving Django applications in production.


PostgreSQL (via psycopg2-binary): 
- Version: 2.9.9 (for psycopg2-binary)
- Database backend used to store application data securely and robustly.


## Dependencies

`Django: Django==5.0.4`
`djangorestframework==3.15.1`
`djangorestframework-simplejwt==5.3.1`
`cloudinary==1.39.1`
`django-cloudinary-storage==0.3.0`
`dj3-cloudinary-storage==0.0.6`
`psycopg2-binary==2.9.9`
`python-decouple==3.8`
`gunicorn==21.2.0`
`django-cors-headers==4.3.1`
`django-filter==24.2`
`PyJWT==2.8.0`
`dj-database-url==2.1.0 `


## Setup and Installation

### Pre-pre checks 
- Python 3.10+
- Visual Studio Code

### 1. Cloning the Repository
Clone the repository to your local machine:
- ![alt text](<testingmd/images/Screenshot 2024-05-01 134745.png>)

- ![alt text](<testingmd/images/Screenshot 2024-05-01 134752.png>)

### Virtual Environment setup 
- ***Using Windows***

- ***`python -m venv venv`***
- ***`.\venv\Scripts\activate`***

## Install Dependencies

### Install the required packages:

- ***Copy the list above and run this command***
- ***pip install*** - ***copied list from above it will then install all you need*** 

**To add it to a requirements list run the pip freeze -r requirements.txt will create the requirements.txt with all of the installed dependencies.** 

**Then to start the "project"**

- ***django-admin startproject "name of the project folder" don't forget the dot after the project .***

**Test that it runs "python manage.py runserver"**

**Then don't forget to add .gitignore and add the ".env" for the enviroment variables ( i used Decouple it looks clean in the settings.py )**


### In settings.py 

- ***DEBUG = config('DEBUG', default=False, cast=bool)***

- ***SECRET_KEY = config('SECRET_KEY')***

- ***if DEBUG:***
  -  ***ALLOWED_HOSTS = ['127.0.0.1', 'localhost']***
  -  ***CORS_ALLOWED_ORIGINS = ['http://localhost:5173']*** **FRONTEND DURING DEVELOPMENT.**
- ***else:***
  - ***ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')***
  -  ***CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS').split(',')***


### The .env : 

- ***DEBUG=True*** ( during development ) False in Production.

- ***ALLOWED_HOSTS='PRODUCTION URL'***

- ***SECRET_KEY='SECRET KEY THAT COMES WITH THE INSTALL AND UPDATE IT DURING DEVELOPMENT AND THEN BEFORE DEPLOYING'*** 

- ***CORS_ALLOWED_ORIGINS='PRODUCTION URL ,http://localhost:5173'***


## Testing

### Postman endpoint testing ( Registration / Login  )

![Registration Test](<testingmd/images/Screenshot 2024-05-01 113635.png>)
![Login Test](<testingmd/images/Screenshot 2024-05-01 113722.png>)

### Unit tests 

### Coverage

## Deployment



## Acknowledgements