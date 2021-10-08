FROM python:latest

WORKDIR /app

# Install poetry
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock /app/
RUN poetry config virtualenvs.create false

# Install deps
RUN poetry install --no-dev
RUN python -m dostoevsky download fasttext-social-network-model fasttext-toxic-model


COPY ./mediator /app/mediator

EXPOSE 8000
CMD ["uvicorn", "mediator.main:app", "--host", "0.0.0.0", "--port", "8000"]
