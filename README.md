# Web Scraping Tool #

Web Scraping Tool is a set of two applications: An extensible web scraper (Scrapy) and an API that serves what was scraped.

Currently only the spider for TechCrunch is available, but the project can be extended to have more spiders.

Python. Django. SQLite3. Scrapy.

### How to install? ###

```
sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev python3 python3-dev
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
export DJANGO_SETTINGS_MODULE=webscrapingtool.settings
```

### How to run? ###

For API:
```
python manage.py runserver
```

For scraper:
```
scrapy crawl techcrunch
```

### How to test? ###

```
python manage.py test
```

### API Routes (samples) ###

curl http://localhost:8000/outlets/

curl -d '{"name":"value1", "website":"value2", "description":"blah"}' -H "Content-Type: application/json" -X POST http://localhost:8000/outlets/

curl http://localhost:8000/outlets/1/

curl -d '{"name":"value1", "website":"value3", "description":"blah"}' -H "Content-Type: application/json" -X PUT http://localhost:8000/outlets/1/

curl -X "DELETE" http://localhost:8000/outlets/2/

curl http://localhost:8000/outlets/1/authors/

curl -d '{"name":"value1", "email":"value2"}' -H "Content-Type: application/json" -X POST http://localhost:8000/outlets/1/authors/

### Challenge Checklist

##### MVP
[x] Create a private repository on Bitbucket and add @carolschmitz as admin;
[x] The suggested framework is: Django;
[x] Create a web scraping tool that constantly scrapes the articles of a major blog like TechCrunch (http://techcrunch.com) and stores it in a database (DBMS is a choice of the candidate). These are the relevant data that we want to store:
    [x] Outlet name and metadata (URL, description, etc);
    [x] Authors (name, twitter handle, profile page, etc);
    [x] Published articles and metadata (publication date, author, content, etc);
[x] Create a JSON REST API endpoints that serve the database data (outlets, authors and articles) - only GET is necessary;
[x] An (oversimplified) example of API response for articles: http://www.ckl.io/challenge/.
[x] Create a pull-request and assign it to @carolschmitz.
[ ] Host the server and provide its IP, as well as all the endpoint(s)  (https://devcenter.heroku.com/articles/getting-started-with-python#introduction);
    [x] Chenge python version to 3.6
    [ ] Change the database to postgresql
[ ] It should scrape constantly

##### Extras
[x] Use cool GitHub libraries to aid the development;
[x] Setup automatic tests;
[x] Use a dependency manager;
[x] Add other REST-compliant HTTP methods for the API (PUT, PATCH, POST, etc);
[x] A server that resists to DDoS attacks;
[x] Integrate with CI;
[ ] Provide an API endpoint to perform searches for articles;
[ ] Use automatic deploys;

### Future Improvements:
- reference models by hiperlinks instead of PKs
- reorganize tests to use factories, to avoid duplicated code
- allow scraper to do POSTs in batches, to improve write performance
- add more tests for the 'sad' paths
- improve Article's 'tags' so it stores an array of strings + scraper should get an array of 'categories'
- use environment variables to config the application
- use config files to config the application
- maybe: routes for authors/:authorId/articles
- maybe: pagination
