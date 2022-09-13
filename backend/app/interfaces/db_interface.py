""" Data Base Main Interface """

from app.extensions import db
from sqlalchemy.orm.session import close_all_sessions



class DBInterface:

    def create_all(self)->None:
        db.create_all()

    def close_and_drop(self)->None:
        # db.close_all_sessions()
        close_all_sessions()
        db.drop_all()

