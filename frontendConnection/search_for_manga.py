from frontendConnection.connection import CONNECTION_TO_DB


# ! == About ==
# Handle search db for manga that meets search parms

# NOTE: Should return info and other data from db as a dictionary 
# - search_type = author | title | theme | genre
# - last_book_id = the last book_id given to the user, using this to setup paging to give complete db to user
# - query = the search query from user
def search_for_manga(search_type: str, last_book_id: int, query: str):
    cursor = CONNECTION_TO_DB.cursor()

    # query code goes here


    cursor.close()
    return {
        "nothing": "need to create func"
    }