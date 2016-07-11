import os

#---------------------------------------------------------
# Caravel specific config
#---------------------------------------------------------
ROW_LIMIT = int(os.getenv("ROW_LIMIT", 5000))
WEBSERVER_THREADS = int(os.getenv("WEBSERVER_THREADS", 8))

CARAVEL_WEBSERVER_PORT = int(os.getenv("CARAVEL_WEBSERVER_PORT", 8088))
#---------------------------------------------------------

#---------------------------------------------------------
# Flask App Builder configuration
#---------------------------------------------------------
# Your App secret key
SECRET_KEY = os.getenv("SECRET_KEY", "\2\1thisismyscretkey\1\2\e\y\y\h")

# The SQLAlchemy connection string.
DB_HOST = None
DB_PORT = None
DB_ADAPTER = None
DB_USER = os.getenv("DB_USER", None)
DB_PASS = os.getenv("DB_PASS", None)
DB_NAME = os.getenv("DB_NAME", None)

if os.getenv("MYSQL_PORT_3306_TCP_ADDR", None):
    DB_ADAPTER = "mysql"
    DB_HOST = "mysql"
    DB_PORT = os.getenv("MYSQL_PORT_3306_TCP_PORT", None)
elif os.getenv("POSTGRESQL_PORT_5432_TCP_ADDR", None):
    DB_ADAPTER = "postgresql"
    DB_HOST = "postgresql"
    DB_PORT = os.getenv("POSTGRESQL_PORT_5432_TCP_PORT", None)

if DB_HOST and DB_PORT and DB_USER and DB_PASS and DB_NAME:
    SQLALCHEMY_DATABASE_URI = "{}://{}:{}@{}/{}".format(DB_ADAPTER, DB_USER, DB_PASS, DB_HOST, DB_NAME)
else:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI", "sqlite:////home/caravel/db/caravel.db")

# Flask-WTF flag for CSRF
CSRF_ENABLED = os.getenv("CSRF_ENABLED", "1") in ("True", "true", "1")

# Whether to run the web server in debug mode or not
DEBUG = os.getenv("DEBUG", "0") in ("True", "true", "1")

# Import all the env variables prefixed with "CARAVEL_"
config_keys = [c for c in os.environ if c.startswith("CARAVEL_")]
for key in config_keys:
    globals()[key[8:]] = os.environ[key]
