from abc import ABC, abstractmethod

from requests import request
from exceptions.exceptions import *
import re
from config import BAD_REQUEST_MESSAGE


class Validator(ABC):
    @abstractmethod
    def _perform_checks():
        pass

class LoginValidator(Validator):
    def perform_checks(self, user_info):
        self.user_info = user_info
        self._validate_request_body_structure()
        self._validate_email()
        self._validate_username()
        

    def _validate_request_body_structure(self):
        if not {'email', 'password'} == self.user_info.properties():
            raise InvalidRequestException()
    
    def _validate_email(self):
        valid_email_pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

        if not re.match(valid_email_pattern,self.user_info.email):
            raise InvalidRequestException()
    
    
    def _validate_username(self):
        if not self.user_info.username:
            raise InvalidRequestException()


class RegistrationValidator(Validator):
    def __init__(self, user_info) -> None:
        self.user_info = user_info
    
    def validate_request_structure(self):
        correct_structure = ["email", "password", "confirm_password"]
        request_structure = self.user_info.properties()
        if not (all(item in correct_structure for item in request_structure) and len(correct_structure) == len(request_structure)):
            raise InvalidRequestException(BAD_REQUEST_MESSAGE)

    def validate_password(self):
        if not self.user_info.password == self.user_info.confirm_password:
            raise InvalidRequestException(BAD_REQUEST_MESSAGE)

    def _perform_checks(self):
        self.validate_request_structure()
        self.validate_password()

