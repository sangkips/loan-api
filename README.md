# Loan-API

Loan-ApI is an Django Rest Framework application that helps traders request loan on your system.

## Installation

Use the package manager pip to install any package in the requirements.txt file.

### Steps to follow

- Clone the repository `https://github.com/sangkips/loan-api.git`

- Cd into the directory `cd loan-api`

- Create a virtual environment `python3 -m env venv`

- Activate virtual environment `source env/bin/activate`

- Install all projects dependencies using the `requirements.txt` file

`pip install -r requirements.txt`

### Create PostgreSQL Database

If you prefer postgreSQL over SQLite, you need to create a local database variables using .env file and move ahead to create a local postgreSQL database on your system.

### .env-sample

```
DATABASE_DB=dbname
DATABASE_USER=dbuser
DATABASE_PASSWORD=dbpassword
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### Make migrations

`python manage.py makemigrations`

### Migrate

`python manage.py migrate`

### Start the server

`python manage.py runserver`
