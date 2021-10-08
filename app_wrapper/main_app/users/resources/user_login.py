from typing import Dict
from flask import current_app, request, session
from flask_restx import Resource
from marshmallow import ValidationError

from ..schema.user_login import UserLoginSchema
from ...extensions import api, mongo
import bcrypt


class UserLoginResource(Resource):
    @api.response(200, description="User login successfully")
    def get(self):
        """
        create a new user
        """
        current_app.logger.debug(
            "Create a new user request received",
        )

        schema = UserLoginSchema()
        user_login_info: Dict = schema.load(request.get_json())
        users = mongo.db.users
        login_user = users.find_one({"email": user_login_info["email"]})


        if login_user and bcrypt.hashpw(user_login_info["password"].encode("utf-8"), login_user["password"].encode("utf-8")) == login_user["password"].encode("utf-8"):
            session["user_email"] = login_user["email"]
            return "User login successfully", 200
        else:
            raise ValidationError("Invalid Email/Password combination")
