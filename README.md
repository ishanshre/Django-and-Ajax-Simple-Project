# A simple CRUD django and ajax project

## Features
1. Load button and spinner to load more posts using ajax
2. Like and Unlike Button for logged in user
3. Create Post and display it in the list without reloading the page
4. Update and Delete Post without reloading
5. Auto create profile when user is created
6. Added Authentication and Authorization function
7. Profile update without reloading


## Installation process
1. Clone this repo:
    ```
    git clone https://github.com/ishanshre/Django-and-Ajax-Simple-Project.git

2. Create a python virtual env inside the repository and activate it
    ```
    $ python -m venv venv
        or
    $ python3 -m venv venv
    For Linux
    $ source venv/bin/activate
    For windows
    > venv/Scripts/activate.bat

3. Install the required packages from requirements.txt
    ```
    pip install -r requirements.txt
        or
    pip3 install -r requirements.txt

4. Run migration command
    ```
    python manage.py migrate

5. Create a superuser using
    ```
    python manage.py createsuperuser

6. Run the development server
    ```
    python manage.py runserver

7. Go to ```127.0.0.1:8000``` to view the django project