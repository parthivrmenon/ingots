# ROUTES
import os
from ingots import app,store,store_s3

from flask import render_template,request
from werkzeug.utils import secure_filename


@app.route('/',methods=['GET', 'POST'])
def home():
    message = None
    # files = store.list()
    files = store_s3.list()

    if request.method == 'POST':
        if 'file' not in request.files:
            message = "No file part in upload."
            
        else:
            file = request.files['file']
            if file.filename == '':
                message = "No file selected."

            if file and file.filename:
                safe_filename = secure_filename(file.filename)
                # store.store(safe_filename, file)
                store_s3.store(safe_filename,file)
                message = f"File {safe_filename} uploaded."
                files = store_s3.list()



    return render_template('index.html', message = message, files = files)
    

@app.route('/uploads/<name>', methods=['GET'])
def download(name):
    return store_s3.retrieve(name)

