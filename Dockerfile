FROM python:3.7

WORKDIR /app
COPY Pipfile.lock Pipfile.lock
COPY Pipfile Pipfile

RUN pip install pipenv
RUN pipenv install --system --deploy
