from .base import BaseDB, DBAuth
from .models import PublicationIN, Publication


class PubDB(BaseDB):
    __auth: DBAuth

    def __init__(self, auth: DBAuth):
        self.__auth = auth
        super().__init__(auth)

    def id_exists(self, id: str) -> bool:
        return self.__get(id) != None

    def add_pub(self, pub: PublicationIN):  # -> InsertionResult
        if not self.conforms_to(pub, PublicationIN, False):
            raise ValueError("Data doesnt conform to required Type")

        data = pub.dict()
        result = self.insert("providers", "publications", data)
        return result

    def get_all(self):
        result = self.get_all("porivders", "publications")
        data = [Publication.parse_obj(r) for r in result]

    # def del_pub(self, id: str): # -> DeletionResult
    #     if not self.id_exists(id):
    #         raise ValueError("Not Found")

    #     if not self.conforms_to(source, str, False):
    #         raise ValueError("Data doesnt conform to required Type")

    #     result = self.__delete("providers", "publications", id)

    #     return result
