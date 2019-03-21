# DataManager

Initialize db:
```
docker-compose run web manage.py migrate
```

Create Admin user:
```
docker-compose run web manage.py createsuperuser 
```

Python shell on container:
```
docker-compose run web manage.py shell
```

