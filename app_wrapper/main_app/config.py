"""Default configuration

Use env var to override
"""
import os

from dotenv import load_dotenv

load_dotenv()

# Flask
ENV = os.getenv("FLASK_ENV")
DEBUG = ENV == "development"
SECRET_KEY = os.getenv("SECRET_KEY")
ALLOWED_ORIGINS = "*" if ENV == "development" or ENV == "staging" or ENV == "test" else r"^https://.+vacayz.com$"



# DB
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")