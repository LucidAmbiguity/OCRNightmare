"""Authentication Module"""

from pickle import GET
from flask import request
from app.auth import auth  # pylint: disable=import-self


@auth.route("/", methods=['GET', 'POST'])
@auth.route("", methods=['GET', 'POST'])
def auth_root():
    """Root route of App Module"""
    return {
            "code": 200,
            "messages": [
                {
                "code": "A00001", 
                "text": "Success."
                }
            ],
            "result": {
                "links": {
                "login": "login", 
                "register": "register"
                }
            },
            "status": "OK"
            }, 200, {'WWW.Authentication': 'Basic realm: "login required"'}


@auth.route('/register', methods=['POST'])  
def register_user():
    """Create a User"""
    request_auth = request.authorization   
    print("auth", request_auth)
    return {
            "code": 200,
            "messages":  [
                {
                "code": "A00002",
                "text": "Username and Password Required."
                },
                {
                "code": "A00003",
                "text": "Basic realm: 'login required'"
                }
            ],
            "result": {
                "links": {
                "login": "login", 
                "register": "register"
                }
            },
            "status": "OK"
            }
   