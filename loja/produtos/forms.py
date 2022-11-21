from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators
from wtforms import Form

class AddProduto(Form):
    name = StringField('Nome :', [validators.DataRequired()])
    price = BooleanField('Preço :', [validators.DataRequired()])
    minimun = BooleanField('minino :', [validators.DataRequired()])
    amount_per_package = BooleanField('Quantidade :', [validators.DataRequired()])
    max_availability = BooleanField('Maxino :', [validators.DataRequired()])
    
    image_1 = FileField('image 1 :' , validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_2 = FileField('image 2 :' , validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_3 = FileField('image 3 :' , validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    