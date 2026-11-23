# Setup project

Make sure you have [python](https://www.python.org/) and [uv](https://docs.astral.sh/uv/) (package manager) installed.

Create the database (sqlite) :
```sh
uv run python manage.py migrate
```

Optionnal, Create super user (this user is needed only for the [Django admin interface](http://localhost:8000/admin/)) :
```sh
uv run python manage.py createsuperuser
```

# Run dev server :

```sh
uv run python manage.py runserver
```


# Run tests :

```sh
uv run python manage.py test
```
