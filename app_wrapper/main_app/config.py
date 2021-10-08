"""Default configuration

Use env var to override
"""
import os

from dotenv import load_dotenv
# load_dotenv()


# Flask
ENV = os.getenv("FLASK_ENV")
DEBUG = ENV == "development"
SECRET_KEY = os.getenv("SECRET_KEY")
ALLOWED_ORIGINS = "*" if ENV == "development" or ENV == "staging" or ENV == "test" else None
SECRET_KEY = os.getenv("SECRET_KEY")


# DB
MONGO_URI = os.getenv("MONGO_URI")