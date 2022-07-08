from abc import ABC, abstractmethod
from models.requestinfo import RequestInfo
from models.user import User
from requests import request
from exceptions.exceptions import *
import re
from utils.messages import USER_NOT_FOUND, INVALID_REQUEST

class Validator(ABC):
    @abstractmethod
    def _perform_checks():
        pass

class LoginValidator(Validator):

    def __init__(self, request_info: RequestInfo) -> None:
        self.request_info = request_info

    def _validate_request_body_structure(self):
        if not ['email', 'password'] == self.request_info.properties():
            raise InvalidRequestException(INVALID_REQUEST)   
    
    def _validate_fields(self):
        if not self.request_info.email or not self.request_info.password:
            raise InvalidRequestException(INVALID_REQUEST)

    def _perform_checks(self):
        self._validate_request_body_structure()
        self._validate_fields()
        

class RegistrationValidator(Validator):
    def __init__(self, request_info:RequestInfo) -> None:
        self.request_info = request_info
    
    def _validate_request_body_structure(self):
        correct_structure = ["email", "password", "confirm_password"]
        request_structure = self.request_info.properties()
        if not (all(item in correct_structure for item in request_structure) and len(correct_structure) == len(request_structure)):
            raise InvalidRequestException(INVALID_REQUEST)

    def _validate_password(self):
        if not self.request_info.password == self.request_info.confirm_password:
            raise InvalidRequestException(INVALID_REQUEST)

    def _perform_checks(self):
        self._validate_request_body_structure()
        self._validate_password()

