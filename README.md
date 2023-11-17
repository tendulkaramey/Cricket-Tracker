# Cricket Tracker: Provide Live score to millions of users.

Project demonstrates how we can implement caching in  Django framework using redis so that we can serve the requests for live score directly from cache and thus lowering the load on database.

## Project Brief

As Cricket Tracker, our core function is to deliver real-time cricket scores, inclusive of detailed statistics and commentary, ball by ball. Our system involves ground teams updating scores via our UI and API, which are then stored in our database. With millions of users seeking live match scores, directing all these requests to the database could potentially overwhelm it.<br>

Considering that each live score update entails the same computations and query evaluations, it seems more efficient to perform these actions once and store the results in a cache. By utilizing Redis for caching, we can significantly reduce the strain on our database, ensuring quicker response times and reducing the load on our infrastructure. <br>

Our strategy involves promptly updating the cache with the latest live scores as soon as they're received from our ground team. This approach ensures that older cache records are replaced with the most recent information. In the event of a cache failure, we have a contingency plan in place: for a temporary period, we'll serve requests directly from the database until the cache is operational again. This ensures continuous service delivery and minimizes disruption to our users even during cache downtime. <br>

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

docker-compose exec cache redis-cli -a pass123 : run this in terminal and try on different redis operations. you can check for keys once you hit the add live score api, you will see the key added in redis cache.<br>

Review the SQL logs to note that when the "get live score" API retrieves data from the cache, it operates without any database calls. This absence of database queries optimizes response times, enabling us to handle a higher volume of requests concurrently by using caching efficiently.


## References:

- https://redis.io/docs/about/
- https://pypi.org/project/django-redis/
- https://docs.djangoproject.com/en/4.2/topics/cache/