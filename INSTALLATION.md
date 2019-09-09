1. 
2. `python3.7 -m venv venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`
6. `cd app`
5. `python manage.py migrate`
6. `echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'admin')" | python manage.py shell`
7. `python manage.py runserver`