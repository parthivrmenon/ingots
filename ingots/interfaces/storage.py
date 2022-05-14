from abc import ABCMeta, abstractmethod

from werkzeug.datastructures import FileStorage

class Storage(metaclass=ABCMeta):
    """
    An interdface tha encapsulates storage emthods for a Book.
    """
    @abstractmethod
    def save_file(self,filepath : str, file : FileStorage) -> bool:
        pass 

    @abstractmethod
    def delete_file(self,filepath : str) -> bool:
        pass

    @abstractmethod
    def get_file(self,filepath : str) -> FileStorage:
        pass 

