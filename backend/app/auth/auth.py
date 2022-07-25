"""Authentication Module"""

from app.auth import auth  # pylint: disable=import-self


@auth.route("/", methods=['GET', 'POST'])
@auth.route("", methods=['GET', 'POST'])
def auth_root():
    """Root route of App Module"""
    return {'auth':'auth root'}
