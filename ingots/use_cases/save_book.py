

from cgi import FieldStorage
from ingots.entities.book import Book
from ingots.dto.book_dto import BookDto
from ingots.interfaces.book_repository import BookRepository
from ingots.interfaces.storage import Storage


class SaveBook:
    """
    SaveBook use case object.
    """
    def __init__(self, book_dto: BookDto, repository: BookRepository, storage_driver: Storage, file: FieldStorage) -> None:
        self.book_dto = book_dto
        self.repository = repository
        self.storage_driver = storage_driver
        self.file = file 

    def execute(self) -> bool:

        try:
            new_book = Book(
                self.book_dto.id,
                self.book_dto.title,
                self.book_dto.category,
                self.book_dto.author,
                self.book_dto.tags
                

            )

            self.repository.save(new_book)

            self.storage_driver.save_file(new_book.title, self.file)
            return True


        except Exception as err:
            print("Could not upload new book {}",format(self.book_dto))
            print(err)
            return False



        
 



