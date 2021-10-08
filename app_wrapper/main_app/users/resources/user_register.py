from typing import Dict

from flask import current_app, request, session
from flask_restx import Resource
from marshmallow import ValidationError

from ..schema.new_user import NewUserSchema
from ...extensions import api, mongo
import bcrypt


class UserRegisterResource(Resource):
    @api.response(201, description="User created successfully")
    def post(self):
        """
        create a new user
        """
        current_app.logger.debug(
            "Create a new user request received",
        )

        schema = NewUserSchema()
        user_info: Dict = schema.load(request.get_json())
        users = mongo.db.users
        existing_user = users.find_one({"email": user_info["email"]})
        if existing_user:
            raise ValidationError("Email already in use")
        hash_password = bcrypt.hashpw(user_info.pop("password").encode("utf-8"), bcrypt.gensalt())
        user_info["password"] = hash_password
        users.insert(user_info)
        session['user_email'] = user_info["email"]
        return "User created", 201