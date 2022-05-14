

from ingots.interfaces.book_repository import BookRepository


class DeleteBook:
    def __init__(self, repository: BookRepository):
        self._repository = repository

    def execute(self, id: int) -> bool:
        try:
            return self._repository.delete_by_id(id)
        except:
            return False