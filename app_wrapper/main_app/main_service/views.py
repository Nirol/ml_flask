from flask_restx import Namespace

from ..main_service.resources import HellowWorldResource

ns = Namespace("hello_world", description="Hello world name space")

ns.add_resource(HellowWorldResource, "/", endpoint="hello_world")

