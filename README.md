# Installation
There are two ways to get it up:
1. The easy way
2. The not so easy way
## Easy way
Just install Docker and run:
```bash
docker compose-up
```
Now you have all the dependencies, and the system up and running! You have a DB instance, a pgAdmin, because reasons, running on the port 5050
and the app running on 8000.
## Not so easy way
You will need various tools installed on your computer.  
First you must install pipenv because who uses only pip for dependencies on 2021?  
In macOS, any distro and WSL the easiest way is to use pipx
```bash
pipx install pipenv
```
Now that you have pipenv, install your dependencies using pipenv with the following command:
```bash
pipenv install
```
Now you need a DB, the project will work with sqlite out of the box, but, if you want a more robust DB you can setup a PostgreSQL DB! Don't forget to set the DATABASE_URL environment variable with your DB settings. This doesn't work with mySQL, I don't like mySQL and neither should you.  
Next, you need to migrate, and add the initial data to the DB.
Run:
```bash
piepnv run python manage.py migrate && pipenv run python manage.py loaddata hits
```
Now I think you have everything to make this work, you only need to run the following command and it should run:
```bash
pipenv run python manage.py runserver
```
This will start a server at port 8000.
# Usage
The initial data has 9 hitmen, 3 managers and the one and only Boss. The Boss account is:
```
usr: the.boss@outerheaven.com
pass: Test0987*_
```
All the users has the same pass; the usernames, well, you can check it directly on the DB or on the list service on the app, logged in as The Boss.