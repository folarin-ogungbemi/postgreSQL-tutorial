from sqlalchemy import (
    create_engine, String, Integer, Column
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "programmer" table
class Profile(base):
    __tablename__ = "Profile"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    occupation = Column(String)
    company = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our Programmer table
folarin_ogungbemi = Profile(
    first_name="Folarin",
    last_name="Ogungbemi",
    gender="M",
    nationality="Nigerian",
    occupation="Software Engineer Student",
    company="Code Institute"
)

# add each instance of our programmers to our session
session.add(folarin_ogungbemi)

# commit our session to the database
session.commit()

# query the database to find all Programmers
profiles = session.query(Profile)
for profile in profiles:
    print(
        profile.id,
        profile.first_name + " " + profile.last_name,
        profile.gender,
        profile.nationality,
        profile.occupation,
        profile.company,
        sep=" | "
    )
