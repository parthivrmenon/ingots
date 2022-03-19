import os
from abc import ABC, abstractmethod
from flask import send_from_directory, abort


import logging
import boto3
from botocore.exceptions import ClientError


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


class S3Storage(Storage):
    def __init__(self, upload_location):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id="AKIAW2AN3TBJVNA57H4I",
            aws_secret_access_key="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"
            )
        self.bucket_name = "ingots"
        self.upload_location = upload_location

    def store(self, file_name, file_object):
        file_path = os.path.join(self.upload_location, file_name)
        file_object.save(file_path)
        response = self.s3_client.upload_file(file_path,self.bucket_name,file_name)
        # TODO: add some logic to confirm upload, then delete temp file.
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
        print(files)

        return files

    def retrieve(self, file_name):
        file_path = os.path.join(self.upload_location, file_name)
        self.s3_client.download_file(self.bucket_name,file_name, file_path)
        try:
            return send_from_directory(self.upload_location,file_name, as_attachment=True)
        except FileNotFoundError:
            return abort(404)


