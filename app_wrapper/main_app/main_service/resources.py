from flask import current_app, session
from flask_restx import Resource
from ..extensions import api, mongo



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