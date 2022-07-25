"""Authentication Module"""

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
