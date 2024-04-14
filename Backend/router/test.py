from flask import Blueprint, Response

test = Blueprint("test", __name__, url_prefix="/TEST")


@test.route("/ping", methods=["GET"])
def ping_test():
    return Response("pong", status=200, mimetype="text/plain")
