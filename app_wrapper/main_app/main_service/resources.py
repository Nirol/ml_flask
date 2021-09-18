from flask import current_app
from flask_restx import Resource
from ..extensions import api



class HellowWorldResource(Resource):
    @api.response(404, "Listing does not exists")
    def get(self):
        """
        hellow world test api resource
        """
        current_app.logger.debug(
            "Hellow world request received",
        )
        return "HELLO WORLD", 200