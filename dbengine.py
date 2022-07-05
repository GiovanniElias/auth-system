
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
        return self.cursor.execute(query) if not args else self.cursor.execute(query, args)


class InputQuery(Query):
    def __init__(self) -> None:
        super().__init__()

    def execute(self,query,args=None) -> None:
        self._query(query, args)
        self.connection.commit()
        self.close()


class OutputQuery(Query):
    def fetchone(self, query, args=None):
        query_result = self._query(query, args)
        if not query_result:
            return False
        self.close()
        return query_result.fetchone()

    def fetchall(self, query, args=None):
        query_result = self._query(query, args)
        if not query_result:
            return False
        self.close()
        return query_result.fetchall()


