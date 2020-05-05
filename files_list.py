from abc import ABCMeta, abstractmethod
import os
from exception_handlers import FilePathInvalid

#making this extendable to be replaced by lets say google storage or S3 bucket
class FilesRepo(object):
    def __init__(self, path):
        path, filtered_files = self.get_validated_path(path)
        self.path = path
        self.filtered_files = filtered_files

    @abstractmethod
    def get_validated_path(self):
        pass

    @abstractmethod
    def get_filtered_files(self):
        pass

    def update_filtered_files(self, filtered_files):
        self.filtered_files = filtered_files

class FilesFromDirectory(FilesRepo):

    def __init__(self, path):
        super(FilesFromDirectory, self).__init__(path)

    def get_validated_path(self, path):
        if path == '.':
            path = os.getcwd()

        if not os.path.isdir(path):
            raise FilePathInvalid()

        #TODO construct relative path as well

        return path, os.listdir(path)

    def get_filtered_files(self):
        # type: () -> object
        return self.filtered_files




