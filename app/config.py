import os

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://user:password@db:3306/fastapi")

settings = Settings()
