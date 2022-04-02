import json
from ingots import app,storage_mgr,db
from flask import jsonify, render_template,request
from flask import Response, send_from_directory, abort
from werkzeug.utils import secure_filename

upload_folder = app.config['UPLOAD_FOLDER']

from ingots.models import Book

@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        books = Book.getBooks()
        return jsonify({"books":books})
    if request.method == 'POST':
        request_body = json.loads(request.form['data'])
        title = request_body['title']
        author = request_body['author']
        category = request_body['category']
        print(request.files['uploaded_file'])


        Book.addBook(title,author,category)
        storage_mgr.store(title,request.files['uploaded_file'])

        return {"status":"success"}


@app.route("/delete/<title>",methods=['GET'])
def delete(title):
    if storage_mgr.delete(title):
        Book.deleteBookByTitle(title)
        return {"status":"success"}
    else:
        abort(404)


@app.route('/uploads/<name>', methods=['GET'])
def download(name):
    try:
        return send_from_directory(upload_folder,name, as_attachment=True)
    except FileNotFoundError:
        print('Could not retrieve',name)
        abort(404)

