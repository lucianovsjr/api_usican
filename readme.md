# Init
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata seed/*.json
```

# Create seed
```bash
python manage.py dumpdata configurator.CustomOption --indent 4 > seed/0001_test.json
```

# load seed
```bash
python manage.py loaddata seed/0001_test.json
```
