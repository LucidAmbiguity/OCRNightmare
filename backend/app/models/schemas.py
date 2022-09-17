""" Schemas for Models """
from app.extensions import ma


class UserSchema(ma.Schema):
    """ User Schema for serialization """

    class Meta:
        fields = ('id', 'public_id', 'name',
                  'admin',)

    # # Experimental

    _links = ma.Hyperlinks(     # type: ignore[misc]
        {                       # type: ignore[misc]
            'self': ma.URLFor('admin.users.users_test', values=dict(id='<id>')), # type: ignore[misc]
            'collection': ma.URLFor('admin.users.users_root'), # type: ignore[misc]
        }
    )

user_schema = UserSchema()
users_schema = UserSchema(many=True)
