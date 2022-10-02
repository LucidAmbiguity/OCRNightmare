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
    id: int = db.Column(db.Integer, primary_key=True,nullable=False) # type: ignore[misc]
    public_id: str = db.Column(db.String(50), unique=True,nullable=False) # type: ignore[misc]
    name: str = db.Column(db.String(50), unique=True,nullable=False) # type: ignore[misc]
    password: str = db.Column(db.String(255), nullable=False) # type: ignore[misc]
    admin: bool = db.Column(db.Boolean, nullable=False) # type: ignore[misc]
    # pylint: enable=no-member

    def __init__(self, **kwargs: Any) ->None:
        super().__init__(**kwargs) # type: ignore[misc]
        # print(kwargs)
        self.public_id = kwargs.get('public_id', str(uuid.uuid4())) # type: ignore[misc]
        self.admin = cast(bool, kwargs.get('admin', False)) # type: ignore[misc]
        if cast(bool, kwargs.get('password', False)): # type: ignore[misc]
            self.password = generate_password_hash(
                kwargs['password'], method='sha256') # type: ignore[misc]
        # do custom initialization here

class Project(db.Model): # type: ignore[name-defined]
    """
    Project Model
        id: int
        name: str
        filename: str
        status: int
        pages: list[Page] - Relation
        customers: list[Customer] - Relation
        tags: list[Tag] - Relation
    """

    # pylint: disable=no-member
    id: int = db.Column(db.Integer, primary_key=True) # type: ignore[misc]
    name: str = db.Column(db.String(25), index=True, unique=True) # type: ignore[misc]
    filename: str = db.Column(db.String(25), index=True, unique=True) # type: ignore[misc]
    status: int = db.Column(db.Integer,  nullable=False) # type: ignore[misc]
    pages: 'Page' = db.relationship('Page', backref='project', lazy='dynamic')
    customers: 'Customer' = db.relationship('Customer', backref='project', lazy='dynamic')  # pylint: disable=line-too-long

    #pylint: enable=no-member

    #  # This will likely be attached to a strategy as the next sample data has 3 sections
    #  #  of account/customer data to extract.
    # tags: 'Tag' = db.relationship('Tag', backref='project', lazy='dynamic')


class Page(db.Model):
    id: int = db.Column(db.Integer, primary_key=True) # type: ignore[misc]
    project_id: int = db.Column(db.Integer, db.ForeignKey('project.id')) # type: ignore[misc]
    page_num: int = db.Column(db.Integer,  nullable=False) # type: ignore[misc]
    width: float = db.Column(db.Float,  nullable=False) # type: ignore[misc]
    height: float = db.Column(db.Float,  nullable=False) # type: ignore[misc]
    text_lines: 'TextLine' = db.relationship('TextLine', backref='page', lazy='dynamic')

    def __repr__(self) -> str:
        return f'<PAGE  id: {self.id}  project_id: {self.project_id}  page_num: {self.page_num}  width: {self.width}  height: {self.height}  text_lines: {cast(int,self.text_lines.count())}  >'  # pylint: disable=line-too-long

class Customer(db.Model):
    id: int = db.Column(db.Integer, primary_key=True) # type: ignore[misc]
    project_id: int = db.Column(db.Integer, db.ForeignKey('project.id')) # type: ignore[misc]


class TextLine(db.Model): # type: ignore[name-defined]
    """
    TextLine Model of Project
        id:
        page_id
        text_line
        chars:
    """
    # pylint: disable=no-member
    id: int = db.Column(db.Integer, primary_key=True)  # type: ignore[misc]
    page_id: int = db.Column(db.Integer, db.ForeignKey('page.id')) # type: ignore[misc]
    text_line: str = db.Column(db.String(10000),  nullable=False) # type: ignore[misc]
    chars: 'Character' = db.relationship('Character', backref='text_line', lazy='dynamic')  # pylint: disable=line-too-long
    # pylint: enable=no-member


class Character(db.Model): # type: ignore[name-defined]
    """
    Character Model of Project
        id:
        text_line_id:
        char:
        width:
        x0: upper left x coordinate of letter on page
        y0: upper left y coordinate of letter on page
        x1: lower right x coordinate of letter on page
        y1: lower right x coordinate of letter on page
    """

    # pylint: disable=no-member
    id: int = db.Column(db.Integer, primary_key=True) # type: ignore[misc]
    text_line_id: int = db.Column(db.Integer, db.ForeignKey('text_line.id')) # type: ignore[misc]
    char: str = db.Column(db.String(1),  nullable=False) # type: ignore[misc]
    width: float = db.Column(db.Float(),  nullable=False) # type: ignore[misc]
    x0: float = db.Column(db.Float(),  nullable=False) # type: ignore[misc]
    y0: float = db.Column(db.Float(),  nullable=False) # type: ignore[misc]
    x1: float = db.Column(db.Float(),  nullable=False) # type: ignore[misc]
    y1: float = db.Column(db.Float(),  nullable=False) # type: ignore[misc]
    # pylint: enable=no-member


