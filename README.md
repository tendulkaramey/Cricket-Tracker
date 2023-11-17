# Cricket Tracker: Provide Live score to millions of users.

Project demonstrates how we can implement caching in  Django framework using redis so that we can serve the requests for live score directly from cache and thus lowering the load on database.

## Project Brief

Suppose we are a company called Cricket Tracker and our main job is to provide live cricket score ball by ball and along with score, every possible stats and commentary should be given in response.Team from ground will update the score using our UI and api to database.Millions of user will requests for live score of a match and if we pass all the requests to database then it can overwhelm the database.But if seen, for every live score it will do the same computation and query evaluation so why not do it once and save in cache and then serve the requests using cache which will not put burden on database and also lower the response time. We are using redis for caching.  <br>

We will update the cache as soon as we receive next live score from our team and thus old record in cache will be replaced for new one. Even if our cache went down due to some issue, for some time we can serve requests from database till we get cache up and running again. <br>

This is a POC (proof of concept) project aimed to learn and implement system design concepts from real life problem statements.

## Setting up

### setup log: create directory 'logs' before running

1. docker-compose up 
2. run migrations on db:docker-compose exec webserver python manage.py migrate
3. populate data into database: docker-compose exec webserver python manage.py populatedb
4. There are 2 apis: 1 for getting live score and 1 for adding new live score, you can find it in postman-api folder.
5. On populating the database, you can create superuser using python manage.py createsuperuser. visit localhost:8000/admin and add fixtures for the tournament.
6. use the api to keep adding the live score from postman.
7. use the api to get latest live score that has been posted.
8. you can use pgadmin tool to login and view your database. username and password is in docker-compose file. it works on port 5051.

## Running

use the postman collection to test and run the api.

docker-compose exec cache redis-cli -a pass123 : run this in terminal and try on different redis operations. you can check for keys once you hit the add live score api, you will see the key added in redis cache.


## References:

- https://redis.io/docs/about/
- https://pypi.org/project/django-redis/
- https://docs.djangoproject.com/en/4.2/topics/cache/