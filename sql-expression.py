# import classes from sqlalchemy module
from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# link Python file to chinook db using create_engine component
# Tell it to point to local chinook db on the postgress server
# engine created and connected to the local database
db = create_engine("postgresql:///chinook")

# data about the table objects and the data in them using MetaData class
meta = MetaData(db)

# create variable for Artist table - table class/data model
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# variable for Album table in db
# foreignkey needs to be linked to the original table and column in that table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# variable for Track table in db
# foreign keys MediaType and GenreId are linked to tables we are not using, so
# just setting primary_key=False instead
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# connect to db, save connection into variable called connection
with db.connect() as connection:

    # use the select method on the table

    # query 1 - select all records from the Artist table
    # select_query = artist_table.select()

    # query 2 - select only the Name column from the Artist table
    # with_only_columns: specify table, then .c. for column name,
    # all inside list[]
    # select_query = artist_table.select().with_only_columns(
    #   [artist_table.c.Name])

    # query 3 - select only Queen from the Artist table
    # select_query = artist_table.select().where(
    #   artist_table.c.Name == "Queen")

    # query 4 - select only ArtistId 51 from the Artist table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # query 5 - select only the albums with ArtistId 51 from the Album table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # query 6 - select all tracks where composer is Queen from the Track table
    select_query = track_table.select().where(
        track_table.c.Composer == "Queen")

    # use the execute method on the db connection to run the query
    results = connection.execute(select_query)

    # print each result in the results variable
    for result in results:
        print(result)
