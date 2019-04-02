# DataManager
 
## Getting started

Create a local directory for persisent postgres data. Copy `env-template` to `.env` and fill in `###REQUIRED###` values. A new django secret key can be generated at https://djskgen.herokuapp.com/.

### Start server:
```docker-compose up```

### Initialize db:
```docker-compose exec django python manage.py migrate```

### Create initial admin user:
```docker-compose exec django python manage.py createsuperuser``` 


## Other useful commands

### Python shell on container:
```docker-compose exec django python manage.py shell```

### DB shell on container:    
```docker-compose exec django python manage.py dbshell```

### Run `manage` without arguement for a full list of commands:
```docker-compose exec django python manage.py```



