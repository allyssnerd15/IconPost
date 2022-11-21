from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class
from flask_bcrypt import Bcrypt

import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minhaloja.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'adminadmin123'

db = SQLAlchemy(app)
app.app_context().push()
bcrypt = Bcrypt(app)

#app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')

#photos = UploadSet('photos', IMAGES)
#configure_uploads(app, photos)
#patch_request_class(app)

from loja.admin import rotas
from loja.produtos import rotas
from loja.carrinho import carrinhos

#if __name__== '__main__':
#    rotas()