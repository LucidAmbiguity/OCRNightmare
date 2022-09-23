""" Login Service """

from typing import TYPE_CHECKING, Optional, Union
import jwt
from datetime import datetime, timedelta
from werkzeug.security import  check_password_hash

from app.repositories import UserRepo
from app.types.my_types import AToken

if TYPE_CHECKING:
    from flask import Flask

def login_service(userpass:tuple[str,str],current_app:'Flask')->Union[tuple[str,Optional[str]],tuple[None,None]]:
    """ The login service """

    user = userpass[0]
    offered_password = userpass[1]
    (current_password, pub_id) = UserRepo(username=user).get_user_password_and_pubid()
    # #print('login_service: ',userpass,current_password,pub_id)
    if current_password is None:
        return None,None

    if not check_password_hash(current_password, offered_password):
        return None,None

    token: AToken = jwt.encode({ # type: ignore[misc]
        'public_id': pub_id,
        'exp' : datetime.utcnow() + timedelta(minutes=30)
        },
        current_app.config['SECRET_KEY'],algorithm='HS256' # type: ignore[misc]
    )
    return (token,pub_id)


