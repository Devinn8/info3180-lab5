# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    poster = FileField('Poster', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])
    