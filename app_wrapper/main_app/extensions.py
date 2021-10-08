"""Extensions registry

All extensions here are used as singletons and
initialized in application factory
"""

from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restx import Api
from flask_pymongo import PyMongo

mongo = PyMongo()
ma = Marshmallow()
migrate = Migrate()
api = Api(version="1.0.0", title="ML API", prefix="/api/v1")
