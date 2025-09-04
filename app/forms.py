from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Register')

class blogForm(FlaskForm):
    title = StringField('Title')
    content = TextAreaField('Content')
    tag = StringField('Tag')
    submit = SubmitField('Submit')
