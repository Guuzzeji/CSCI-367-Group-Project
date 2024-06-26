from flask import Blueprint, request
from db.get_manga_details import get_manga_details
from db.search_for_manga import search_for_manga
from flask import jsonify

# ! == About ==
# This is our API endpoints for the web server, this connects and hands request made from client to use items in the database

api = Blueprint("api", __name__, url_prefix="/API")

# ! == Query setup ==
# * Example url /API/manga/69
# - book_id is the id of the manga in the database
@api.route("/manga/<int:book_id>", methods=["GET"])
def manga_info(book_id: int):
    try:
        manga_details = get_manga_details(book_id)
        if manga_details:
            return manga_details, 200
        else:
            return jsonify({"error": "Manga not found"}), 404
            #return {"error": "Manga not found"}, 404

    except:
        return jsonify({"error": "Something bad happen",}), 400


# ! == Query setup ==
# NOTE: limit number of manga return to be 25 to 50
# * Example url /API/search?query=helloworld&type=author&lastbookid=10
# - type = title | author | theme | genre, defualt is title
# - lastbookid = some int, default is 1
# - query = user search term, this is required to run
@api.route("/search", methods=["GET"])
def search():
    try:
        query = request.args.get("query")
        search_type = request.args.get("type", "title")  # Default is title

        # ! Not using lask book id
        # last_book_id = request.args.get("lastbookid", 1)  # Default is 1 

        search_result = search_for_manga(search_type, query)
        return jsonify(search_result), 200

    except:
        return jsonify({"error": "Something bad happen",}), 400