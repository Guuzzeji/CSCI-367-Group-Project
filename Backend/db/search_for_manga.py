from db.connection import CONNECTION_TO_DB


# ! == About ==
# Handle search db for manga that meets search parms

# NOTE: Should return info and other data from db as a dictionary 
# - search_type = author | title | theme | genre
# - last_book_id = the last book_id given to the user, using this to setup paging to give complete db to user
# - query = the search query from user
def search_for_manga(search_type: str, query: str):
    cursor = CONNECTION_TO_DB.cursor()

    search_type = search_type.lower()

    # NOTE: Key is used to reorganize result as json file so each element has the correct key pair

    if search_type == "title":
        table_name = "Manga"
        keys = ['bookid','imgurl', 'title']
        searchQuery = """
        SELECT m.bookid, m.imgurl, m.title
        FROM {} m
        WHERE m.title = %s
        OR m.title LIKE %s 
        OR m.title LIKE %s
        ORDER BY CASE
        WHEN m.title = %s then 1
        WHEN m.title LIKE %s then 2
        WHEN m.title LIKE %s then 3
        END
        """.format(table_name)

    elif search_type == "author":
        table_name = "Authors"
        keys = ['bookid','imgurl', 'title', 'author']
        searchQuery = """
        SELECT m.bookid, m.imgurl, m.title, a.name
        FROM Author a
        INNER JOIN Manga m on m.bookid = a.bookid
        WHERE a.name = %s
        OR a.name LIKE %s 
        OR a.name LIKE %s
        ORDER BY CASE
        WHEN a.name = %s then 1
        WHEN a.name LIKE %s then 2
        WHEN a.name LIKE %s then 3
        END,
        m.title;
        """.format(table_name)

    elif search_type == "genre":
        table_name = "Genre"
        keys = ['bookid','imgurl', 'title', 'type']
        searchQuery = """
        SELECT m.bookid, m.imgurl, m.title, g.type
        FROM Genre g
        INNER JOIN Manga m on m.bookid = g.bookid
        WHERE g.type = %s
        OR g.type LIKE %s 
        OR g.type LIKE %s
        ORDER BY CASE
        WHEN g.type = %s then 1
        WHEN g.type LIKE %s then 2
        WHEN g.type LIKE %s then 3
        END,
        m.title;
        """.format(table_name)

    elif search_type == "theme":
        table_name = "Theme"
        keys = ['bookid','imgurl', 'title', 'type']
        searchQuery = """
        SELECT m.bookid, m.imgurl, m.title, t.type
        FROM Theme t
        INNER JOIN Manga m on m.bookid = t.bookid
        WHERE t.type = %s
        OR t.type LIKE %s 
        OR t.type LIKE %s
        ORDER BY CASE
        WHEN t.type = %s then 1
        WHEN t.type LIKE %s then 2
        WHEN t.type LIKE %s then 3
        END,
        m.title;
        """.format(table_name)

    cursor.execute(searchQuery, (query, f'{query}%', f'%{query}%', query, f'{query}%', f'%{query}%'))
    result = cursor.fetchall()
    result_key_list = [{keys[i]: row[i] for i in range(len(keys))} for row in result]

    cursor.close()
    return result_key_list