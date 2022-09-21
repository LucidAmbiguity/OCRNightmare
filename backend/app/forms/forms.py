""" WTF Form Models"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField



class UploadFile(FlaskForm):
    class Meta:
        csrf = False  # Disable CSRF

    upfile = FileField(
        validators=[FileRequired(), FileAllowed(['pdf', ], 'PDFs only!')])
    submit = SubmitField('UPLOAD')
