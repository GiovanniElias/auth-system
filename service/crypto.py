import uuid
import hashlib

class Cryptography:

    @staticmethod
    def generate_uuid() -> str:
        return uuid.uuid4().hex

    @staticmethod
    def secure_password(password) -> str:
        salt = Cryptography.generate_uuid()
        hashed_password = hashlib.sha256(
            f'{password}{salt}'.encode('utf-8')).hexdigest()

        return f'{salt}:{hashed_password}'

    