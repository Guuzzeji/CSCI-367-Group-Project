import select
import mysql.connector
from mysql.connector import errorcode

try:
  reservationConnection = mysql.connector.connect(   host="localhost",user="pwd12345",password="exampleUser",
        database="manga_db",
        port="4040"
    )

except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print('Invalid credentials')
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print('Database not found')
   else:
      print('Cannot connect to database:', err)

else:
   	##gets user search

    print('Input Search ', end = '')
    search = input()

   
    #search_type = getSpecifiedSearch()
    search_type = "Theme"

    ##If statement for when adv search is by title
    if search_type == "title":
        table_name = "Manga"

        searchQuery = """
        SELECT m.imgurl, m.title
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

        searchCursor = reservationConnection.cursor()
        searchCursor.execute(searchQuery, (search, f'{search}%', f'%{search}%', search, f'{search}%', f'%{search}%'))

    ##If statement for when adv search is by author
    elif search_type == "Author":
        table_name = "Authors"
        searchQuery = """
        SELECT m.imgurl, m.title, a.name
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

        searchCursor = reservationConnection.cursor()
        searchCursor.execute(searchQuery, (search, f'{search}%', f'%{search}%', search, f'{search}%', f'%{search}%'))

    ##If statement for when adv search is by genre  
    elif search_type == "Genre":
        table_name = "Genre"
        searchQuery = """
        SELECT m.imgurl, m.title, g.type
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
        searchCursor = reservationConnection.cursor()
        searchCursor.execute(searchQuery, (search, f'{search}%', f'%{search}%', search, f'{search}%', f'%{search}%'))

    ##If statement for when adv search is by theme
    elif search_type == "Theme":
        table_name = "Theme"
        searchQuery = """
        SELECT m.imgurl, m.title, t.type
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
        searchCursor = reservationConnection.cursor()
        searchCursor.execute(searchQuery, (search, f'{search}%', f'%{search}%', search, f'{search}%', f'%{search}%'))



    ##PAGE 2 SELECT CODE

    # Fetch the results

    result= searchCursor.fetchall()


    ##if statement to see if anything was selected
    if not result:
        print("search not found")
    else:
        for x in result:
            print(x)

    reservationConnection.commit()
    searchCursor.close()
    reservationConnection.close()
