""" DB Interface Thingy """

from typing import Optional, cast

from app.types import NewUserTup
from app.extensions import db
from app.models import  User


class DBUserI:
    """ User Interface """

    def get_all_users(self)->list[User]:
        result: list[User] = User.query.all()  # type: ignore[misc]
        return result

    def get_user_by_username(self, username:Optional[str])->Optional[User]:
        return cast( User, User.query.filter_by(name=username).first()) # type: ignore[misc]

    def get_user_by_id(self, uid:Optional[int])->Optional[User]:
        return cast( User, User.query.filter_by(id=uid).first()) # type: ignore[misc]

    def get_user_by_public_id(self, public_id:Optional[str])->Optional[User]:
        return cast( User, User.query.filter_by(public_id=public_id).first()) # type: ignore[misc]


    def new_user(self,new_user:NewUserTup)->User:
        new_user_db = User(
                public_id = new_user.public_id,
                name = new_user.name,
                password = new_user.password,
                admin = new_user.admin,
        )
        db.session.add(new_user_db) # type: ignore[misc] # pylint: disable=no-member
        db.session.commit() # type: ignore[misc] # pylint: disable=no-member
        db.session.refresh(new_user_db) # type: ignore[misc]
        return new_user_db

    def del_user(self, user_db:Optional[User])->bool:
        if user_db:
            db.session.add(user_db)
            db.session.delete(user_db)
            db.session.commit()
            return True
        return False