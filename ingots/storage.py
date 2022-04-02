from cgi import FieldStorage
import os
from abc import ABC, abstractmethod
from xmlrpc.client import Boolean
from flask import Response, send_from_directory, abort




import logging
import boto3
from botocore.exceptions import ClientError


class Storage(ABC):

    @abstractmethod
    def store(self) -> Boolean:
        pass 

    @abstractmethod
    def retrieve(self) -> Response:
        pass

    @abstractmethod
    def list(self) -> list[str]:
        pass

    @abstractmethod
    def delete(self) ->Boolean:
        pass


class LocalStorage(Storage):
    def __init__(self, upload_location:str):
        self.upload_location = upload_location

    def store(self, file_name:str, file_object:any):
        logging.debug(f"Uploading {file_name} to {self.upload_location}.")
        file_object.save(os.path.join(self.upload_location, file_name))
        return True

    def retrieve(self,file_name):
        try:
            return send_from_directory(self.upload_location,file_name, as_attachment=True)
        except FileNotFoundError:
            print('Could not retrieve',file_name)
            return None

    def list(self) -> list[str]:
        files = os.listdir(self.upload_location)
        return files

    def delete(self,file_name):
        file_path = os.path.join(self.upload_location,file_name)
        if os.path.exists(file_path):
            print(f"Removing temp file {file_path}")
            os.remove(file_path)
            return True



class S3Storage(Storage):
    def __init__(self, upload_location, aws_access_key, aws_secret_key, aws_bucket):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
            )
        self.bucket_name = aws_bucket
        self.upload_location = upload_location

    def store(self, file_name, file_object):
        file_path = os.path.join(self.upload_location, file_name)
        file_object.save(file_path)
        try:
            self.s3_client.upload_file(file_path,self.bucket_name,file_name)
        except Exception as err:
            print(err)
            self.delete_file(file_path)
            return False
            
        self.delete_file(file_path)
        return True

    def delete_file(self, file_path):
        if os.path.exists(file_path):
            print(f"Removing temp file {file_path}")
            os.remove(file_path)

    def list(self):
        files = []
        try:
            file_objects = self.s3_client.list_objects(Bucket=self.bucket_name)["Contents"]
            for file in file_objects:
                files.append(file["Key"])

        except KeyError as e:
            print(e)

        return files

    def retrieve(self, file_name):
        file_path = os.path.join(self.upload_location, file_name)
        self.s3_client.download_file(self.bucket_name,file_name, file_path)
        try:
            return send_from_directory(self.upload_location,file_name, as_attachment=True)
        except FileNotFoundError:
            return abort(404)


