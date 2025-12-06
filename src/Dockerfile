#
FROM python:3.12-slim AS requirements-stage

#
WORKDIR /tmp

#
RUN pip install poetry poetry-plugin-export

#
COPY ./pyproject.toml ./poetry.lock* /tmp/

#
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

#
FROM python:3.12-slim

#
WORKDIR /code

#
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./src /code/src

#
CMD ["python", "-m", "src.main"]