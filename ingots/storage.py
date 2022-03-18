import os
from abc import ABC, abstractmethod
from flask import send_from_directory, abort


class Storage(ABC):
    
    @abstractmethod
    def store(self):
        pass 

    @abstractmethod
    def retrieve(self):
        pass

    @abstractmethod
    def list(self):
        pass


class LocalStorage(Storage):
    def __init__(self, upload_location):
        self.upload_location = upload_location

    def store(self, file_name, file_object):
        file_object.save(os.path.join(self.upload_location, file_name))

    def retrieve(self,file_name):
        try:
            return send_from_directory(self.upload_location,file_name, as_attachment=True)
        except FileNotFoundError:
            return abort(404)

    def list(self):
        files = os.listdir(self.upload_location)
        return files
