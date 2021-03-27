from rethinkdb import RethinkDB
from rethinkdb.net import DefaultConnection as Connection
from pydantic import BaseModel
from typing import List


class DBAuth(BaseModel):
    host: str
    port: int = 28015
    user: str = None
    password: str = None


class BaseDB:
    __max_retries: int = 1
    __auth: DBAuth
    __rdb: RethinkDB = RethinkDB
    __connection: Connection = None

    def __init__(self, auth: DBAuth):
        self.__auth = auth
        self.__rdb = RethinkDB()
        _ = self.__conn()

    def __conn(self) -> Connection:
        """ Returns a connection Objekt """
        if self.__connection == None:
            self.__connection = self.__rdb.connect(
                host=self.__auth.host,
                port=self.__auth.port,
                user=self.__auth.user,
                password=self.__auth.password
            )

        if self.__connection.is_open():
            return self.__connection

        retry = 0
        while retry < self.max_retries:
            if self.__connection.is_open():
                return self.__connection

            self.__connection.reconnect()
            retry += 1

        raise ValueError(
            f"BaseDB: Max Retries exceeded ({self.max_retries})")
        return None

    def status(self) -> bool:
        return self.__conn().is_open()

    def conforms_to(self, data, obj, is_list: bool = False) -> bool:
        """ Checks if an instance conforms to a class """
        if is_list:
            for index in data:
                if not isinstance(index, obj):
                    return False
            return True
        else:
            return isinstance(data, obj)


class BaseDB(BaseDB):
    def __get(self, db: str, tb: str, id: str):
        ref = self.__rdb.db(db).table(tb)
        res = ref.get(id)
        return res

    def __get_multiple(self, db: str, tb: str, id: List[str]):
        ref = self.__rdb.db(db).table(tb)
        res = ref.get_all(id)
        return res
# Insertion


class BaseDB(BaseDB):
    def insert(self, db: str, tb: str, data: dict):
        ref = self.__rdb.db(db).table(tb)

        res = ref.insert(
            data,
            return_changes=True,
            conflict="error"
        ).run(self.__conn())

        if res.get('inserted') == 1:
            return True, None

        try:
            error = res["errors"][0]
        except:
            error = "Unknown Error"

        return False, error

    def insert_all(self, db: str, tb: str, data: List[dict]):
        ref = self.__rdb.db(db).table(tb)
        res = ref.insert(
            data,
            return_changes=True,
            conflict="error"
        ).run(self.__conn())

        if res.get('inserted') == len(data):
            return True, None

        try:
            error = res["errors"][0]
        except:
            error = "Unknown Error"

        return False, error


# Deletion
class BaseDB(BaseDB):
    def __delete(self, db: str, tb: str, id: List[str]):
        ref = self.__rdb.db(db).table(tb)
        res = ref.get_all(id).delete().run(self.__conn())

        if res.get('deleted') == 1:
            return True, None

        try:
            error = res["errors"][0]
        except:
            error = "Unknown Error"

        return False, error


# Updating
class BaseDB(BaseDB):
    def __update(self, db: str, tb: str, data: dict):
        ref = self.__rdb.db(db).table(tb)
        res = ref.insert(
            data,
            return_changes=True,
            conflict="update"
        ).run(self.__conn())

        if res.get('replaced', 0) == 1:
            return True, None

        try:
            error = res["errors"][0]
        except:
            error = "Unknown Error"

        return False, error

    def update_all(self, db: str, tb: str, data: List[dict]):
        ref = self.__rdb.db(db).table(tb)
        res = ref.insert(
            data,
            return_changes=True,
            conflict="update"
        ).run(self.__conn())

        if res.get('replaced', 0) + res.get('inserted', 0) + res.get('unchanged', 0) == len(data):
            return True, None

        try:
            error = res["errors"][0]
        except:
            error = "Unknown Error"

        return False, error
