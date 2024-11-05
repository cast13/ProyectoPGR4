import os

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    # Puedes agregar más configuraciones aquí

settings = Settings() 