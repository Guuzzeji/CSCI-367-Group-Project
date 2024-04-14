from flask import Blueprint, Response, request

api = Blueprint("api", __name__, url_prefix="/API")


@api.route("/manga/<int:book_id>", methods=["GET"])
def manga_info(book_id):
    return Response("bookid = " + str(book_id), status=200, mimetype="text/plain")

# ! Query setup
# * Example url /API/search=helloworld?type=author&page=10
# - type = title | author | theme | genre, defualt is title
# - page = some int, default is 1
@api.route("/search=<string:query>", methods=["GET"])
def search(query):
    return Response("query = " + str(query) + " | args = " + str(request.args), status=200, mimetype="text/plain")
