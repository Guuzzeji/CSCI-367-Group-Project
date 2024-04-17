from db.connection import CONNECTION_TO_DB

# ! == About ==
# Handle getting more information about specifc manga in db

# NOTE: Should return info and other data from db as a dictionary 
# - book_id = the book_id of the manga that is the same as the one in the database
def get_manga_details(book_id: int):
    cursor = CONNECTION_TO_DB.cursor()

    # query code goes here

    cursor.close()
    return {
        "nothing": "need to create func"
    }
