CREATE DATABASE 'datamanager_main';
CREATE USER 'datamanager_user' WITH ENCRYPTED PASSWORD 'datamanager_pw';
GRANT ALL PRIVILEGES ON DATABASE 'datamanager_main' TO 'datamanager_user';