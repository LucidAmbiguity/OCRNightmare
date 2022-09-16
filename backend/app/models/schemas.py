
from app.extensions import ma


class UserSchema(ma.Schema):
    """ User Schema for serialization """

    class Meta:
        fields = ('id', 'public_id', 'name',
                  'admin',)

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("admin.users.users_test", values=dict(id="<id>")),
            "collection": ma.URLFor("admin.users.users_root"),
        }
    )

user_schema = UserSchema()
users_schema = UserSchema(many=True)
