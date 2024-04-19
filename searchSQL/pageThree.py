import select
import mysql.connector
from mysql.connector import errorcode


try:
    reservationConnection = mysql.connector.connect(   host="localhost",user="root",password="rootpassword",
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
    ##bookid of manga from hyplerlink. Will be defined by html
    selectedBookid = input()
    #selectedBookid = bookid
    ##gets advance information of specified manga for page three
    pageThreeQuery =( '''
                    SELECT DISTINCT m.title, a.Name, m.publishedstart, m.publishedend,
                    GROUP_CONCAT(DISTINCT t.type SEPARATOR ', ') AS themes,
                    GROUP_CONCAT(DISTINCT g.type SEPARATOR ', ') AS genres,
                    m.synopsis
                    FROM Manga m
                    INNER JOIN Author a ON a.bookid = m.bookid
                    INNER JOIN Theme t ON t.bookid = a.bookid
                    INNER JOIN Genre g ON g.bookid = t.bookid
                    WHERE m.bookid = %s
                    GROUP BY m.title, a.Name, m.publishedstart, m.publishedend, m.synopsis''')


    searchCursor = reservationConnection.cursor()
    searchCursor.execute(pageThreeQuery, (selectedBookid,))

    result= searchCursor.fetchall()

##prints results
    for x in result:
        for item in x:
            print(item)
        print()


    reservationConnection.commit()
    searchCursor.close()
    reservationConnection.close()
