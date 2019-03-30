from django.db.models import Model, IntegerField, CharField, BooleanField, DateTimeField


class PPOModel(Model):
    '''
    Base class for PPOModels
    '''
    _id = IntegerField()

    Meta:
        abstract = True


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
    name = CharField()
    

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
    invitation_date = DateTimeField()
    email = CharField()
    user_claimed = IntegerField()
    _user_claimed_db = IntegerField()
    user_inviting = IntegerField()
    _user_inviting_db = IntegerField()
    claimed = IntegerField()
    scope = IntegerField()
    _scope_db = IntegerField()
    invitation_string = CharField()


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
    country = CharField()
    city = CharField()
    date = DateTimeField()
    url = CharField()
    name = CharField()
    abbreviation = CharField()
    scope = IntegerField()
    _scope_db = IntegerField()    
    location = CharField()


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
    user = IntegerField()
    _user_db = IntegerField()
    organization = IntegerField()
    _organization_db = IntegerField()


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
    value = CharField()
    user = IntegerField()
    _user_db = IntegerField()
    application = IntegerField()
    _application_db = IntegerField()    
    name = CharField()


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
    granted = BooleanField()
    delegated = BooleanField()
    data_id = CharField()
    data_type = CharField()
    application = IntegerField()
    _application_db = IntegerField()
    name = CharField()
    scope = IntegerField()
    _scope_db = IntegerField()


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
    application = IntegerField()
    _application_db = IntegerField()
    name = CharField()
    description = CharField()


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
    session_id = CharField()
    user = IntegerField()
    _user_db = IntegerField()
    creation = DateTimeField()


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
    parameters = CharField()
    page = CharField()
    timestamp = DateTimeField()


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
    _array_index = IntegerField()
    _target_id = IntegerField()
    _source_id = IntegerField()
    _target_db = IntegerField()


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
    firstname = CharField()
    email = CharField()
    password = CharField()    
    comment = CharField()    
    entry_date = DateTimeField()
    active = BooleanField()
    lastname = CharField()
    login = CharField()
    email2 = CharField()


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
    user = IntegerField()
    _user_db = IntegerField() 
    scope = IntegerField()
    _scope_db = IntegerField()    
    granted = BooleanField()


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
    error_page = CharField()
    session_id = CharField()    
    error_parameters = CharField()
    current_page = CharField()
    timestamp = DateTimeField()
    previous_page = CharField()
    user = IntegerField()
    _user_db = IntegerField()
    current_parameters = CharField()
    previous_parameters = CharField()