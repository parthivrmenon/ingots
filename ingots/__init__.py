# CONFIGURATION
import os
from flask import Flask
from .storage import LocalStorage,S3Storage

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER=os.path.join(BASE_DIR, 'files')
    
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = '1@3$5^7'

store = LocalStorage(app.config['UPLOAD_FOLDER'])
store_s3 = S3Storage(app.config['UPLOAD_FOLDER'])



from ingots import routes

