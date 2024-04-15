import csv
import mysql.connector
import datetime 

def readCsv(filename):
    manga_data = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            bookid = row[0]
            dataType = row[1]
            manga_data.append({
                'bookid': bookid,
                'dataType': dataType
            })
    return manga_data


def readMangaCsv(filename):
    manga_data = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        # next(reader)
        for row in reader:
            # getting data from each line
            bookid = row[0]
            myanimelisturl = row[1]
            title = row[2]
            imgurl = row[3]
            chapters = row[4]
            volumes = row[5]
            status = row[6]
            publishedstart = row[7]
            publishedend = row[8]
            synopsis = row[9]
            background = row[10]

            # appending the data as a dictionary to the manga_data list
            manga_data.append({
                'bookid': bookid,
                'myanimelisturl': myanimelisturl,
                'title': title,
                'imgurl': imgurl,
                'chapters': chapters,
                'volumes': volumes,
                'status': status,
                'publishedstart': publishedstart,
                'publishedend': publishedend,
                'synopsis': synopsis,
                'background': background
            })

    return manga_data

def readAuthorCsv(filename):
    authorData = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            bookid = row[0]
            authorname = row[1]
            authorurl = row[2]

            authorData.append({
                'bookid': bookid,
                'authorname': authorname,
                'authorurl': authorurl
            })

    return authorData

def insertDataManga(table_name, data):
    try:
        # insert query for manga table
        query = "INSERT INTO Manga (bookid, myanimelisturl, title, imgurl, chapters, volumes, status, publishedstart, publishedend, synopsis, background) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        # Executes query for each manga entry in the data
        for manga in data:
            # synopsis = manga['synopsis']
            # print(f"Length of synopsis: {len(synopsis)}")
            try:
                chapters = int(manga['chapters'])
            except ValueError:
                # handles case where the string cannot be converted to an int
                chapters = None
            try:
                volumes = int(manga['volumes'])
            except ValueError:
                volumes = None

            publishedstart = manga['publishedstart']
            if publishedstart:
                try:
                    publishedstart = datetime.datetime.strptime(publishedstart, '%Y-%m-%dT%H:%M:%S%z')
                except ValueError:
                # handels case where the string cannot be converted to datetime
                    publishedstart = None  
            else:
                publishedstart = None
            publishedend = manga['publishedend']
            if publishedend:
                try:
                    publishedend = datetime.datetime.strptime(publishedend, '%Y-%m-%dT%H:%M:%S%z')
                except ValueError:
                    publishedend = None  
            else:
                publishedend = None
            manga_values = (
                int(manga['bookid']),
                manga['myanimelisturl'],
                manga['title'],
                manga['imgurl'],
                chapters,
                volumes,
                manga['status'],
                #int(manga['chapters']),
                #int(manga['volumes']),
                # manga['publishedstart'],
                publishedstart,
                #manga['publishedend'],
                publishedend,
                manga['synopsis'],
                manga['background']
            )
            cursor.execute(query, manga_values)

        connection.commit()
        print(f"{len(data)} manga records inserted successfully.")

    except mysql.connector.Error as error:
        print(f"Failed to insert manga records: {error}")


def insertDataAuthor(table_name, data):
    try:
        query = "INSERT INTO Author (bookid, Name, authorurl) VALUES (%s, %s, %s)"

        for author in data:
            authorValues = (
                int(author['bookid']),
                author['authorname'],
                author['authorurl']
            )
            cursor.execute(query, authorValues)

        connection.commit()
        print(f"{len(data)} author records inserted successfully.")

    except mysql.connector.Error as error:
        print(f"Failed to insert author records: {error}")

def insertDataMisc(table_name, data, column_names):
    try:
        query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES (%s, %s)"
        
        for entry in data:
            if entry['dataType'] == '':
                entry['dataType'] = None
            entry_values = (
                int(entry['bookid']),
                entry['dataType']
            )
            cursor.execute(query, entry_values)

        connection.commit()
        print(f"{len(data)} records inserted successfully into {table_name} table.")

    except mysql.connector.Error as error:
        print(f"Failed to insert records into {table_name} table: {error}")


# Change this to your guys' shit
connection = mysql.connector.connect(
    host="localhost",
    port=4040,
    user="pwd12345",
    password="exampleUser",
    database="manga_db"
)

cursor = connection.cursor()

# reading data from csv files
manga_data = readMangaCsv("Manga.csv")
authorData = readAuthorCsv("Author.csv")
genre_data = readCsv("Genre.csv")
theme_data = readCsv("Theme.csv")
demographic_data = readCsv("Demographic.csv")
review_data = readCsv("Rating.csv")


# inserting data into the mysql tables
insertDataManga("Manga", manga_data)
insertDataAuthor("Author", authorData)
insertDataMisc("Genre", genre_data,['bookid', 'type'])
insertDataMisc("Theme", theme_data,['bookid','type'])
insertDataMisc("Demographic", demographic_data,['bookid', 'Name'])
insertDataMisc("Ratings", review_data, ['bookid', 'score'])


cursor.close()
connection.close()