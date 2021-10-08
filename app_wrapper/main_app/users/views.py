from flask_restx import Namespace
from .resources.user_login import UserLoginResource
from .resources.user_register import UserRegisterResource

ns = Namespace("users", description="Hello world name space")

ns.add_resource(UserLoginResource, "/login", endpoint="user_login")
ns.add_resource(UserRegisterResource, "/register", endpoint="user_register")

