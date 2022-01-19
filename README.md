# Change Event Service

This service is web service that provides a RESTful API for creating, deleting and querying change events.
## How it Works?
This project written with [Flask web framework](https://flask.palletsprojects.com/en/2.0.x/). It use [flask-smorest](https://flask-smorest.readthedocs.io/en/latest/index.html) for REST API, [Pyctuator](https://github.com/SolarEdgeTech/pyctuator) for actuator endpoint and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) for handle DB queries. Swagger UI documentation and API validations handled by flask-smorest itself. flask-smorest uses [Marshmallow](https://marshmallow.readthedocs.io/en/stable/index.html) schemas for marshalling and unmarshalling objects in request and response. This schemas also used by Swagger UI.  

With [Flask-APScheduler](https://viniciuschiele.github.io/flask-apscheduler/index.html), a background job started to consume change events from the queue using [Pika](https://pika.readthedocs.io/en/stable/) and persist them to the database.

## Environment Variables
* `__SERVICE_MQ_HOST` : RabbitMQ host
* `__SERVICE_MQ_VHOST`: RabbitMQ virtual host
* `__SERVICE_MQ_QUEUE`: RabbitMQ queue name
* `__SERVICE_MQ_USER`:  RabbitMQ user
* `__SERVICE_MQ_PASSWORD`: RabbitMQ password
* `__SERVICE_MQ_EXCHANGE`: RabbitMQ exchange (For dead letter queue feature)
* `__SERVICE_MQ_ROUTING_KEY`: RabbitMQ routing key (For dead letter queue feature)
* `__SERVICE_SQLALCHEMY_DATABASE_URI`: SQLAlchemy database URI
* `__SERVICE_DB_TABLE_NAME`: Database table name
* `__SERVICE_API_TITLE`: Swagger UI title
* `__SERVICE_API_VERSION`: API version
* `__SERVICE_OPENAPI_URL_PREFIX`: OpenAPI URL prefix
* `__SERVICE_OPENAPI_SWAGGER_UI_PATH`: Swagger UI path
* `__SERVICE_OPENAPI_JSON_PATH`: OpenAPI JSON path
* `__SERVICE_OPENAPI_SWAGGER_UI_URL`: Swagger UI Library URL
* `__SERVICE_ACTUATOR_BASE_URI`: Actuator base URI