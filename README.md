# nakiri

Flask API with JWT authentication

## Setup

1. Get Python 3.7 and install pipenv
2. Generate a JWT signing key.

```bash
$(/usr/bin/env python -c 'import secrets; print(f"export NAKIRI_KEY={secrets.token_urlsafe(64)}")')
```

3. Set the Postgres password with `export NAKIRI_DB_PASSWORD=hunter2`

4. Spin up the Docker containers

```bash
docker-compose up -d
```

If the Dockerfile or dependencies have changed, rebuild the images with

```bash
docker-compose up -d --build
```

## Hack away

The Flask app spins up in debug mode by default, so it watches for changes and reloads appropriately. If you want to keep an eye on logs, spin the containers up without the `-d` flag, i.e. `docker-compose up`


#### Reinit database

A really quick and easy way to mess with table schemas is to change the database URI and reinitialize the database. E.g.

```diff
- app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
+ app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test2.db'
```

And then running the `db init` command on the container. You can skip pulling the containers down and spinning them back up with `docker exec -it nakiri pipenv run flask db init --yes`


#### `print()` debugging

The `util.py` file contains a function called `print_d` that prints to `stderr`. Printing to `stdout` doesn't show up in the log stream since presumably Flask completely hijacks it. You can print to `stderr` and it shows up in the logstream instead.

What are debuggers anyways?
