FROM python:3.7

WORKDIR /app
COPY Pipfile.lock Pipfile.lock
COPY Pipfile Pipfile
COPY entrypoint.sh entrypoint.sh

RUN chmod +x entrypoint.sh
RUN pip install pipenv
RUN pipenv install --system --deploy
