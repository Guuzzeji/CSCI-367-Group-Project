import mysql.connector
from mysql.connector import errorcode

try:
   reservationConnection = mysql.connector.connect(
      user='FIGURE THIS OUT',
      password='FIGURE THIS OUT',
      host='FIGURE THIS OUT',
      database='FIGURE THIS OUT')

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

##gets a the category of search
searchType = getSpecifiedSearch()

##get what table to look through
if search_type == "Title":
    table_name = "Manga"
elif search_type == "Author":
    table_name = "Authors"
elif search_type == "Genre":
    table_name = "Genre"
elif search_type == "Theme":
    table_name = "Theme"

searchCursor = reservationConnection.cursor()

##PAGE 2 SELECT CODE
searchQuery = """
SELECT imgurl, title
    FROM Manga
    INNER JOIN {} ON {}.bookid = manga.bookid
    WHERE searchType = %s 
    OR searchType LIKE %s 
    OR searchType LIKE %s
    ORDER BY CASE
    	 WHEN searchType = %s then 1
	 WHEN searchType LIKE %s then 2
	 WHEN searchType LIKE %s then 3
	 ELSE 4
`   END
""".format(table_name, table_name)
search_cursor.execute(search_query, (search, f'{search}%', f'%{search}%', search, f'{search}%', f'%{search}%'))

result= select.fetchall()


##if statement to see if anything was selected
if not result:
	print(“search not found”)
else:
for x in result:
 	print(x)

reservationConnection.commit()
searchCursor.close()
   reservationConnection.close()
