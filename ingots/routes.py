# ROUTES
import os
from ingots import app
from flask import render_template,request,send_from_directory,abort


@app.route('/',methods=['GET', 'POST'])
def home():
    message = None
    files = os.listdir(app.config['UPLOAD_FOLDER'])

    if request.method == 'POST':
        if 'file' not in request.files:
            message = "No file part in upload."

        file = request.files['file']
        if file.filename == '':
            message = "No file selected."

        if file and file.filename:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            message = f"File {filename} uploaded."

    return render_template('index.html', message = message, files = files)
    

@app.route('/uploads/<name>', methods=['GET'])
def download(name):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], name, as_attachment=True)
    except FileNotFoundError:
        abort(404)
