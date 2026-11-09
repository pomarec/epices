# Setup project

Create the database (sqlite) :
```sh
uv run python manage.py migrate
```

Create super user :
```sh
uv run python manage.py createsuperuser
```

# Run dev server :

```sh
uv run python manage.py runserver
```
