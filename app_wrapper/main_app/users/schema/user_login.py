from ...extensions import ma

class UserLoginSchema(ma.Schema):
    email = ma.String(required=True)
    password = ma.String(required=True)
