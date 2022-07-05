from models.requestinfo import RequestInfo
from service.token_factory import TokenService
from utils.validator import Validator
from service.auth import AuthService


class LoginService(AuthService):
    def __init__(self, user_info: RequestInfo, validator: Validator, token_service: TokenService):
        self.password = user_info.password  
        self.email = user_info.email
        self.validator = validator
        self.token_service = token_service

    def login(self):
        self.validator.validate_email(self.email)
        self.authenticator.authenticate(self.password)

    def perform_checks(*args):
        pass

    def sign_user(self, password: str):
        self.login()


        
