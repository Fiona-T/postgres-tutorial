# import classes from sqlalchemy module
from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String,
)

# will create classes which subclass from declarative_base
from sqlalchemy.ext.declarative import declarative_base
# sessionmaker for connection to the db
from sqlalchemy.orm import sessionmaker

# link to the local chinook db on the postgress server
# engine created and connected to the local database
db = create_engine("postgresql:///chinook")
# get metadata produced by db table schema from the declarative_base class
base = declarative_base()


# create a class-based model for the table Artist, using base subclass
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create a class-based model for the table Album, using base subclass
# foreignkey points to original Class and Column name
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create a class-based model for the table Track, using base subclass
# foreignkey points to original Class and Column name as before
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)

# open an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# query 1 - select all records from the Artist table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# query 2 - select only the Name column from the Artist table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# query 3 - select only Queen from the Artist table
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# query 4 - select only ArtistId 51 from the Artist table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# query 5 - select only the albums with ArtistId 51 from the Album table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# query 6 - select all tracks where the composer is Queen from the Track table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
        )
