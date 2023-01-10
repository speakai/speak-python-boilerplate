# Speak Python Boilerplate

Speak Python Boilerplate helps to create a microservice quickly in any environment.

Pre-configured files and templates to create your Flask API endpoint and deploy on Docker quickly.

## Set up virtual env

- Install virtualenv `pip install virtualenv`
- Create virtualenv `virtualenv venv`
- Activate virtualenv `venv\Scripts\activate.bat`

## Installation

`python install -r requirement.txt`

### Add to requirements.txt file

`pip freeze > requirements.txt`

### Run on your local server

First go to your `venv` environment:

`python application.py`

## Workflow

- application.py
- api
  - api_component.py
- utils
  - email.py
    - Send Error email
  - requests.py
    - Make a GET OR POST Request
- logging.ini
  - Logging format file
- application.py
  - Main application file

### Create your first API

- Create your first API by adding your `endpoint` in the `application.py` file
- Copy `api_component` file under `api` folder or **rename** the file name

- Add your logic under the `function`

- Start a server and test the endpoint

## Build Docker

- docker image build -t repo_name .
- docker tag repo_name organization_name/repo_name

### Run Docker

- docker run -p 5000:5000 -d repo_name

## To Deploy on AWS

`docker buildx build -t "________.dkr.ecr.ca-central-1.amazonaws.com/repo_name:latest" . --platform linux/amd64 --push`
