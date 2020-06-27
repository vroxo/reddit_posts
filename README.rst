# REDDIT HOT POSTS API

## CLONE

`$ git clone git@github.com:vroxo/reddit_posts.git`

or

`$ git clone https://github.com/vroxo/reddit_posts.git`

## SETUP

This application uses docker containers, it is mandatory to install Docker CLI and Docker compose.

Create the containers from the docker-compose.yml file:

`$ docker-compose up -d --build`

All application dependencies will be installed and the application started using the address http://localhost:5000/ (default for a Flask application)

If we look at the pyproject file we will see that the main dependencies of the application:

- Python 3.8
- Flask
- Connexion
- Flask MongoEngine
- Flask APScheduler
- Pytest
- Dynaconf
- MongoDB

Run the Flask custom command to populate the database with fake data:

`$ docker-compose exec web flask populate-db`

Run job to consult the reddis api and populate the database with real data.
This task is scheduled in the application to run every 10 minutes:

`$ docker-compose exec web flask job-reddit-posts`


If you want to clear the existing data in the database, use:

`$ docker-compose exec web flask truncate-db`

Run tests:

`$ pytest tests/`

## API DOCUMENTATION

This application uses Swagger and OpenApi 3 for API documentation:

- UI: http://localhost:5000/api/v1/ui/
- JSON: http://localhost:5000/api/v1/openapi.json