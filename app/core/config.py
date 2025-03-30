from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    #db
    DB_URL:str = os.getenv("DB_URL")
    DB_ECHO:bool = os.getenv("DB_ECHO")
    DB_AUTOFLUSH: bool = os.getenv("DB_AUTOFLUSH")
    DB_AUTOCOMMIT: bool = os.getenv("DB_AUTOCOMMIT")
    DB_EXPIRE_ON_COMMIT: bool  = os.getenv("DB_EXPIRE_ON_COMMIT")

    #postgres
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")

    #auth
    SECRET_KEY:str = os.getenv("SECRET_KEY")
    ALGORITHM:str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES:int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    
    #minio
    MINIO_ENDPOINT:str = os.getenv("MINIO_ENDPOINT")
    MINIO_ACCES_KEY:str = os.getenv("MINIO_ACCES_KEY")
    MINIO_SECRET_KEY:str = os.getenv("MINIO_SECRET_KEY")
    MINIO_PORT:str = os.getenv("MINIO_PORT")
    class Config:
        env_file = ".env"


settings = Settings()