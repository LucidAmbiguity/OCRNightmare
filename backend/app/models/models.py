"""
Models for the project
"""
# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring


from typing import Any, cast
import uuid
from werkzeug.security import generate_password_hash


from app.extensions import db


class User(db.Model): # type: ignore[name-defined]
    """
    User Model of Project
        id:
        public_id: uuid4 used as username behind the scenes
        name:
        password:
        admin: boolean
    """

    # pylint: disable=no-member
    id: int = db.Column(db.Integer, primary_key=True) # type: ignore[misc]
    public_id: str = db.Column(db.String(50), unique=True) # type: ignore[misc]
    name: str = db.Column(db.String(50), unique=True,) # type: ignore[misc]
    password: str = db.Column(db.String(255), nullable=False) # type: ignore[misc]
    admin: bool = db.Column(db.Boolean, nullable=False) # type: ignore[misc]
    # pylint: enable=no-member

    def __init__(self, **kwargs: Any) ->None:
        super().__init__(**kwargs) # type: ignore[misc]
        # print(kwargs)
        self.public_id = kwargs.get('public_id', str(uuid.uuid4()))
        self.admin = cast(bool, kwargs.get('admin', False)) # type: ignore[misc]
        if cast(bool, kwargs.get('password', False)): # type: ignore[misc]
            self.password = generate_password_hash(
                kwargs['password'], method='sha256') # type: ignore[misc]
        # do custom initialization here


