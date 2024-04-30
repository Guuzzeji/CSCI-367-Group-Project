from connection import CONNECTION_TO_DB
import datetime
# from searchSQL.pageThree import getMangaDetails

# ! == About ==
# Handle getting more information about specifc manga in db

# NOTE: Should return info and other data from db as a dictionary 
# - book_id = the book_id of the manga that is the same as the one in the database
def get_manga_details(book_id: int):
    cursor = CONNECTION_TO_DB.cursor()

    page_three_query = '''
            SELECT DISTINCT m.title, a.Name, DATE_FORMAT(m.publishedstart, '%m/%d/%Y') AS published_start,
            DATE_FORMAT(m.publishedend, '%m/%d/%Y') AS published_end, m.imgurl,
            GROUP_CONCAT(DISTINCT t.type SEPARATOR ', ') AS themes,
            GROUP_CONCAT(DISTINCT g.type SEPARATOR ', ') AS genres,
            m.synopsis, r.score, m.chapters, m.status
            FROM Manga m
            INNER JOIN Author a ON a.bookid = m.bookid
            INNER JOIN Theme t ON t.bookid = a.bookid
            INNER JOIN Genre g ON g.bookid = t.bookid
            INNER JOIN Ratings r on r.bookid = m.bookid
            WHERE m.bookid = %s
            GROUP BY m.title, a.Name, m.publishedstart, m.publishedend, m.synopsis, r.score, m.chapters, m.status
        '''

    cursor.execute(page_three_query, (book_id,))
    results = cursor.fetchall()
    
    manga_details_list = []
    # query code goes here
    if results:
        for result in results:
            # Constructs a dictionary with column names as keys
            '''
            published_start = result[2]
            if published_start is not None:
                published_start = result[2]
            else:
                published_start = None
            published_end = result[3]
            if published_end is not None:
                published_end = result[3]
            else:
                published_end = None'''
            manga_details = {
                "title": result[0],
                "author": result[1],
                "published_start": result[2], #published_start,
                "published_end": result[3], #published_end,
                "image": result[4],
                "themes": result[5],
                "genres": result[6],
                "synopsis": result[7],
                "score": result[8],
                "chapters": result[9],
                "status": result[10]
            }
            manga_details_list.append(manga_details)
    else:
        manga_details_list = None

        

    cursor.close()
    return manga_details_list
    
