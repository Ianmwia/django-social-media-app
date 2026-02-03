# Social Media Project

This project is a social media gallery web app.It allows users to create an account, login and access
built in features to add images and view other peoples posted images and like them.It also features api endpoints for the models created 

## Tech Stack

![Django](https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white)

- **Backend** python3, Django
- **Frontend** Django Htmx
- **Database** PostgreSQL
- **Authentication** Django Auth
- **Libraries and dependencies** Available in the requirements.txt file

## Features

- Account creation - Secure account creation and authentication with django
- User Authentication and validation
- Profile Page - A dedicated profile page for authenticated users
- Add photo page - Ability to add pictures, save them and persist
- View added photos in library

## Live demo

_Coming Soon_

## Installation and Setup

1. Clone the repository

```bash
git clone https://github.com/Ianmwia/django-social-media-app.git
```

2. Open the folder in a terminal

```git
cd photo_project

```
3. Create the virtual environment

```git
source venv/scripts/activate
```

4. Install the dependencies

```git
pip install -r requirements.txt
```

5.Open in vs code and run the server

```python
python manage.py runserver
```

## API Endpoints

Endpoints are available for serialized models to perform crud applications(GET, CREATE, UPDATE, DELETE) on
Users, Posts and Comments


```api
http://127.0.0.1:8000/api/profile/

```

```api
http://127.0.0.1:8000/api/comment/
```

```api
http://127.0.0.1:8000/api/post/
```

## Contributing

- Contributions are welcome
- Feel Free to Fork the Repository and  Submit a pull request

- If there are any issues or comments please raise a new Issue
