from flask import Blueprint, Response

# ! == About ==
# A simple test handler for testing connection between client and this web server.

test = Blueprint("test", __name__, url_prefix="/TEST")


@test.route("/ping", methods=["GET"])
def ping_test():
    return Response("pong", status=200, mimetype="text/plain")
