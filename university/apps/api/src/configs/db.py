from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    # Pydantic automatically maps uppercase env vars to these fields
    host: str = Field(default="localhost", validation_alias="DATABASE_HOST")
    port: int = Field(default=3306, validation_alias="DATABASE_PORT")
    user: str = Field(default="root", validation_alias="DATABASE_USER")
    password: str = Field(default="", validation_alias="DATABASE_PASSWORD")
    database: str = Field(default="university_db", validation_alias="DATABASE_NAME")

    @property
    def database_url(self) -> str:
        """Assembles the PyMySQL connection string dynamically."""
        return f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

    # Configuration to read from a local .env file
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


# Instantiate the settings class for use across the application
db_settings = DatabaseSettings()
