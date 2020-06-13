# quest_meme

Prerequisites

As this software is on docker you will need to have docker and docker compose installed in your machine.


For Local Setup,
Go to project Root Dir

Build Containers
docker-compose -f local.yml build

Generate Migrations
docker-compose -f local.yml run --rm django python3 manage.py makemigrations users

Run Migrations
docker-compose -f local.yml run --rm django python3 manage.py migrate

Run The Containers
docker-compose -f local.yml up # This will start the container

If you want to use django python shell
docker-compose -f local.yml run --rm django python3 manage.py shell
