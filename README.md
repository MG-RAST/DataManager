# DataManager

## Useful django manage commands

```
# Start server:
docker-compose run web manage start

# Initialize db:
docker-compose run web manage migrate

# Create initial admin user:
docker-compose run web manage createsuperuser 

# Python shell on container:
docker-compose run web manage shell

# DB shell on container:    
docker-compose run web manage dbshell 

# Run `manage` without arguement for a full list of commands:
docker-compose run web manage
```


