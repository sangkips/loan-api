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
DATABASE_HOST=db
DATABASE_PORT=5432
```

### Make migrations

`python manage.py makemigrations`

### Migrate

`python manage.py migrate`

### Start the server

`python manage.py runserver`

### To use Phone Number field

To use Phone Number field make sure you are starting with the coutry's prefix such as `(+1, for US, +254 for Kenya)`

## Docker

### To buld docker image

In order to build the docker image use `make`

### To run the Docker container

Run Docker container with the following command

- `docker-compose up`

- `-d` when you want to run in detached mode

### Stop running container

- `docker-compose stop`

## Running Django Application

To run dajngo-related commands use the following

### Make Migrations

- `docker-compose run app /usr/local/bin/python manage.py makemigrations`
  `app` comes from docker-compose.yml file

### Migrate

- `docker-compose run app /usr/local/bin/python manage.py migrate`

### Run server

- `docker-compose run app /usr/local/bin/python manage.py createsuperuser`
