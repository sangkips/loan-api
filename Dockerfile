# Python base image
FROM python:3.11-slim

# ensure all python outputs are send to the terminal 
ENV PYTHONUNBUFFERED=1

# set up working directory inside the container
WORKDIR /usr/src/app

# Install dependencies required by the image
RUN apt update && apt install -y g++ libpq-dev gcc musl-dev

# upgrade pip environment
RUN pip install --upgrade pip

# copy requirements.txt file to current directory
COPY requirements.txt .

# install requirements and allow Docker to cache all installed dependencies 
RUN python3 -m pip install -r requirements.txt --no-cache-dir

# copy and mount the project to the current directory
COPY . .

# Script
CMD ["./run.sh"]
