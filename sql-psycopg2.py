import psycopg2


# connect to the chinook database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database. cursor object is a set or list,
# queried data goes here
cursor = connection.cursor()

# query 1 - select all records from the Artist table
# cursor.execute('SELECT * FROM "Artist"')

# query 2 - select only the Name column from the Artist table
# cursor.execute('SELECT "Name" FROM "Artist"')

# query 3 - select only Queen from the Artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# query 4 - select only ArtistId 51 from the Artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# query 5 - select only the albums with ArtistId 51 from the Album table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# query 6 - select all tracks where the composer is Queen from the Track table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# query 7 - select all tracks from Track table where the composer is Pearl Jam
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Pearl Jam"])

# fetch the results from the cursor - multiple results
results = cursor.fetchall()

# fetch the results from the cursor - single record
# results = cursor.fetchone()

# close the connection to the after the results are retrieved
connection.close()

# print each individual result from results
for result in results:
    print(result)
