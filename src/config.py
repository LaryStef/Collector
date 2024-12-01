from os import getenv

from dotenv import load_dotenv


load_dotenv()


class Settings():
    API_KEY: str = getenv("API_KEY", "")
    DB_URL: str = f"postgresql://{getenv('POSTGRES_USER')}:{getenv('POSTGRES_PASSWORD')}@host.docker.internal:5432/{getenv('POSTGRES_NAME')}"  # noqa: E501

    BACKUP_COUNT: int = 3
    MAX_BYTES_PER_FILE: int = 4 * 1024 * 1024


settings: Settings = Settings()
