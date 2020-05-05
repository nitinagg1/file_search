import typing
from files_list import FilesRepo
from abc import ABCMeta, abstractmethod



class BaseFilter(object):
    def __init__(self, pattern, file_list_obj):
        # type: (str, FilesRepo) -> None
        self.pattern = pattern
        self.file_list_obj = file_list_obj

    @abstractmethod
    def get_matching_files(self):
        pass


class NameFilter(BaseFilter):

    def get_matching_files(self):
        matching_files = []
        for file in self.file_list_obj.get_filtered_files():
            if self.pattern in file:
                matching_files.append(file)

        return matching_files


class ExtensionFilter(BaseFilter):

    def get_matching_files(self):
        matching_files = []
        for file in self.file_list_obj.get_filtered_files():
            if file.endswith(self.pattern):
                matching_files.append(file)

        return matching_files


class SizeFilter(BaseFilter):

    def get_matching_files(self):
        pass


class TimeStampFilter(BaseFilter):

    def get_matching_files(self):
        pass


FILTER_COMMAND_MAPPING = {

    'n' : NameFilter,
    'e' : ExtensionFilter,
    't' : TimeStampFilter,
    's' : SizeFilter
}