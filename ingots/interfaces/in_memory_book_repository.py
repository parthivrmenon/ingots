

from cgi import FieldStorage
from typing import List, Union
from ingots.interfaces.book_repository import BookRepository
from ingots.entities.book import Book
from ingots.interfaces.local_storage import LocalStorage
from ingots.interfaces.storage import Storage


class InMemoryBookRepository(BookRepository):


    def __init__(self):
        self.books : List[Book] = []
        
        

    def get_all(self) -> List[Book]:
        return self.books

    def get_by_id(self, id: int) -> Union[Book, None]:
        for book in self.books:
            if book.id == id:
                return book 
        else:
            return None 

    def save(self, book: Book) -> bool:
        if book.id == None:
            book.id = len(self.books)
        self.books.append(book)
        
        
        return True

    def delete_by_id(self, id: int) -> bool:
        for book in self.books:
            
            if book.id == id:
                self.books.remove(book)
                return True 
        else:
            return False
        