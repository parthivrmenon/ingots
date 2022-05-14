from abc import ABCMeta, abstractmethod
from cgi import FieldStorage
from typing import List, Union

from ingots.entities.book import Book
from ingots.interfaces.storage import Storage

class BookRepository(metaclass=ABCMeta):
    """
    Interface that encapsulates repository methods for the Book entity.
    """

    @abstractmethod
    def get_all(self) -> List[Book]:
        pass 

    @abstractmethod
    def get_by_id(self,id:int) -> Union[Book,None]:
        pass 

    @abstractmethod
    def save(self, book:Book) -> bool:
        pass

    @abstractmethod
    def delete_by_id(self, id: int) -> bool:
        pass 
