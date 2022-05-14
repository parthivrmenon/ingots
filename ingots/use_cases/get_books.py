

from typing import List
from ingots.entities.book import Book
from ingots.interfaces.book_repository import BookRepository

class GetBooks:
    def __init__(self, repository: BookRepository) -> None:
        self._repository = repository

    def execute(self) -> List[Book]:
        books: List[Book] = self._repository.get_all()
        return books