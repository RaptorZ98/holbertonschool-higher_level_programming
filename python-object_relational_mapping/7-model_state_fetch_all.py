#!/usr/bin/python3
""" select states """


import MySQLdb
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select


if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb\
://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        query = select(State).order_by(State.id)
        result = session.execute(query).all()
    for row in result:
        print(f"{row[0].id} : {row[0].name}")
