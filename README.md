# nakiri

Flask API with JWT authentication

## Setup

1. Generate a JWT signing key.

```bash
$(/usr/bin/env python -c 'import secrets; print(f"export NAKIRI_KEY={secrets.token_urlsafe(64)}")')
```

If you're using Docker, generate the key before spinning up the containers.
