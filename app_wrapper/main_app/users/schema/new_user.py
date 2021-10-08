from ...extensions import ma


class NewUserSchema(ma.Schema):
    first_name = ma.String()
    last_name = ma.String()
    email = ma.String(required=True)
    password = ma.String(required=True)
