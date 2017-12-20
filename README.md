# Web Scraping Tool #

[TODO: Brief introduction to what this repo does and what techs it uses.]

### How to install? ###

sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
sudo apt-get install python3 python3-dev
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
export DJANGO_SETTINGS_MODULE=webscrapingtool.settings

### How to run? ###

python manage.py runserver

### How to test? ###

python manage.py test

### API Routes ###

#### Outlets

curl http://localhost:8000/outlets/

curl -d '{"name":"value1", "website":"value2", "description":"blah"}' -H "Content-Type: application/json" -X POST http://localhost:8000/outlets/

curl http://localhost:8000/outlets/1/

curl -d '{"name":"value1", "website":"value3", "description":"blah"}' -H "Content-Type: application/json" -X PUT http://localhost:8000/outlets/1/

curl -X "DELETE" http://localhost:8000/outlets/2/

#### Authors

curl http://localhost:8000/outlets/1/authors/

curl -d '{"name":"value1", "email":"value2"}' -H "Content-Type: application/json" -X POST http://localhost:8000/outlets/1/authors/