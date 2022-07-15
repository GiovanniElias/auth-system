

class ExceptionCodeMap(dict):
    InvalidRequestException = 400
    ResourceNotFoundException = 404
    UserNotFoundException = 401
    WrongPasswordException = 403
    UnathorizedRequestException = 401

class ExceptionBase(Exception): 
    def __init__(self, message):
        self.message = message
        class_name = self.__class__.__name__
        self.code = eval(f'ExceptionCodeMap.{class_name}')

class InvalidRequestException(ExceptionBase):
    def __init__(self, message):
        super().__init__(message)

class ResourceNotFoundException(ExceptionBase):
    def __init__(self, message):
        super().__init__(message)

class UserNotFoundException(ExceptionBase):
    def __init__(self, message):
        super().__init__(message)

class WrongPasswordException(ExceptionBase):
    def __init__(self, message):
        super().__init__(message)

class UnauthorizedRequestException(ExceptionBase):
    def __init__(self, message):
        super().__init__(message)
