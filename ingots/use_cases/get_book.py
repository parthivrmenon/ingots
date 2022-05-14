
from typing import Union
from ingots.entities.book import Book
from ingots.interfaces.book_repository import BookRepository


class GetBook:
    def __init__(self, repository : BookRepository):
        self._repository = repository

    def execute(self,id) -> Union[Book, None]:
        book = self._repository.get_by_id(id)
        
        return book
        