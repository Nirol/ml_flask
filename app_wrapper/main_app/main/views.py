import logging
from flask import Blueprint, jsonify

blueprint = Blueprint("main", __name__)
logger = logging.getLogger(__name__)


@blueprint.route("/", methods=["GET"])
def health_check():
    return jsonify("root api")
