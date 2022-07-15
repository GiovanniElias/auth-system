import uuid
import hashlib
from exceptions.exceptions import WrongPasswordException
from utils.messages import WRONG_PASSWORD 

def generate_uuid() -> str:
        return uuid.uuid4().hex


def _verify_password(request_password:str, hashed_password: str) -> None:
    salt, password = hashed_password.split(':')
    if not password == hashlib.sha256(
            f'{str(request_password)}{salt}'.encode('utf-8')).hexdigest():
        raise WrongPasswordException(WRONG_PASSWORD)

def secure_password(password:str) -> str:
    salt = generate_uuid()
    hashed_password = hashlib.sha256(
            f'{password}{salt}'.encode('utf-8')).hexdigest()

    return f'{salt}:{hashed_password}'

