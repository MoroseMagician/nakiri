# nakiri

Flask API with JWT authentication

## Setup

1. Get Python 3.7 and install pipenv
2. `pipenv install`
3. Generate a JWT signing key.

```bash
$(/usr/bin/env python -c 'import secrets; print(f"export NAKIRI_KEY={secrets.token_urlsafe(64)}")')
```

4. Spin up the Docker containers

```bash
docker-compose up -d
```

If the Dockerfile or dependencies have updated, rebuild the images with

```bash
docker-compose up -d --build
```

## Hack away

The Flask app spins up in debug mode by default, so it watches for changes and reloads appropriately. If you want to keep an eye on logs, spin the containers up without the `-d` flag, i.e. `docker-compose up`
