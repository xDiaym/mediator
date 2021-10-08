# Mediator

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)  
Mediator is a Russian aggressive texts filtering library.

This app use [Dostoevsky](https://github.com/bureaucratic-labs/dostoevsky) to detect aggression in text.

## API
Use API documentation in app. Open `http://localhost:8000/redoc` in browser after installation. 

## Build
Using docker:
```shell
docker built -t mediator .
```

or manually:
```shell
poetry install
python -m dostoevsky download fasttext-social-network-model fasttext-toxic-model
```

## Run
With docker:
```shell
docker run -d --name mediator-container -p 8000:8000 mediator
```

or manually:
```shell
uvicorn mediator.main:app --host 0.0.0.0 --port 8000
```

# License
Licensed under [MIT](./LICENSE).
