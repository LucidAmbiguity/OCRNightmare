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


class ProjectSchema(ma.Schema):

    class Meta:
        fields = ('id', 'name', 'filename',
                  'status',
                  )

project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)


class PageSchema(ma.Schema):

    class Meta:
        fields = ('id', 'project_id',)

page_schema = PageSchema()
pages_schema = PageSchema(many=True)


class CustomerSchema(ma.Schema):

    class Meta:
        fields = ('id', 'project_id',)

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

class TextLineSchema(ma.Schema):

    class Meta:
        fields = ('id', 'page_id','text_line')

text_line_schema = TextLineSchema()
text_lines_schema = TextLineSchema(many=True)

