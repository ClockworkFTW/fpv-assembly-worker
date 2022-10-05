import os
from dotenv import load_dotenv

load_dotenv()

env = os.environ.get("PYTHON_ENV")

postgres = (
    {
        "database": os.getenv("POSTGRES_DATABASE_PROD"),
        "user": os.getenv("POSTGRES_USER_PROD"),
        "password": os.getenv("POSTGRES_PASSWORD_PROD"),
        "host": os.getenv("POSTGRES_HOST_PROD"),
        "port": os.getenv("POSTGRES_PORT_PROD"),
    }
    if env == "production"
    else {
        "database": os.getenv("POSTGRES_DATABASE_DEV"),
        "user": os.getenv("POSTGRES_USER_DEV"),
        "password": os.getenv("POSTGRES_PASSWORD_DEV"),
        "host": os.getenv("POSTGRES_HOST_DEV"),
        "port": os.getenv("POSTGRES_PORT_DEV"),
    }
)

uuid_namespace = os.getenv("UUID_NAMESPACE")
