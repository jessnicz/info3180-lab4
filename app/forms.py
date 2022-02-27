from click import File
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    file_field = FileField('image upload', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg'], 'File type not supported. Please use one of the following required file types: jpg, png, jpeg')])