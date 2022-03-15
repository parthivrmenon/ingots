# CONFIGURATION
import os
from flask import Flask

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER=os.path.join(BASE_DIR, 'files')
    
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = '1@3$5^7'

from ingots import routes

