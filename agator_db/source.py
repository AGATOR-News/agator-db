from .base import BaseDB, DBAuth
from .models import Source
from .publication import PubDB


class SourceDB(BaseDB):
    __auth: DBAuth

    def __init__(self, auth: DBAuth):
        self.__auth = auth
        super().__init__(auth)

    def add_source(self, source: SourceIN):  # -> InsertionResult
        pubDB = PubDB(self.__auth)
        if not pubDB.id_exists(source.publication):
            raise ValueError("Publication Unknown")

        if not self.conforms_to(source, Source, False):
            raise ValueError("Data doesnt conform to required Type")

        data = source.dict()
        result = self.insert("providers", "sources", data)

        return result

    def del_source(self, id: str):  # -> InsertionResult
        pubDB = PubDB(self.__auth)
        if not self.id_exists(id):
            raise ValueError("Not Found")

        if not self.conforms_to(source, str, False):
            raise ValueError("Data doesnt conform to required Type")

        data = source.dict()
        result = self.insert("providers", "sources", data)

        return result
