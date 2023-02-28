FROM python:3.10

WORKDIR /src

COPY pyproject.toml /src/pyproject.toml
COPY poetry.lock /src/poetry.lock

RUN pip install poetry
RUN poetry install

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]
