from enum import Enum

class ExceptionCodeMap(Enum):
    InvalidRequestException = 400
    ResourceNotFoundException = 404

class ExceptionBase(Exception): 
    def __init__(self, message):
        super().__init__()
        self.message = message
        class_name = self.__class__.__name__
        self.code = ExceptionCodeMap(class_name)

class InvalidRequestException(ExceptionBase):
    def __init__(self, message):
        super().__init__()

class ResourceNotFoundException(ExceptionBase):
    def __init__(self, message):
        super().__init__()