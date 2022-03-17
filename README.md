# Kaboom Python

A Kaboom API Python wrapper. This wrapper implements all of the endpoints (comics, cartoons and accounts) for Kaboom in an easy to use manner.

## Installation

## Basic Usage

**Searching for a comic**

```python
from kaboompython.base import Base
from kaboompython.comics import ComicsClient

kaboom = Base()
# The url to the Kaboom instance. If this is not provided it will default to the staging instance
kaboom.url = "http://127.0.0.1:8000"

# Search for the comic 'Fables'
data = ComicsClient().get_comics(query='fables')
print(data)
```

**Logging in**

```python
from kaboompython.base import Base

kaboom = Base()

# Log in as the staging demo user. This saves the users access token as an environment variable and automatically authenticates auth required requests.
user = kaboom.login(username='demo', password='kaboom123')
# Securely save the access token if needed
print(user['token'])
```

If you already have the users access token you can just set it like this and avoid making an api call with user credentials:

```python
kaboom.access_token - 'aabbccggeeffgghhiijjkkllmmnnooppqqrrsstt'
```

**Signing up**

```python
from kaboompython.base import Base

kaboom = Base()

# Creates an account, then logs the user in automatically
user = kaboom.signup(username='tmp', password='super_strong_password', email='tmp@example.com')
# Securely save the access token if needed
print(user['token'])
```