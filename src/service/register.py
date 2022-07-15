from unittest import result
from click import password_option
from pymongo import HASHED
from models.requestinfo import RequestInfo
from service.token_factory import TokenService
import service.crypto as crypto
from utils.validator import Validator
from service.auth import AuthService
from config import DB_INIT, CREATE_USER
from dbengine import InputQuery
from models.user import User
from models.result import Result

class RegistrationService(AuthService):
    def __init__(self, request_info: RequestInfo, validator: Validator, result: Result):
        self.request_info= request_info
        self.validator = validator
        self.result = result

    def _register(self, user : User):
        user.insert()
        self.result.build(
            200,
            dict(user)
        )

    def perform_checks(self):
        self.validator._perform_checks()

    def sign_user(self):
        new_user = User(
            email=self.request_info.email,
            password=crypto.secure_password(self.request_info.password)
        )
        self._register(new_user)
