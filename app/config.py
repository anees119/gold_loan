import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "development-only-change-this")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "development-jwt-change-this")
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USER', 'root')}:"
        f"{os.getenv('DB_PASSWORD', '')}@{os.getenv('DB_HOST', '127.0.0.1')}:"
        f"{os.getenv('DB_PORT', '3307')}/{os.getenv('DB_NAME', 'gold_crm')}?charset=utf8mb4"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.getenv("FLASK_DEBUG", "0") == "1"
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 60 * 8
