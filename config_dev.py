class Config(object):
    DEBUG=True

    TOKEN_DOMAIN="127.0.0.1"

    PHP_DOMAIN="http://127.0.0.1:8888"
    LOCAL_DOMAIN="http://127.0.0.1:5000"

    SECRET_KEY="secret"
    TOKEN_TIMEOUT=5*60

    # After how much time should the user auth cache refresh (in seconds)
    CACHE_TIMEOUT=5*60

    USER_CACHE_ENABLED=True

    MYSQL_DATABASE_HOST="atcs-dev.bergen.org"
    MYSQL_DATABASE_USER="atcsdevb_devusr"
    MYSQL_DATABASE_PASSWORD="UEFCVQ!;a!b~"
    MYSQL_DATABASE_PORT=3306