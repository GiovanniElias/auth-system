from datetime import datetime
from models.user import User
import jwt
from config import SECRET_KEY
from flask import Request, request
from utils.messages import UNAUTHORIZED_REQUEST, COOKIE_KEY, TOKEN_OK
from exceptions.exceptions import UnauthorizedRequestException
from models.result import Result


class TokenService:
    def __init__(self):
        pass

    def _expires_at(self, issued_at):
        duration = 60*60*12  # 12 hours
        return duration + issued_at

    def generate_token(self, user: User):
        issued_at = int(datetime.timestamp(datetime.now()))

        payload = {
            "iat": issued_at,
            "exp": self._expires_at(issued_at),
            "usr": user.email,
            "pwd": user.password,
        }

        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm="HS256"
        )

    def validate(self, client_request: Request, result: Result) -> None:
        if not client_request.cookies or len(client_request.cookies) == 0:
            raise UnauthorizedRequestException(UNAUTHORIZED_REQUEST)

        token = request.cookies.get(COOKIE_KEY)
        try:
        #if decoding fails, the token is invalid, has invalid signature or has expired
            payload = jwt.decode(
                token,
                SECRET_KEY,
                algorithms="HS256",
                options=dict(
                    verify_signature=True,
                    verify_iat=True
                )
            )
        except Exception as e:
            payload = dict()

        result.build(200, dict(
            message=TOKEN_OK,
            user_id=payload.get("usr")
        ))

