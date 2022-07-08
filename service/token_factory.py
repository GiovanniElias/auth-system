from datetime import datetime
from models.user import User
import jwt 
from config import SECRET_KEY

class TokenService:
    def __init__(self):
        pass
    
    def _expires_at(self, issued_at):
        return (60*60*12) + issued_at

    def generate_token(self, user_info):
        issued_at = int(datetime.timestamp(datetime.now()))
        
        payload = {
            "iat": issued_at,
            "exp": self._expires_at(issued_at),
            "usr": user_info.email,
            "pwd": user_info.password,
        }

        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm="HS256"
        )

            