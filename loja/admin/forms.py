from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    __tablename__ = "admin"
    
    username = StringField('Username :', [validators.Length(min=4, max=25)])
    email = StringField('Email Address :', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirmação da senha', message='usuario e senha não são iguais')
    ])
    confirm = PasswordField('Repeat Password')
    

class LoginForm(Form):
    email = StringField('Email Address :', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [validators.DataRequired()])
    