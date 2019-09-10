All required libraries are in `requirements.txt`

To run project please follow the instructions:

1. clone repo from `git clone -b feature/team-app https://github.com/megapixar/django-test`
2. make sure that you are in `django-test` directory and run `python3.7 -m venv venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`
6. `cd app`
5. `python manage.py migrate`
6. `echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'admin')" | python manage.py shell`
7. `python manage.py runserver`

To run test `python ./manage.py test` from `django-test/app` directory

By default is used dev config from `teams.settings.dev`

I implemented 3 endpoints:

1. Login

```
POST http://localhost:8000/api/v1/login
Content-Type: application/json

{
  "username": "USERNAME",
  "password": "PASS"
}
```

Example response:

```json
{
  "data": {
    "token": "254159653a63c381c2ea6af8539a0dd99f2d2068"
  }
}
```

2. POST to send happiness, valid values (1,3,5), you have to be authorised so `Authorization` required.
Return statistic of your team

```
POST http://localhost:8000/api/v12/{{TEAM_SLUG}}/happiness
Authorization: Token {{auth_token}}
Content-Type: application/json

{
  "happiness": 1
}
```

Example response:
```json
{
  "data": {
    "happy": 1,
    "neutral": 2,
    "unhappy": 1,
    "average_happiness": 3.0
  }
}
```

3. GET to see the statics of team

```
GET http://localhost:8000/api/v12/{{TEAM_SLUG}}/happiness
```

Example response:
```json
{
  "data": {
    "happy": 1,
    "neutral": 2,
    "unhappy": 1,
    "average_happiness": 3.0
  }
}
```

4. Admin console to login pls use login `admin` and pass `admin`

```
GET http://localhost:8000/admin
```