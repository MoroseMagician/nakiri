# nakiri

Flask API with JWT authentication

## Setup

1. Get Python 3.7 and install pipenv
2. Generate a JWT signing key.

```bash
$(/usr/bin/env python -c 'import secrets; print(f"export NAKIRI_KEY={secrets.token_urlsafe(64)}")')
```

3. Set the Postgres password with `export NAKIRI_DB_PASSWORD=hunter2`

4. Set the Postgres connection string with `export NAKIRI_DB="postgres://postgres:hunter2@nakiri-db:5432/nakiri"`

5. Spin up the Docker containers

```bash
docker-compose up -d
```

If the Dockerfile or dependencies have changed, rebuild the images with

```bash
docker-compose up -d --build
```

6. Run migrations `docker exec -it pipenv run flask db upgrade`

## Hack away

The Flask app spins up in debug mode by default, so it watches for changes and reloads appropriately. If you want to keep an eye on logs, spin the containers up without the `-d` flag, i.e. `docker-compose up`

The database is mounted on a volume, so it should persist through restarts as long as you don't run `docker system prune -af` or something.

### Database stuff

Nakiri uses Flask-Migrate which uses Alembic under the hood. Migrations are generated with the `flask db migrate` command or the `flask db revision` command. `flask db migrate` autogenerates migrations from changes in the models, but it's pretty limited in what it can pick up, e.g. column types are really finnicky.

Migrations are kept under the `/migrations` folder (waow!), to run the migrations, just run `flask db upgrade`.

Note that you can connect to the Postgres database from the host, using something like pgAdmin, at `localhost:5432`

#### `print()` debugging

The `util.py` file contains a function called `print_d` that prints to `stderr`. Printing to `stdout` doesn't show up in the log stream since presumably Flask completely hijacks it. You can print to `stderr` and it shows up in the logstream instead.

What are debuggers anyways?
