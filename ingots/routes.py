from ingots import app,storage_mgr
from flask import render_template,request
from werkzeug.utils import secure_filename

@app.route('/',methods=['GET', 'POST'])
def home():
    message = None
    files = storage_mgr.list()

    if request.method == 'POST':
        if 'file' not in request.files:
            message = "No file part in upload."
            
        else:
            file = request.files['file']
            if file.filename == '':
                message = "No file selected."

            if file and file.filename:
                safe_filename = secure_filename(file.filename)
                if storage_mgr.store(safe_filename,file):
                    message = f"File {safe_filename} uploaded."
                    files = storage_mgr.list()
                else:
                    message = f"File {safe_filename} could not be uploaded. Please try again after some time."

    return render_template('index.html', message = message, files = files)
    

@app.route('/uploads/<name>', methods=['GET'])
def download(name):
    return storage_mgr.retrieve(name)

