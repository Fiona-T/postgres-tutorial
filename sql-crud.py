# import classes from sqlalchemy module
from sqlalchemy import (
    create_engine, Column, Integer, String,
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


# create a class-based model for the Programmer table, extending base
# this defines the table schema
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)

# open an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# create records on the Programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

fiona_t = Programmer(
    first_name="Fiona",
    last_name="T",
    gender="F",
    nationality="Irish",
    famous_for="Nothing yet!"
)

# add instance of Programmer to the session. Comment out old one before adding
# more, otherwise it creates a second record for that person
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(fiona_t)

# commit the session (that was added above) to the database
# session.commit()

# updating a single record
# find record in table with id 7, add .first() - one record, no need to iterate
# programmer = session.query(Programmer).filter_by(id=7).first()
# # add what needs to be updated
# programmer.famous_for = "World President"
# # commit the update to the database
# session.commit()

# updating multiple records
# find the records to update - all records in Programmer table
# people = session.query(Programmer)
# # for each record, update gender field
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     # commit the update
#     session.commit()

# delete a single record
# first identify the record - get first and last name from user
fname = input("Enter the first name: ")
lname = input("Enter the last name: ")
# find first record in table that matches the first and last name input
programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# check if any record found, get user to confirm before deleting
if programmer is not None:
    print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
    confirmation = input("Are you sure you want to delete this record (y/n) ")
    if confirmation.lower() == "y":
        session.delete(programmer)
        session.commit()
        print("Programmer has been deleted")
    else:
        print("Programmer not deleted")
else:
    print("No records found")

# to delete all records - keep commented out
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()
# would need to add in defensive to confirm deletion first

# query the database to find Programmers
programmers = session.query(Programmer)

for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
