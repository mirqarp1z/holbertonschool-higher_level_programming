#!/usr/bin/python3
"""
Module for deleting all the cities with 'a'.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(state)
    session.commit()

    if session:
        session.close()
