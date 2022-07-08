
from exceptions.exceptions import UserNotFoundException
import psycopg2
import contextlib
from config import DB_CONFIG, DB_INIT

class Query:
    def __init__(self) -> None:
        self.connection = psycopg2.connect(**DB_CONFIG)
        self.cursor = self.connection.cursor()
    
    def close(self) -> None:
        self.cursor.close()
        self.connection.close()
    
    def _query(self,query, args=None):
        if not args:
            return self.cursor.execute(query)  
        return self.cursor.execute(query, args)


class InputQuery(Query):
    def __init__(self) -> None:
        super().__init__()

    def execute(self,query,args=None) -> None:
        self._query(query, args)
        self.connection.commit()
        self.close()


class OutputQuery(Query):
    def fetchone(self, query, args=None):
        self._query(query, args)
        query_result = self.cursor.fetchone()
        self.close()
        if not query_result:
            raise UserNotFoundException()
        return query_result

    def fetchall(self, query, args=None):
        self._query(query, args)
        query_result = self.cursor.fetchall()
        self.close()
        if not query_result:
            raise UserNotFoundException()
        return query_result


