import dbengine
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
import uuid
from config import DB_INIT, CREATE_USER
from dbengine import InputQuery, OutputQuery
from service.crypto import Cryptography

class UserStatus(Enum):
    Locked = 0
    Active = 1


@dataclass
class User:    
    id: str = field(default_factory=Cryptography.generate_uuid)
    created_at: int = int(datetime.timestamp(datetime.now()))
    status: int = UserStatus.Active.value
    email: str = ""
    password: str = ""

    def properties(self):
        values = vars(self).items()
        return [k[1] for k  in values]

    def insert(self):
        InputQuery().execute(CREATE_USER, self.properties())