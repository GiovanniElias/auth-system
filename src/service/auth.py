from abc import ABC, abstractmethod
from models.requestinfo import RequestInfo
from service.token_factory import TokenService
from utils.validator import Validator
from models.result import Result
class AuthService(ABC):
    def __init__(self, user_info: RequestInfo, validator: Validator, result: Result, token_service: TokenService = None, ):
        pass

    @abstractmethod
    def perform_checks(self, *args):
        """Performs checks that could vary between different services."""

    @abstractmethod
    def sign_user(self, password: str):
        """Signs user in or up dipending on the service implementing the method."""
    