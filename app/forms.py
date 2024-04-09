from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, DataRequired, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max = 1000)])
    poster = FileField('Poster', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg','png'], 'Images only!')])
