# Web Scraping Tool #

Web Scraping Tool is a set of two applications: An extensible web scraper (Scrapy) and an API that serves what was scraped.

Currently only the spider for TechCrunch is available, but the project can be extended to have more spiders.

Python. Django. PostgreSQL. Scrapy.

Observation: The API (webscrapingtool) is in Python 3, since it is the recommended version to use and the one compatible with Heroku. However, scraper (webscraper) only works for Python 2 due to a dependency with the package 'twisted', that wasn't migrated to Python3.

### How to install? ###

```
sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev python3 python3-dev libpq-dev postgresql postgresql-contrib nginx
pipenv install
python manage.py makemigrations
python manage.py migrate
export DJANGO_SETTINGS_MODULE=webscrapingtool.settings
```

### How to run? ###

For API (Python 3):
```
gunicorn webscrapingtool.wsgi
```

For scraper (Python 2, uses the Pipfile inside webscraper):
- local
```
sh run_scraper_local.sh
```

- heroku
```
sh run_scraper_heroku.sh
```

### How to test? ###

```
cd webscrapingtool; python manage.py test; cd ..
```

### API Routes ###

Heroku: https://powerful-fjord-44213.herokuapp.com/

##### Outlets

- GET (list)
curl https://powerful-fjord-44213.herokuapp.com/v1/outlets/

- POST (create)
curl -d '{"name":"TechCrunch", "website":"https://techcrunch.com/", "description":"blah"}' -H "Content-Type: application/json" -X POST https://powerful-fjord-44213.herokuapp.com/v1/outlets/

- GET (individual)
curl https://powerful-fjord-44213.herokuapp.com/v1/outlets/1/

- PUT/PATCH (update)
curl -d '{"name":"TechCrunch", "website":"https://techcrunch.com/", "description":"blah"}' -H "Content-Type: application/json" -X PUT https://powerful-fjord-44213.herokuapp.com/v1/outlets/1/

- DELETE (remove)
curl -X "DELETE" https://powerful-fjord-44213.herokuapp.com/v1/outlets/1/

##### Authors

- GET (list)
curl https://powerful-fjord-44213.herokuapp.com/v1/outlets/1/authors/

- POST (create)
curl -d '{"name":"Ana", "email":"ana@gmail.com", "profile_page":"some_url"}' -H "Content-Type: application/json" -X POST https://powerful-fjord-44213.herokuapp.com/v1/outlets/1/authors/

- GET (individual)
curl https://powerful-fjord-44213.herokuapp.com/v1/outlets/1/authors/1/

- PUT/PATCH (update)
curl -d '{"name":"Ana Maria", "email":"ana@gmail.com"}' -H "Content-Type: application/json" -X PUT https://powerful-fjord-44213.herokuapp.com/v1/outlets/1/authors/1/

- DELETE (remove)
curl -X "DELETE" https://powerful-fjord-44213.herokuapp.com/v1/outlets/1/authors/1/

##### Articles

- GET (list)
curl https://powerful-fjord-44213.herokuapp.com/v1/outlets/1/articles/
curl https://powerful-fjord-44213.herokuapp.com/v1/outlets/1/articles/?title=guide

- POST (create using author_id, author_id must exist. Articles must be unique given (title, outlet, author).)
curl -d '{"title":"A Arte de Dormir", "content":"rh hrehe ehryey", "publication_date": "2001-12-30", "author_id": 1}' -H "Content-Type: application/json" -X POST https://powerful-fjord-44213.herokuapp.com/v1/outlets/1/articles/

- POST (create using author name, author will be created if it does not exist. Articles must be unique given (title, outlet, author).)
curl -d '{"title":"Oceano Raso", "content":"rg egrg gergeg", "publication_date": "2023-11-03", "author": "Fernando"}' -H "Content-Type: application/json" -X POST https://powerful-fjord-44213.herokuapp.com/v1/outlets/1/articles/

- GET (individual)
curl https://powerful-fjord-44213.herokuapp.com/v1/outlets/1/articles/1/

- PUT/PATCH (update)
curl -d '{"title":"Oceano Super Raso", "content":"rg egrg gergeg", "publication_date": "2023-11-03", "author_id": 2}' -H "Content-Type: application/json" -X PUT https://powerful-fjord-44213.herokuapp.com/v1/outlets/1/articles/2/

- DELETE (remove)
curl -X "DELETE" https://powerful-fjord-44213.herokuapp.com/v1/outlets/1/articles/1/

### TODOs:
- improve the search articles feature to support more complex queries
- allow sorting of results
- generate a good documentation, maybe using Swagger
- reference models by hiperlinks instead of PKs
- reorganize tests to use factories, to avoid duplicated code
- allow scraper to do POSTs in batches, to improve write performance
- add more tests for the 'sad' paths
- improve Article's 'tags' so it stores an array of strings + scraper should get an array of 'categories'
- maybe: routes for authors/:authorId/articles
- maybe: pagination
