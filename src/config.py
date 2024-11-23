from os import getenv

from dotenv import load_dotenv


load_dotenv()


class Settings():
    API_KEY: str = getenv("api_key", "")
    DB_URL: str = f"postgresql://postgres:{getenv('database_password')}@localhost:5432/postgres"  # noqa: E501
    BACKUP_COUNT: int = 3
    MAX_BYTES_PER_FILE: int = 4 * 1024 * 1024


settings: Settings = Settings()
