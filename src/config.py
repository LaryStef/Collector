# flake8: noqa

from os import getenv

from dotenv import load_dotenv


load_dotenv()

API_KEY: str = getenv("api_key")
DB_URL: str = f"postgresql://postgres:{getenv('database_password')}@localhost:5432/postgres"
