
from app.extensions import ma


class UserSchema(ma.Schema):
    """ User Schema for serialization """

    class Meta:
        fields = ('id', 'public_id', 'name',
                  'admin',)

user_schema = UserSchema()
users_schema = UserSchema(many=True)