from ingots.entities.book import Book
from ingots.dto.book_dto import BookDto
from ingots.interfaces.in_memory_book_repository import InMemoryBookRepository
from ingots.interfaces.local_storage import LocalStorage
from ingots.use_cases.get_book import GetBook
from ingots.use_cases.get_books import GetBooks
from ingots.use_cases.delete_book import DeleteBook
from ingots.use_cases.save_book import SaveBook

class IngotsUnitTests():

    # Set up a repository and storage for testing.
    repository = InMemoryBookRepository()
    storage = LocalStorage("./tests/")
    example_book = Book(
        0,
        "example_title",
        "example_category",
        "example_author",
        ["tag_one","tag_two","tag_three"]

    )

    repository.save(example_book)
    fd = open("./sample01")
    storage.save_file("./tests/example_file",fd)
    fd.close()

    def test_get_book_use_case(self):
        print("Testing get book from repository...")
        book = GetBook(IngotsUnitTests.repository).execute(0)
        assert book.id == 0, "{} Test Failed".format(self.__repr__())
        print("Test PASSED")


    def test_delete_book_use_case(self):
        print("Testing delete book use case...")
        DeleteBook(IngotsUnitTests.repository).execute(0)
        assert len(IngotsUnitTests.repository.get_all()) == 0, "Test failed."
        print("Test PASSED") 


    def test_save_book_use_case(self):
        print("Testing save book use case...")
        assert SaveBook(BookDto(
                {
                    "title" : "test_title",
                    "category":"test_category",
                    "author": "test_author",
                    "tags":[]
                }
            ),
            IngotsUnitTests.repository,
            IngotsUnitTests.storage,
            None

        ).execute(), "Test FAILED"
        print("Test PASSED")
    

    def test_get_books_use_case(self):
        print("Testing get all book use case...")
        list_of_books = GetBooks(IngotsUnitTests.repository).execute()
        assert len(list_of_books) == 1, "Test Failed"
        print("Test PASSED")
        

if __name__ == '__main__':
    ut = IngotsUnitTests()
    ut.test_get_book_use_case()
    ut.test_delete_book_use_case()
    ut.test_save_book_use_case()
    ut.test_get_books_use_case()
