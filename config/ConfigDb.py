import os
from dotenv import load_dotenv

load_dotenv()


class ConfigDB:
    POSTGRES_URL = os.environ['URL']
    POSTGRES_PRISMA_URL = os.environ['PRISMA']
    POSTGRES_URL_NON_POOLING = os.environ['NON_POOLING']
    POSTGRES_USER = os.environ['USER']
    POSTGRES_HOST = os.environ['HOST']
    POSTGRES_PASSWORD = os.environ['PASSWORD']
    POSTGRES_DATABASE = os.environ['DATABASE']