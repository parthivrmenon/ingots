from unicodedata import category
from ingots import db 

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    author = db.Column(db.String(200))
    category = db.Column(db.String(200))

    def toDict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author":self.author,
            "category":self.category
        }

    @staticmethod
    def getBooks(count=100):	
        books = Book.query.order_by(Book.id).limit(count).all()	
        return [book.toDict() for book in books]

    @staticmethod
    def getBookById(id):
        book = Book.query.filter_by(id=id).first()
        return book.toDict()

    @staticmethod
    def addBook(title,author,category):
        new_book = Book()
        new_book.title = title 
        new_book.author = author
        new_book.category = category
        db.session.add(new_book)
        db.session.commit()

    @staticmethod
    def deleteBookByTitle(title):
        book = Book.query.filter_by(title=title).first()
        db.session.delete(book)
        db.session.commit()


    
