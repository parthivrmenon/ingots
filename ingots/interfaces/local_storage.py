
import os
from flask import send_from_directory

from werkzeug.datastructures import FileStorage
from ingots.interfaces.storage import Storage


class LocalStorage(Storage):
    def __init__(self,storage_path) -> None:
        self.storage_path = storage_path

    def save_file(self, filepath: str, file: FileStorage) -> bool:
        try:
            file.save(filepath)
            return True
        except Exception as err:
            return False

    def delete_file(self, filepath: str) -> bool:
        if os.path.exists(filepath):
            os.remove(filepath)
            return True 
        else:
            return False

    def get_file(self, filepath: str) -> FileStorage:
        try:
            return send_from_directory(filepath, as_attachment=True)
        except Exception as err:
            return None

