from connection import CONNECTION_TO_DB
# from searchSQL.pageThree import getMangaDetails

# ! == About ==
# Handle getting more information about specifc manga in db

# NOTE: Should return info and other data from db as a dictionary 
# - book_id = the book_id of the manga that is the same as the one in the database
def get_manga_details(book_id: int):
    cursor = CONNECTION_TO_DB.cursor()

    page_three_query = '''
            SELECT DISTINCT m.title, a.Name, m.publishedstart, m.publishedend,
            GROUP_CONCAT(DISTINCT t.type SEPARATOR ', ') AS themes,
            GROUP_CONCAT(DISTINCT g.type SEPARATOR ', ') AS genres,
            m.synopsis
            FROM Manga m
            INNER JOIN Author a ON a.bookid = m.bookid
            INNER JOIN Theme t ON t.bookid = a.bookid
            INNER JOIN Genre g ON g.bookid = t.bookid
            WHERE m.bookid = %s
            GROUP BY m.title, a.Name, m.publishedstart, m.publishedend, m.synopsis
        '''

    cursor.execute(page_three_query, (book_id,))
    result = cursor.fetchone()
    
    # query code goes here
    if result:
        # Construct a dictionary with column names as keys
        manga_details = {
            "title": result[0],
            "author": result[1],
            "published_start": result[2],
            "published_end": result[3],
            "themes": result[4],
            "genres": result[5],
            "synopsis": result[6]
        }
    else:
        manga_details = None

        

    cursor.close()
    return {
        #"nothing": "need to create func"
        manga_details
    }
