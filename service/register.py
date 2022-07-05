from click import password_option
from pymongo import HASHED
from models.requestinfo import RequestInfo
from service.token_factory import TokenService
from service.crypto import Cryptography
from utils.validator import Validator
from service.auth import AuthService
from config import DB_INIT, CREATE_USER
from dbengine import InputQuery
from models.user import User
import uuid
import hashlib


class RegistrationService(AuthService):
    def __init__(self, user_info: RequestInfo, validator: Validator):
        self.user_info = user_info
        self.validator = validator

    def perform_checks(self):
        self.validator._perform_checks()

    def sign_user(self):
        email = self.user_info.email
        password = self.user_info.password
        new_user = User(
            email=email,
            password=Cryptography.secure_password(password)
        )
        new_user.insert()
