from flask import current_app
from flask_restx import Resource
from ..extensions import api



class HellowWorldResource(Resource):
    @api.response(404, "Listing does not exists")
    def get(self, listing_id):
        """
        hellow world test api resource
        """
        current_app.logger.debug(
            "Listing data by listing_id request received",
            extra={"listing_id": listing_id},
        )
        return "HELLO WORLD", 200