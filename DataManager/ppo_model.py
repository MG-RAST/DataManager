from django.db import models


class PPOModel(models.Model):
    '''
    Base class for PPOModels
    '''

    class Meta:
        abstract = True

    # Base
    _id = models.IntegerField()


class Backend(PPOModel):
    '''
    Table: Backend 

        fields:
            _id, name

        sql:
            CREATE TABLE `Backend` (
            `_id` int(11) NOT NULL AUTO_INCREMENT,
            `name` varchar(64) DEFAULT NULL,
            PRIMARY KEY (`_id`),
            UNIQUE KEY `Backend_unique_0` (`name`)
            ) ENGINE=InnoDB AUTO_INCREMENT=435 DEFAULT CHARSET=latin1;
    '''
    name = models.CharField()
    

class Invitation(PPOModel):
    '''
    Table: Invitation 

        fields:
            _id, invitation_date, email, user_claimed, _user_claim_db, user_inviting, _user_inviting_db, 
            claimed, scope, _scope_db

        sql:
            CREATE TABLE `Invitation` (
            `_id` int(11) NOT NULL AUTO_INCREMENT,
            `invitation_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            `email` varchar(255) DEFAULT NULL,
            `user_claimed` int(11) DEFAULT NULL,
            `_user_claimed_db` int(11) DEFAULT NULL,
            `user_inviting` int(11) DEFAULT NULL,
            `_user_inviting_db` int(11) DEFAULT NULL,
            `claimed` tinyint(1) DEFAULT NULL,
            `scope` int(11) DEFAULT NULL,
            `_scope_db` int(11) DEFAULT NULL,
            `invitation_string` varchar(255) DEFAULT NULL,
            PRIMARY KEY (`_id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
    '''
    invitation_date = models.DateTimeField()
    email = models.CharField()
    user_claimed = models.IntegerField()
    _user_claimed_db = models.IntegerField()
    user_inviting = models.IntegerField()
    _user_inviting_db = models.IntegerField()
    claimed = models.IntegerField()
    scope = models.IntegerField()
    _scope_db = models.IntegerField()
    invitation_string = models.CharField()


class Organization(PPOModel):
    '''
    Table: Organization

        fields:
            _id, country, city, date, url, name, abbreviation, scope, _scope_db, location

        sql:
            CREATE TABLE `Organization` (
            `_id` int(11) NOT NULL AUTO_INCREMENT,
            `country` varchar(128) DEFAULT NULL,
            `city` varchar(128) DEFAULT NULL,
            `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            `url` varchar(255) DEFAULT NULL,
            `name` varchar(255) DEFAULT NULL,
            `abbreviation` varchar(255) DEFAULT NULL,
            `scope` int(11) DEFAULT NULL,
            `_scope_db` int(11) DEFAULT NULL,
            `location` varchar(128) DEFAULT NULL,
            PRIMARY KEY (`_id`),
            UNIQUE KEY `Organization_unique_0` (`name`)
            ) ENGINE=InnoDB AUTO_INCREMENT=6624 DEFAULT CHARSET=latin1;
    '''
    country = models.CharField()
    city = models.CharField()
    date = models.DateTimeField()
    url = models.CharField()
    name = models.CharField()
    abbreviation = models.CharField()
    scope = models.IntegerField()
    _scope_db = models.IntegerField()    
    location = models.CharField()


class OrganizationUsers(PPOModel):
    '''
    Table: OrganizationUsers

        fields:
            _id, user, _user_db, organization, _organization_db

        sql:
            CREATE TABLE `OrganizationUsers` (
            `_id` int(11) NOT NULL AUTO_INCREMENT,
            `user` int(11) DEFAULT NULL,
            `_user_db` int(11) DEFAULT NULL,
            `organization` int(11) DEFAULT NULL,
            `_organization_db` int(11) DEFAULT NULL,
            PRIMARY KEY (`_id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=36923 DEFAULT CHARSET=latin1;
    '''
    user = models.IntegerField()
    _user_db = models.IntegerField()
    organization = models.IntegerField()
    _organization_db = models.IntegerField()


class Preferences(PPOModel):
    '''
    Table: Preferences

        fields:
            _id, value, user, _user_db, application, _application_db, name

        sql:
            CREATE TABLE `Preferences` (
            `_id` int(11) NOT NULL AUTO_INCREMENT,
            `value` varchar(255) DEFAULT NULL,
            `user` int(11) DEFAULT NULL,
            `_user_db` int(11) DEFAULT NULL,
            `application` int(11) DEFAULT NULL,
            `_application_db` int(11) DEFAULT NULL,
            `name` varchar(255) DEFAULT NULL,
            PRIMARY KEY (`_id`),
            KEY `Preferences_user` (`user`,`_user_db`),
            KEY `Preferences_name` (`name`),
            KEY `Preferences_value` (`value`)
            ) ENGINE=InnoDB AUTO_INCREMENT=1786443 DEFAULT CHARSET=latin1;
    '''
    value = models.CharField()
    user = models.IntegerField()
    _user_db = models.IntegerField()
    application = models.IntegerField()
    _application_db = models.IntegerField()    
    name = models.CharField()


class Rights(PPOModel):
    '''
    Table: Rights

        fields:
            _id, granted, delegated, data_id, data_type, application, _application_db, name, scope, _scope_db

        sql:
            CREATE TABLE `Rights` (
            `_id` int(11) NOT NULL AUTO_INCREMENT,
            `granted` tinyint(1) DEFAULT NULL,
            `delegated` tinyint(1) DEFAULT NULL,
            `data_id` varchar(255) DEFAULT NULL,
            `data_type` varchar(255) DEFAULT NULL,
            `application` int(11) DEFAULT NULL,
            `_application_db` int(11) DEFAULT NULL,
            `name` varchar(255) DEFAULT NULL,
            `scope` int(11) DEFAULT NULL,
            `_scope_db` int(11) DEFAULT NULL,
            PRIMARY KEY (`_id`),
            KEY `rights_scope_idx` (`scope`),
            KEY `Rights_data_type` (`data_type`),
            KEY `Rights_data_id` (`data_id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=4562521 DEFAULT CHARSET=latin1;
    '''
    granted = models.BooleanField()
    delegated = models.BooleanField()
    data_id = models.CharField()
    data_type = models.CharField()
    application = models.IntegerField()
    _application_db = models.IntegerField()
    name = models.CharField()
    scope = models.IntegerField()
    _scope_db = models.IntegerField()


class Scope(PPOModel):
    '''
    Table: Scope

        fields:
            _id, application, _application_db, name, description

        sql:
            CREATE TABLE `Scope` (
            `_id` int(11) NOT NULL AUTO_INCREMENT,
            `application` int(11) DEFAULT NULL,
            `_application_db` int(11) DEFAULT NULL,
            `name` varchar(255) DEFAULT NULL,
            `description` text,
            PRIMARY KEY (`_id`),
            UNIQUE KEY `Scope_unique_0` (`name`,`application`)
            ) ENGINE=InnoDB AUTO_INCREMENT=165536 DEFAULT CHARSET=latin1;
    '''
    application = models.IntegerField()
    _application_db = models.IntegerField()
    name = models.CharField()
    description = models.CharField()


class Session(PPOModel):
    '''
    Table: Session

        fields:
            _id, session_id, user, _user_db, creation

        sql:
            CREATE TABLE `Session` (
            `_id` int(11) NOT NULL AUTO_INCREMENT,
            `session_id` varchar(32) DEFAULT NULL,
            `user` int(11) DEFAULT NULL,
            `_user_db` int(11) DEFAULT NULL,
            `creation` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (`_id`),
            UNIQUE KEY `Session_unique_0` (`session_id`,`user`)
            ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
    '''
    session_id = models.CharField()
    user = models.IntegerField()
    _user_db = models.IntegerField()
    creation = models.DateTimeField()


class SessionItem(PPOModel):
    '''
    Table: SessionItem

        fields:
            _id, parameters, page, timestamp

        sql:
            CREATE TABLE `SessionItem` (
            `_id` int(11) NOT NULL AUTO_INCREMENT,
            `parameters` text,
            `page` varchar(255) DEFAULT NULL,
            `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (`_id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
    '''
    parameters = models.CharField()
    page = models.CharField()
    timestamp = models.DateTimeField()


class Session_entries(PPOModel):
    '''
    Table: Session_entries

        fields:
            _id, _array_index, _target_id, _source_id, _target_db

        sql:
            CREATE TABLE `Session_entries` (
            `_id` int(11) NOT NULL AUTO_INCREMENT,
            `_array_index` int(11) DEFAULT NULL,
            `_target_id` int(11) DEFAULT NULL,
            `_source_id` int(11) DEFAULT NULL,
            `_target_db` int(11) DEFAULT NULL,
            PRIMARY KEY (`_id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
    '''
    _array_index = models.IntegerField()
    _target_id = models.IntegerField()
    _source_id = models.IntegerField()
    _target_db = models.IntegerField()


class User(PPOModel):
    '''
    Table: User

        fields:
            _id, firstname, email, password, comment, entry_date, active, lastname, login, email2

        sql:
            CREATE TABLE `User` (
            `_id` int(11) NOT NULL AUTO_INCREMENT,
            `firstname` varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
            `email` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
            `password` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
            `comment` mediumtext COLLATE utf8mb4_unicode_ci,
            `entry_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            `active` tinyint(1) DEFAULT NULL,
            `lastname` varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
            `login` varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
            `email2` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
            PRIMARY KEY (`_id`),
            UNIQUE KEY `User_unique_0` (`login`),
            UNIQUE KEY `User_unique_1` (`email`)
            ) ENGINE=InnoDB AUTO_INCREMENT=71290 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
    '''
    firstname = models.CharField()
    email = models.CharField()
    password = models.CharField()    
    comment = models.CharField()    
    entry_date = models.DateTimeField()
    active = models.BooleanField()
    lastname = models.CharField()
    login = models.CharField()
    email2 = models.CharField()


class UserHasScope(PPOModel):
    '''
    Table: UserHasScope

        fields:
            _id, user, _user_db, scope, _scope_db, granted

        sql:
            CREATE TABLE `UserHasScope` (
            `_id` int(11) NOT NULL AUTO_INCREMENT,
            `user` int(11) DEFAULT NULL,
            `_user_db` int(11) DEFAULT NULL,
            `scope` int(11) DEFAULT NULL,
            `_scope_db` int(11) DEFAULT NULL,
            `granted` tinyint(1) DEFAULT NULL,
            PRIMARY KEY (`_id`),
            UNIQUE KEY `UserHasScope_unique_0` (`user`,`scope`)
            ) ENGINE=InnoDB AUTO_INCREMENT=83299 DEFAULT CHARSET=latin1;
    '''
    user = models.IntegerField()
    _user_db = models.IntegerField() 
    scope = models.IntegerField()
    _scope_db = models.IntegerField()    
    granted = models.BooleanField()


class UserSession(PPOModel):
    '''
    Table: UserSession

        fields:
            _id, error_page, session_id, error_parameters, current_page, timestamp, previous_page, user, 
            _user_db, current_parameters, previous_parameters 

        sql:
        CREATE TABLE `UserSession` (
        `_id` int(11) NOT NULL AUTO_INCREMENT,
        `error_page` varchar(255) DEFAULT NULL,
        `session_id` varchar(32) DEFAULT NULL,
        `error_parameters` text,
        `current_page` varchar(255) DEFAULT NULL,
        `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        `previous_page` varchar(255) DEFAULT NULL,
        `user` int(11) DEFAULT NULL,
        `_user_db` int(11) DEFAULT NULL,
        `current_parameters` text,
        `previous_parameters` text,
        PRIMARY KEY (`_id`),
        UNIQUE KEY `UserSession_unique_0` (`session_id`),
        UNIQUE KEY `UserSession_unique_1` (`session_id`,`user`,`_user_db`),
        KEY `sess_key` (`_user_db`,`user`)
        ) ENGINE=InnoDB AUTO_INCREMENT=139945626 DEFAULT CHARSET=latin1;
    '''
    error_page = models.CharField()
    session_id = models.CharField()    
    error_parameters = models.CharField()
    current_page = models.CharField()
    timestamp = models.DateTimeField()
    previous_page = models.CharField()
    user = models.IntegerField()
    _user_db = models.IntegerField()
    current_parameters = models.CharField()
    previous_parameters = models.CharField()


class _metainfo(PPOModel):
    '''
    Table: _metainfo

        fields:
            _id, info_name, info_value

        sql:
            CREATE TABLE `_metainfo` (
            `_id` int(11) NOT NULL AUTO_INCREMENT,
            `info_name` varchar(255) DEFAULT NULL,
            `info_value` varchar(255) DEFAULT NULL,
            PRIMARY KEY (`_id`),
            KEY `_metainfo_info_name` (`info_name`)
            ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
    '''
    info_name = models.CharField()
    info_value = models.CharField()    


class _objects(PPOModel):
    '''
    Table: _objects

        fields:
            _id, objects

        sql:
            CREATE TABLE `_objects` (
            `_id` int(11) NOT NULL AUTO_INCREMENT,
            `object` varchar(255) DEFAULT NULL,
            PRIMARY KEY (`_id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
    '''
    pass


class _references(PPOModel):
    '''
    Table: _references

        fields:
            _id, _database, _backend_type, _backend_data

        sql:
            CREATE TABLE `_references` (
            `_id` int(11) NOT NULL AUTO_INCREMENT,
            `_database` varchar(512) DEFAULT NULL,
            `_backend_type` varchar(255) DEFAULT NULL,
            `_backend_data` varchar(1024) DEFAULT NULL,
            PRIMARY KEY (`_id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
    '''
    _database = models.CharField()
    _backend_type = models.CharField()
    _backend_data = models.CharField()