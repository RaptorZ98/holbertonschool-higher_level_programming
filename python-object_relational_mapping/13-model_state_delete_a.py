#!/usr/bin/python3
""" select states """


import MySQLdb
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@local\
host:3306/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        query = select(State).where(State.name.like('%a%'))
        result = session.execute(query).all()
    for row in result:
        session.delete(row[0])
    session.commit()
