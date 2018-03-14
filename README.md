crawler-ml
=====================

## About

Special crawler to get some public information from mercado libre.

## Dependecies

* [**Docker**](https://www.docker.com/)
* [**Scrapy**](https://scrapy.org/)

## Installing

After cloning the project, on the root, run:

```
cp .env.example .env
```

```
docker-compose -f docker-compose.yml up --build -d
```

## Running integration tests

The integration tests can be running with:

```
behave tests/integration
```

## Start crawler

To start crawler, just follow bellow:

```
python crawler_ml.py start
```

## Contributing

Please contribute ! :)

Read the contribution standards, on [**CONTRIBUING.md**](./CONTRIBUTING.md)


