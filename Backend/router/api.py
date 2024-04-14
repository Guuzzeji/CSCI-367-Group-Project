from flask import Blueprint, Response, request
from db.mysql import get_manga_info, search_for_manga

api = Blueprint("api", __name__, url_prefix="/API")


@api.route("/manga/<int:book_id>", methods=["GET"])
def manga_info(book_id: int):

    # impliment get_manga_info

    return Response("bookid = " + str(book_id), status=200, mimetype="text/plain")

# ! Query setup
# NOTE: limit number of manga return to be 25 to 50
# * Example url /API/search?query=helloworld&type=author&lastbookid=10
# - type = title | author | theme | genre, defualt is title
# - lastbookid = some int, default is 1
# - query = user search term, this is required to run
@api.route("/search", methods=["GET"])
def search():

    # impliment search_for_manga

    return Response("args = " + str(request.args), status=200, mimetype="text/plain")
