from typing import Optional
from dbengine import OutputQuery
from models.requestinfo import RequestInfo
from service.token_factory import TokenService
from utils.validator import Validator
from service.auth import AuthService
import config
from utils.messages import WRONG_PASSWORD
from utils.result import Result
from exceptions.exceptions import WrongPasswordException
from models.user import User
import hashlib


class LoginService(AuthService):
    def __init__(self, request_info: RequestInfo, validator: Validator,
                 result: Result, token_service: TokenService):
        self.request_info = request_info
        self.validator = validator
        self.token_service = token_service
        self.result = result

    def _retrieve_user(self) -> Optional[User]:
        query_result = OutputQuery().fetchone(
            config.FIND_USER_BY_EMAIL, [self.request_info.email])

        return User(*query_result)

    def _verify_password(self, hashed_password: str) -> None:
        salt, password = hashed_password.split(':')
        if not password == hashlib.sha256(
                f'{str(self.request_info.password)}{salt}'.encode('utf-8')).hexdigest():
            raise WrongPasswordException(WRONG_PASSWORD)

    def _login(self, user: User):
        token = self.token_service.generate_token(user)
        self.result.build(200, dict(token=token))

    def perform_checks(self, *args):
        self.validator._perform_checks(*args)

    def sign_user(self):
        user = self._retrieve_user()
        self._verify_password(user.password)
        self._login(user)
