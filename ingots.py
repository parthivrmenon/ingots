import json
from flask import Flask,jsonify, request , abort

from ingots.interfaces.in_memory_book_repository import InMemoryBookRepository
from ingots.interfaces.local_storage import LocalStorage
from ingots.use_cases.get_books import GetBooks
from ingots.use_cases.get_book import GetBook
from ingots.use_cases.save_book import SaveBook
from ingots.use_cases.delete_book import DeleteBook

from ingots.dto.book_dto import BookDto

app = Flask(__name__)
repository = InMemoryBookRepository()
storage = LocalStorage("./")


@app.route("/api/v1/ping", methods=['GET'])
def ping():
    return "pong"
    
@app.route("/api/v1/get-books", methods=['GET'])
def get_books():
    use_case = GetBooks(repository)
    books = use_case.execute()
    return jsonify({"books":books})

@app.route("/api/v1/delete-book/<int:id>", methods=['GET'])
def delete_book(id):
    print("Trying to delete book by id",id)
    use_case_delete_book = DeleteBook(repository)
    is_deleted = use_case_delete_book.execute(id)
    

        
    
    return jsonify({"status":is_deleted})

@app.route("/api/v1/upload-book",methods=['POST'])
def upload_book():
    """
    Uploading a book requires two steps:
    1. Save the uploaded file via 'Storage.save_file method
    2. Store metadata via 'BookRepository.'
    """
    form_data = request.form
    uploaded_file = request.files['uploaded_file']
    try:
        new_book = BookDto(form_data)
        use_case = SaveBook(new_book, repository, storage, uploaded_file)
        is_uploaded = use_case.execute()
        return jsonify({"status": is_uploaded})
    except Exception as err:
        print(err)
        abort(400)


if __name__ == "__main__":
    app.run()