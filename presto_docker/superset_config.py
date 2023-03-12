import os

# Set the path to the SQLite database file
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'superset.db')

# Enable Presto as a database backend
DATABASES = {
    'presto': {
        'name': 'Presto',
        'driver': 'presto',
        'host': 'presto',
        'port': 8080,
        'username': 'presto',
        'password': '',
        'extra': {
            'catalog': 'hive',
            'schema': 'default'
        }
    }
}

# Enable authentication for Superset
AUTH_TYPE = AUTH_LDAP
AUTH_LDAP_SERVER = 'ldap://ldap.example.com'
AUTH_LDAP_SEARCH = 'ou=People,dc=example,dc=com'
AUTH_LDAP_UID_FIELD = 'uid'
AUTH_LDAP_FIRSTNAME_FIELD = 'givenName'
AUTH_LDAP_LASTNAME_FIELD = 'sn'

# Set the timezone for Superset
TIMEZONE = 'UTC'

# Set the path to static files
STATIC_PATH = os.path.join(BASE_DIR, 'static')

# Set the maximum upload size for CSV files (in bytes)
CSV_FILE_MAX_BYTES = 1024 * 1024

# Enable caching for Superset
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_cache_',
    'CACHE_REDIS_HOST': 'redis',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': 1
}
