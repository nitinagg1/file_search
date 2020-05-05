

class BaseException(Exception):
    message = 'unknown error'

    def __init__(self, message=None, code=0):
        super(BaseException, self).__init__(message or self.message)
        self.code = code or self.code


class FilePathInvalid(BaseException):

    def __init__(self, message = None):
        self.message = 'File path invalid ' + message if message else ''
        self.code = 11
