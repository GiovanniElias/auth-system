
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
from config import DB_INIT, CREATE_USER, FIND_USER_BY_EMAIL, FIND_USER_BY_ID
from dbengine import InputQuery, OutputQuery
import service.crypto as crypto

class UserStatus(Enum):
    Locked = 0
    Active = 1


@dataclass
class User:    
    id: str = field(default_factory=crypto.generate_uuid)
    created_at: int = int(datetime.timestamp(datetime.now()))
    status: int = UserStatus.Active.value
    email: str = ""
    password: str = ""

    def properties(self):
        values = vars(self).items()
        return [k[1] for k  in values]

    def insert(self):
        InputQuery().execute(CREATE_USER, self.properties())

    @staticmethod
    def exists(**kwargs):
        if 'email' in kwargs.keys():
            return OutputQuery().fetchone(FIND_USER_BY_EMAIL, [kwargs.get('email')])
        elif 'id' in kwargs.keys():
            return OutputQuery().fetchone(FIND_USER_BY_ID, kwargs.get('id'))
            
    @staticmethod
    def get_by_email(email: str):
        query_result = OutputQuery().fetchone(FIND_USER_BY_EMAIL, [email])
        return User(*query_result)
    
