from typing import Optional
from dbengine import OutputQuery
from models.requestinfo import RequestInfo
from service.token_factory import TokenService
from utils.validator import Validator
from service.auth import AuthService
import config
import service.crypto as crypto
from utils.messages import WRONG_PASSWORD
from models.result import Result
from exceptions.exceptions import WrongPasswordException
from models.user import User
import hashlib


class LoginService(AuthService):
    def __init__(self, request_info: RequestInfo, validator: Validator,
                 result: Result, token_service: TokenService):
        self.request_info = request_info
        self.validator = validator
        self.token_service = token_service
        self.result: Result = result

    def _login(self, user: User):
        token = self.token_service.generate_token(user)
        self.result.build(200, dict(token=token))


    def perform_checks(self, *args):
        self.validator._perform_checks(*args)

    def sign_user(self):
        user: User = User.get_by_email(self.request_info.email)
        crypto._verify_password(self.request_info.password, user.password)
        self._login(user)
