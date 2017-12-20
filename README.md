# Web Scraping Tool #

[TODO: Brief introduction to what this repo does and what techs it uses.]

### How to install? ###

[TODO]

### How to run? ###

[TODO]

### How to test? ###

[TODO]

### API Routes ###

[TODO]

#### Outlets

curl http://localhost:8000/outlets/

curl -d '{"name":"value1", "website":"value2", "description":"blah"}' -H "Content-Type: application/json" -X POST http://localhost:8000/outlets/

curl http://localhost:8000/outlets/1/

curl -d '{"name":"value1", "website":"value3", "description":"blah"}' -H "Content-Type: application/json" -X PUT http://localhost:8000/outlets/1/

curl -X "DELETE" http://localhost:8000/outlets/2/

#### Authors

curl http://localhost:8000/outlets/1/authors/

curl -d '{"name":"value1", "email":"value2"}' -H "Content-Type: application/json" -X POST http://localhost:8000/outlets/1/authors/