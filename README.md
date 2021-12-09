#Change-Event Query

## How it Works?
This project written with [Flask web framework](https://flask.palletsprojects.com/en/2.0.x/). It use [flask-smorest](https://flask-smorest.readthedocs.io/en/latest/index.html) for REST API, [Pyctuator](https://github.com/SolarEdgeTech/pyctuator) for actuator endpoint and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) for handle DB queries. Swagger UI documentation and API validations handled by flask-smorest itself. flask-smorest uses [Marshmallow](https://marshmallow.readthedocs.io/en/stable/index.html) models for marshalling and unmarshalling objects in request and response. This models also used by Swagger UI and [Pika](https://pika.readthedocs.io/en/stable/).
##Run In Development Environments

Open project in PyCharm, set environment variables and run `app.py`

##Environment Variables
* AMQP_HOST : Set host name of rabbitmq
* AMQP_VIRTUAL_HOST: Set virtual host name of rabbitmq
* AMQP_QUEUE: Set queue name of rabbitmq
* AMQP_USER:  Set username of rabbitmq
* AMQP_PASSWORD: Set password of rabbitmq
* AMQP_EXCHANGE: Set exchange of rabbitmq
* AMQP_ROUTING_KEY: Set routing key of rabbitmq
* TBL_NAME: Set table name to insert
* API_TITLE=Set api name;
* API_VERSION= Set api version;
* OPENAPI_URL_PREFIX= Set Open api url prefix
* OPENAPI_SWAGGER_UI_PATH=Set Open api url prefix
* OPENAPI_JSON_PATH= Set open api json path
* OPENAPI_SWAGGER_UI_URL= Set swagger ui url
* ACTUATOR_BASE_URI= Set actuator base url
* POSTGRES_USER= Set username of database
* POSTGRES_URL= Set url of database
* POSTGRES_PASS= Set password of database
* POSTGRES_DB= Set db name of database

Other application settings in [config.py](change_event_query/config.py)