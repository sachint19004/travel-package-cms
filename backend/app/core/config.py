from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str

    SECRET_KEY: str
    ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    GEMINI_API_KEY: str | None = None

    OLLAMA_MODEL: str = "qwen2.5:7b"

    class Config:
        env_file = ".env"


settings = Settings()