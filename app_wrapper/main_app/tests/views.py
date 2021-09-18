import logging
from flask import Blueprint
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest

test_blueprint = Blueprint("test", __name__)

logger = logging.getLogger(__name__)

@test_blueprint.route("/test/werkzeug-bad-request-error", methods=["GET"])
def test_werkzeug_bad_request():
    raise BadRequest("werkzeug bad request error test")


@test_blueprint.route("/test/marshmallow-validation-error", methods=["GET"])
def test_validation_error():
    raise ValidationError(message="marshmallow validation error test")
